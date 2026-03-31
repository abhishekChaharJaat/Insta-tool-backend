import httpx
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from app.models import DownloadRequest, DownloadResponse
from app.services.instagram_service import fetch_instagram_media
from app.utils.validators import is_valid_instagram_url
from app.core.rate_limiter import limiter

router = APIRouter()

PROXY_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.instagram.com/",
}


@router.post("/download", response_model=DownloadResponse)
@limiter.limit("10/minute")
async def download_instagram_media(
    request: Request,
    body: DownloadRequest,
):
    url = body.url.strip()

    if not url:
        raise HTTPException(status_code=400, detail="URL is required.")

    if not is_valid_instagram_url(url):
        return DownloadResponse(
            success=False,
            error=(
                "Invalid Instagram URL. Please provide a valid link to a "
                "public Instagram post, reel, or IGTV video."
            ),
        )

    result = await fetch_instagram_media(url)
    return DownloadResponse(**result)


@router.get("/proxy-download")
@limiter.limit("10/minute")
async def proxy_download(request: Request, url: str, filename: str = "instatoolkit_reel"):
    """
    Proxy the media file from Instagram CDN so the browser downloads it
    instead of opening it in a new tab.
    """
    if not url.startswith("https://"):
        raise HTTPException(status_code=400, detail="Invalid URL.")

    allowed_hosts = ("cdninstagram.com", "fbcdn.net", "instagram.com")
    if not any(host in url for host in allowed_hosts):
        raise HTTPException(status_code=400, detail="URL not from an allowed host.")

    try:
        client = httpx.AsyncClient(timeout=30, follow_redirects=True)
        resp = await client.get(url, headers=PROXY_HEADERS)

        if resp.status_code != 200:
            raise HTTPException(status_code=502, detail="Failed to fetch media from source.")

        content_type = resp.headers.get("content-type", "video/mp4")
        ext = "mp4" if "video" in content_type else "jpg"
        safe_filename = f"{filename}.{ext}"

        async def stream():
            async for chunk in resp.aiter_bytes(chunk_size=1024 * 64):
                yield chunk
            await client.aclose()

        return StreamingResponse(
            stream(),
            media_type=content_type,
            headers={
                "Content-Disposition": f'attachment; filename="{safe_filename}"',
                "Cache-Control": "no-store",
            },
        )

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Request timed out.")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import re
import asyncio
from typing import Dict, Any
import yt_dlp


def _normalize_url(url: str) -> str:
    url = url.strip().rstrip("/")
    match = re.match(r"(https?://(?:www\.)?instagram\.com/(?:p|reel|tv)/[A-Za-z0-9_-]+)", url)
    return match.group(1) if match else url


def _extract_with_ytdlp(url: str) -> Dict[str, Any]:
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "best",
        "noplaylist": True,
        # Return best quality with direct URL
        "extractor_args": {"instagram": {"include_feed_data": ["1"]}},
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        if not info:
            return {"success": False}

        # Handle playlists (carousels)
        if info.get("_type") == "playlist" and info.get("entries"):
            info = info["entries"][0]

        download_url = info.get("url", "")
        thumbnail = info.get("thumbnail", "")
        description = info.get("description") or info.get("title") or ""
        title = description[:100] if description else "Instagram Media"

        # Detect media type
        vcodec = info.get("vcodec", "")
        acodec = info.get("acodec", "")
        ext = info.get("ext", "")
        is_video_url = download_url.endswith(".mp4") or ".mp4" in download_url
        if vcodec and vcodec != "none":
            media_type = "video"
        elif acodec and acodec != "none":
            media_type = "video"
        elif ext in ("mp4", "mov", "webm") or is_video_url:
            media_type = "video"
        else:
            media_type = "image"

        if not download_url:
            return {"success": False}

        return {
            "success": True,
            "type": media_type,
            "download_url": download_url,
            "thumbnail": thumbnail,
            "title": title,
        }

    except yt_dlp.utils.DownloadError as e:
        err = str(e).lower()
        if "private" in err or "login" in err or "restricted" in err:
            return {
                "success": False,
                "error": "This post is private or requires login. Only public posts can be downloaded.",
            }
        if "not found" in err or "404" in err or "deleted" in err:
            return {
                "success": False,
                "error": "Post not found. It may have been deleted or the URL is invalid.",
            }
        return {"success": False, "error": f"Could not extract media: {str(e)[:200]}"}

    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)[:200]}"}


async def fetch_instagram_media(url: str) -> Dict[str, Any]:
    url = _normalize_url(url)
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, _extract_with_ytdlp, url)

    if not result.get("success") and "error" not in result:
        result["error"] = (
            "Could not extract media. The post may be private, deleted, "
            "or the URL is invalid. Only public posts are supported."
        )

    return result

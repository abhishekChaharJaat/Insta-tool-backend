from fastapi import APIRouter, Request, HTTPException
from app.models import GeneratorRequest, GeneratorResponse
from app.services.generator_service import (
    generate_captions,
    generate_hashtags,
    generate_bios,
)
from app.utils.validators import sanitize_topic, validate_tone
from app.core.rate_limiter import limiter

router = APIRouter()


def _validate_request(body: GeneratorRequest, max_count: int = 20) -> tuple[str, str, int]:
    topic = sanitize_topic(body.topic)
    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required.")
    tone = validate_tone(body.tone or "neutral")
    count = max(1, min(body.count or 5, max_count))
    return topic, tone, count


@router.post("/caption", response_model=GeneratorResponse)
@limiter.limit("30/minute")
async def generate_caption(request: Request, body: GeneratorRequest):
    topic, tone, count = _validate_request(body, max_count=20)
    results = generate_captions(topic, tone, count)
    return GeneratorResponse(success=True, results=results)


@router.post("/hashtags", response_model=GeneratorResponse)
@limiter.limit("30/minute")
async def generate_hashtag(request: Request, body: GeneratorRequest):
    topic, tone, count = _validate_request(body, max_count=30)
    results = generate_hashtags(topic, tone, count)
    return GeneratorResponse(success=True, results=results)


@router.post("/bio", response_model=GeneratorResponse)
@limiter.limit("30/minute")
async def generate_bio(request: Request, body: GeneratorRequest):
    topic, tone, count = _validate_request(body)
    results = generate_bios(topic, tone, count)
    return GeneratorResponse(success=True, results=results)

from pydantic import BaseModel
from typing import Optional, List, Any


class DownloadRequest(BaseModel):
    url: str


class DownloadResponse(BaseModel):
    success: bool
    type: Optional[str] = None
    download_url: Optional[str] = None
    thumbnail: Optional[str] = None
    title: Optional[str] = None
    error: Optional[str] = None


class GeneratorRequest(BaseModel):
    topic: str
    tone: Optional[str] = "neutral"
    count: Optional[int] = 5


class GeneratorResponse(BaseModel):
    success: bool
    results: List[str] = []
    error: Optional[str] = None

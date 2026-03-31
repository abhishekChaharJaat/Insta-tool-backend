import re
from urllib.parse import urlparse


INSTAGRAM_DOMAINS = {"instagram.com", "www.instagram.com", "instagr.am"}

INSTAGRAM_PATH_PATTERNS = [
    r"^/p/[A-Za-z0-9_-]+",       # Posts
    r"^/reel/[A-Za-z0-9_-]+",    # Reels
    r"^/tv/[A-Za-z0-9_-]+",      # IGTV
]


def is_valid_instagram_url(url: str) -> bool:
    try:
        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https"):
            return False
        if parsed.netloc not in INSTAGRAM_DOMAINS:
            return False
        for pattern in INSTAGRAM_PATH_PATTERNS:
            if re.match(pattern, parsed.path):
                return True
        return False
    except Exception:
        return False


def sanitize_topic(topic: str) -> str:
    topic = re.sub(r"[^\w\s#@]", "", topic)
    return topic.strip()[:100]


def validate_tone(tone: str) -> str:
    allowed = {"neutral", "cool", "funny", "motivational", "professional", "casual", "aesthetic"}
    return tone.lower() if tone.lower() in allowed else "neutral"

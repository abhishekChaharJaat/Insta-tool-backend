from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api.routes import download, generator
from app.core.config import settings
from app.core.rate_limiter import limiter

app = FastAPI(
    title="InstaToolkit API",
    description=(
        "Production-ready Instagram tools API. "
        "For personal and educational use only."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Routers
app.include_router(download.router, prefix="/api", tags=["Downloader"])
app.include_router(generator.router, prefix="/api", tags=["Generators"])


@app.get("/", tags=["Health"])
async def root():
    return {
        "name": "InstaToolkit API",
        "version": "1.0.0",
        "status": "running",
        "disclaimer": "For personal and educational use only.",
    }


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}

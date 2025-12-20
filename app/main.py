from fastapi import FastAPI
from app.api.match import router as match_router
from app.core.config import settings
from app.api.ats import router as ats_router

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
)

app.include_router(match_router)
app.include_router(ats_router)


@app.get("/health")
def health():
    return {"status": "ok"}

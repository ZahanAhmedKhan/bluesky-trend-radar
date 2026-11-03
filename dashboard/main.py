from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dashboard.simulator import build_snapshot

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Bluesky Live Trend Radar")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def dashboard_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html", {})


@app.get("/api/overview")
async def overview() -> dict:
    return build_snapshot()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("dashboard.main:app", host="0.0.0.0", port=8000, reload=True)

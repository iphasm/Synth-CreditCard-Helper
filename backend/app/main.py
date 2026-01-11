from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
import os

app = FastAPI(title="TC Helper", version="1.0.0")

from app.api import auth

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "TC Helper"}

# Serve Frontend Static Files (Production)
# Ensure the `static` directory exists or the path is correct after Docker build
static_dir = os.path.join(os.path.dirname(__file__), "../static")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
else:
    # Fallback for local development if not using a proxy
    print(f"Static directory not found at {static_dir}. Running in API-only mode or expected Dev Proxy.")

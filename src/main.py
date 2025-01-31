from fastapi import FastAPI
from .services import sports_monitor
from .core import config

app = FastAPI(title="SportsBot API")

@app.on_event("startup")
async def startup_event():
    # Initialize the sports monitor
    await sports_monitor.start_monitoring()

@app.get("/")
async def root():
    return {"status": "running", "service": "SportsBot"}

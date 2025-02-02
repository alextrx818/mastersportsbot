import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
import yaml
from typing import Optional, Dict, List
from pydantic import BaseModel

# Import our existing BetsAPI client
from src.core.api_client import B365Client
from src.core.sports_data import SportsData

app = FastAPI(
    title="BetsAPI Integration",
    description="API documentation and endpoints for BetsAPI integration",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize our clients
api_client = B365Client()
sports_data = SportsData()

class ErrorResponse(BaseModel):
    success: int = 0
    error: str

class Team(BaseModel):
    name: str
    id: Optional[int] = None

class Timer(BaseModel):
    tm: Optional[str] = None
    q: Optional[str] = None

class League(BaseModel):
    name: str
    id: int

class Match(BaseModel):
    id: int
    sport_id: int
    time_status: str
    league: League
    home: Team
    away: Team
    ss: Optional[str] = None
    timer: Optional[Timer] = None

class MatchResponse(BaseModel):
    success: int = 1
    results: List[Match]

@app.get("/v1/events/inplay", response_model=MatchResponse)
async def get_live_events(
    sport_id: int = Query(..., description="ID of the sport (1=Soccer, 18=Basketball, etc)"),
    league_id: Optional[int] = Query(None, description="Optional league ID to filter results")
):
    """
    Get live events for a specific sport.
    """
    try:
        events = await api_client.get_live_events(sport_id, league_id)
        return {"success": 1, "results": events}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/v1/events/upcoming", response_model=MatchResponse)
async def get_upcoming_events(
    sport_id: int = Query(..., description="ID of the sport"),
    league_id: Optional[int] = Query(None, description="Optional league ID to filter results"),
    day: Optional[str] = Query(None, description="Optional date filter (YYYY-MM-DD)"),
    page: Optional[int] = Query(None, description="Page number for pagination")
):
    """
    Get upcoming events for a specific sport.
    """
    try:
        events = await api_client.get_upcoming_events(sport_id, league_id, day, page)
        return {"success": 1, "results": events}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/v1/event/view/{event_id}", response_model=MatchResponse)
async def get_event_details(event_id: int):
    """
    Get detailed information about a specific event.
    """
    try:
        event = await api_client.get_event_stats(event_id)
        return {"success": 1, "results": [event]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Custom OpenAPI schema that includes our Swagger YAML
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    # Load our custom Swagger YAML
    swagger_path = os.path.join(os.path.dirname(__file__), "docs/betsapi_swagger.yaml")
    with open(swagger_path, 'r') as f:
        custom_schema = yaml.safe_load(f)

    app.openapi_schema = custom_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from ..core.auth import verify_token
from ..core.logging_config import LogConfig
from ..core.debug import api_debug_trace, DEBUG_MODE
from ..services.sports_monitor import SportsMonitor

# Initialize router and logging
router = APIRouter(prefix="/api/v1")
logger = LogConfig.get_component_logger("api")

@router.get("/sports", dependencies=[Depends(verify_token)])
@api_debug_trace
async def get_available_sports():
    """Get list of available sports for monitoring"""
    try:
        sports = ["NBA", "NFL", "MLB", "NHL"]
        logger.info("Retrieved available sports list")
        return {"sports": sports}
    except Exception as e:
        logger.error(f"Error retrieving sports list: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/games/{sport}", dependencies=[Depends(verify_token)])
@api_debug_trace
async def get_live_games(sport: str):
    """Get live games for a specific sport"""
    try:
        monitor = SportsMonitor()
        games = await monitor.get_live_games(sport)
        logger.info(f"Retrieved live games for {sport}")
        return {"games": games}
    except ValueError as e:
        logger.error(f"Invalid sport specified: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error retrieving live games: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/alerts/configure", dependencies=[Depends(verify_token)])
@api_debug_trace
async def configure_alerts(
    sport: str,
    alert_type: str = Query(..., description="Type of alert to configure"),
    threshold: float = Query(..., description="Threshold value for the alert"),
    enabled: bool = Query(True, description="Whether the alert is enabled")
):
    """Configure alerts for a specific sport"""
    try:
        # Add alert configuration logic here
        logger.info(f"Configured {alert_type} alert for {sport}")
        return {
            "status": "success",
            "message": f"Alert configured for {sport}",
            "config": {
                "sport": sport,
                "type": alert_type,
                "threshold": threshold,
                "enabled": enabled
            }
        }
    except Exception as e:
        logger.error(f"Error configuring alert: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/alerts/history", dependencies=[Depends(verify_token)])
@api_debug_trace
async def get_alert_history(
    sport: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    """Get alert history with optional filters"""
    try:
        # Add alert history retrieval logic here
        logger.info("Retrieved alert history")
        return {
            "alerts": [
                # Sample alert history structure
                {
                    "id": "alert_id",
                    "sport": "NBA",
                    "type": "score_difference",
                    "triggered_at": datetime.now().isoformat(),
                    "details": "Score difference exceeded threshold"
                }
            ]
        }
    except Exception as e:
        logger.error(f"Error retrieving alert history: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/patterns/{sport}", dependencies=[Depends(verify_token)])
@api_debug_trace
async def get_patterns(
    sport: str,
    pattern_type: str = Query(..., description="Type of pattern to analyze"),
    timeframe: str = Query("24h", description="Timeframe for pattern analysis")
):
    """Get detected patterns for a specific sport"""
    try:
        # Add pattern analysis logic here
        logger.info(f"Retrieved patterns for {sport}")
        return {
            "patterns": [
                # Sample pattern structure
                {
                    "type": pattern_type,
                    "sport": sport,
                    "detected_at": datetime.now().isoformat(),
                    "description": "Pattern description",
                    "confidence": 0.85
                }
            ]
        }
    except Exception as e:
        logger.error(f"Error analyzing patterns: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

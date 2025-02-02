#!/usr/bin/env python3
"""
Example script demonstrating how to get prematch odds using the v3 API endpoint.
"""

import requests
import json

def decimal_to_american(decimal_odds):
    """Convert decimal odds to American odds format."""
    decimal = float(decimal_odds)
    if decimal >= 2.0:
        american = (decimal - 1) * 100
    else:
        american = -100 / (decimal - 1)
    return int(round(american))

def get_prematch_odds(token, event_id):
    """Get prematch odds for a specific event."""
    url = "https://api.b365api.com/v3/bet365/prematch"
    params = {
        "token": token,
        "FI": event_id
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
        
    data = response.json()
    if data["success"] != 1:
        print("Error: API request failed")
        return None
        
    return data["results"][0]

def parse_asian_handicap(odds_data):
    """Parse and display Asian Handicap odds."""
    asian_lines = odds_data.get("asian_lines", {})
    sp = asian_lines.get("sp", {})
    
    # Get Asian Handicap odds
    ah = sp.get("asian_handicap", {})
    print("\nAsian Handicap:")
    for odd in ah.get("odds", []):
        decimal_odds = odd['odds']
        american_odds = decimal_to_american(decimal_odds)
        print(f"{odd['header']}: {odd['handicap']} @ {decimal_odds} (American: {american_odds:+d})")
        
    # Get Goal Line odds
    gl = sp.get("goal_line", {})
    print("\nGoal Line:")
    for odd in gl.get("odds", []):
        decimal_odds = odd['odds']
        american_odds = decimal_to_american(decimal_odds)
        print(f"{odd['header']} {odd.get('name', '')}: {decimal_odds} (American: {american_odds:+d})")

def main():
    # Example usage
    token = "180846-0nb22aL4DeG73U"
    event_id = "168201273"  # Real Betis vs Athletic Bilbao
    
    print(f"Getting prematch odds for event {event_id}...")
    odds = get_prematch_odds(token, event_id)
    if odds:
        parse_asian_handicap(odds)

if __name__ == "__main__":
    main()

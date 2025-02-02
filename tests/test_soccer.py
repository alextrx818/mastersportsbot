#!/usr/bin/env python3
"""
Test module for soccer match formatting.
Tests the display of live soccer matches with proper score formatting.
"""

import unittest
import requests
import time
import sys

class B365APISync:
    """API client for fetching live soccer events"""
    def __init__(self):
        self.base_url = "https://api.b365api.com/v3"
        self.token = "180846-0nb22aL4DeG73U"

    def get_inplay_events(self, sport='soccer'):
        """Fetch all live soccer events"""
        endpoint = f"{self.base_url}/events/inplay"
        params = {
            'token': self.token,
            'sport_id': 1,  # 1 is for soccer
            'skip_esports': 'true',
            'stats': 'true'
        }
        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            return None
        return response.json()

def format_soccer_match(match):
    """Format soccer match with half information and separate half scores"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', '0-0')
    if score is None:
        score = '0-0'
    
    # Calculate total goals in match
    home_score, away_score = score.split('-')
    total_goals = int(home_score) + int(away_score)
    main_score = str(total_goals)
    
    timer = match.get('timer', {})
    time = str(timer.get('tm', '0'))
    
    # Get scores for each half
    scores = match.get('scores', {})
    first_half = scores.get('1', {'home': '0', 'away': '0'})
    
    try:
        minutes = int(time.split('+')[0] if '+' in time else time)
        is_first_half = minutes <= 45 and time != 'HT'
        
        # Calculate half scores based on current period
        if is_first_half:
            # If in first half, all goals are first half goals
            current_score = score.split('-')
            fh_home = current_score[0]
            fh_away = current_score[1]
            sh_home = '0'
            sh_away = '0'
        else:
            # If in second half/HT, use the stored first half score
            fh_home = first_half.get('home', '0')
            fh_away = first_half.get('away', '0')
            # Calculate second half goals
            current_score = score.split('-')
            sh_home = str(int(current_score[0]) - int(fh_home))
            sh_away = str(int(current_score[1]) - int(fh_away))
    except (ValueError, IndexError):
        # Fallback if there's any error in calculation
        fh_home = '0'
        fh_away = '0'
        sh_home = '0'
        sh_away = '0'
    
    # Format half scores showing goals scored in each half
    first_half_score = f"({fh_home}:{fh_away})"
    second_half_score = f"({sh_home}:{sh_away})"
    
    # Determine period and format time display
    if time == 'HT':
        period = 'Half Time'
        time_display = 'HT'
        show_second_half = False  # Don't show second half scores at HT
    else:
        try:
            minutes = int(time)
            # Check for additional time info
            ts = timer.get('ts', 0)  # Additional seconds in overtime
            ta = timer.get('ta', 0)  # Additional minutes in overtime
            
            if minutes >= 90:
                # If we have additional time
                if ta > 0:
                    time_display = f"90+{ta}"
                else:
                    time_display = "90+"
                period = 'Second Half'
                show_second_half = True
            else:
                time_display = str(minutes)
                if minutes > 45:
                    period = 'Second Half'
                    show_second_half = True
                else:
                    period = 'First Half'
                    show_second_half = False
                
        except ValueError:
            time_display = time
            period = 'First Half'
            show_second_half = False
    
    # Only show second half scores if we're past first half
    # In second half, show first half score first, then second half score
    if show_second_half:
        score_display = f"{first_half_score}-{second_half_score}"
    else:
        score_display = first_half_score
    
    return (f"⚽ {home} - {away}\n"
            f"📊 Score:{main_score} {score_display}\n"
            f"⏰ {time_display}' {period}")

def get_match_time_value(match):
    """Get numeric value for match time for sorting (0' to 90')"""
    timer = match.get('timer', {})
    time = str(timer.get('tm', '0'))
    
    # Convert time to minutes for sorting
    if time == 'HT':
        return 45  # Half time is at 45 minutes
    else:
        try:
            # Handle injury time (e.g., "45+2", "90+3")
            base_time = time.split('+')[0] if '+' in time else time
            return int(base_time)
        except ValueError:
            return 0

def show_live_soccer_events():
    """Fetch and display all live soccer events"""
    api = B365APISync()
    response = api.get_inplay_events()
    
    if not response or 'results' not in response:
        print("\n❌ No live events found")
        return
    
    matches = response['results']
    
    # Sort matches by their current play time (0' to 90')
    matches.sort(key=get_match_time_value)
    
    print(f"\n📡 Found {len(matches)} live soccer events:\n")
    
    current_league = None
    for match in matches:
        league = match.get('league', {}).get('name', 'Unknown League')
        
        # Print league header when it changes
        if league != current_league:
            if current_league is not None:
                print("----------------------------------------")
            print(f"🏆 {league}")
            current_league = league
        
        # Print match info
        print(format_soccer_match(match))
        print("----------------------------------------")

class TestSoccerFormat(unittest.TestCase):
    """Test cases for soccer match formatting"""
    
    def test_first_half(self):
        """Test formatting for a match in first half"""
        match = {
            'home': {'name': 'Barcelona'},
            'away': {'name': 'Real Madrid'},
            'ss': '2-1',
            'timer': {'tm': '35'},
            'scores': {
                '1': {'home': '2', 'away': '1'}
            }
        }
        expected = ("⚽ Barcelona - Real Madrid\n"
                   "📊 Score:3 (2:1)\n"
                   "⏰ 35' First Half")
        self.assertEqual(format_soccer_match(match), expected)

    def test_halftime(self):
        """Test formatting for a match at halftime"""
        match = {
            'home': {'name': 'Liverpool'},
            'away': {'name': 'Chelsea'},
            'ss': '1-1',
            'timer': {'tm': 'HT'},
            'scores': {
                '1': {'home': '1', 'away': '1'}
            }
        }
        expected = ("⚽ Liverpool - Chelsea\n"
                   "📊 Score:2 (1:1)\n"
                   "⏰ HT' Half Time")
        self.assertEqual(format_soccer_match(match), expected)

    def test_second_half(self):
        """Test formatting for a match in second half"""
        match = {
            'home': {'name': 'Manchester City'},
            'away': {'name': 'Arsenal'},
            'ss': '3-1',
            'timer': {'tm': '75'},
            'scores': {
                '1': {'home': '2', 'away': '0'},
                '2': {'home': '1', 'away': '1'}
            }
        }
        expected = ("⚽ Manchester City - Arsenal\n"
                   "📊 Score:4 (2:0)-(1:1)\n"
                   "⏰ 75' Second Half")
        self.assertEqual(format_soccer_match(match), expected)

    def test_overtime(self):
        """Test formatting for a match in overtime"""
        match = {
            'home': {'name': 'Manchester City'},
            'away': {'name': 'Arsenal'},
            'ss': '3-1',
            'timer': {'tm': '90+3'},
            'scores': {
                '1': {'home': '2', 'away': '0'},
                '2': {'home': '1', 'away': '1'}
            }
        }
        expected = ("⚽ Manchester City - Arsenal\n"
                   "📊 Score:4 (2:0)-(1:1)\n"
                   "⏰ 90+3' Second Half")
        self.assertEqual(format_soccer_match(match), expected)

if __name__ == '__main__':
    if '--live' in sys.argv:
        show_live_soccer_events()
    else:
        unittest.main()

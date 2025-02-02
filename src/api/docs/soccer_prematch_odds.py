#!/usr/bin/env python3
"""
Comprehensive soccer odds script that shows:
1. Live match information with proper score formatting
2. Prematch odds in both decimal and American formats
"""

import requests
import json
import sys
from datetime import datetime

class SoccerOddsClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.b365api.com/v1"

    def decimal_to_american(self, decimal_odds):
        """Convert decimal odds to American odds format."""
        decimal = float(decimal_odds)
        if decimal >= 2.0:
            american = (decimal - 1) * 100
        else:
            american = -100 / (decimal - 1)
        return int(round(american))

    def get_live_events(self):
        """Get all live soccer events."""
        endpoint = f"{self.base_url}/events/inplay"
        params = {
            'token': self.token,
            'sport_id': 1,  # 1 is for soccer
            'skip_esports': 'true',
            'stats': 'true'
        }
        
        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            print(f"Error fetching live events: {response.status_code}")
            return []
            
        data = response.json()
        if not data.get('success'):
            print("Error: API request failed")
            return []
            
        return data.get('results', [])

    def get_live_event_odds(self, event_id, home_team=None, away_team=None):
        """Get odds for a live event using both inplay and event endpoints."""
        # First get the list of live events
        inplay_endpoint = f"{self.base_url}/bet365/inplay_filter"
        params = {
            'token': self.token,
            'sport_id': 1,  # 1 is for soccer
            'odds_market': 1  # Money line odds
        }
        try:
            response = requests.get(inplay_endpoint, params=params, timeout=10)
            if response.status_code != 200:
                print(f"Error fetching inplay events: {response.status_code}")
                return None
            data = response.json()
            if not data.get('success'):
                print("Error: Inplay API request failed")
                return None
            
            # Find the specific event in the results to get its FI
            results = data.get('results', [])
            event_fi = None
            
            # Handle case where results is a list of lists
            if results and isinstance(results[0], list):
                results = results[0]
            
            # Try to match by team names
            if home_team and away_team:
                for event in results:
                    if not isinstance(event, dict):
                        continue
                    event_home = event.get('home', {}).get('name', '')
                    event_away = event.get('away', {}).get('name', '')
                    
                    # Simple string matching
                    if (home_team.lower() in event_home.lower() or event_home.lower() in home_team.lower()) and \
                       (away_team.lower() in event_away.lower() or event_away.lower() in away_team.lower()):
                        event_fi = event.get('FI')
                        break
            
            if not event_fi:
                # Fallback to ID matching
                for event in results:
                    if not isinstance(event, dict):
                        continue
                    if str(event.get('id', '')) == str(event_id):
                        event_fi = event.get('FI')
                        break
            
            if not event_fi:
                return None

            # Now get the event details using the FI
            event_endpoint = f"{self.base_url}/bet365/event"
            event_params = {
                'token': self.token,
                'FI': event_fi
            }
            event_response = requests.get(event_endpoint, params=event_params, timeout=10)
            if event_response.status_code != 200:
                print(f"Error fetching event details: {event_response.status_code}")
                return None
            event_data = event_response.json()
            if not event_data.get('success'):
                print("Error: Event API request failed")
                return None
            
            return event_data
        except Exception as e:
            print(f"Error fetching odds: {e}")
            return None

    def parse_live_odds(self, odds_data):
        """Parse and return formatted money line (1x2) odds data for live events."""
        if not odds_data or not isinstance(odds_data, dict):
            return {'money_line': []}

        results = odds_data.get('results', [])
        if not results or not isinstance(results, list):
            return {'money_line': []}

        # If results is a list but first item is also a list, get the first item
        if results and isinstance(results[0], list):
            results = results[0]

        money_line = []
        try:
            # For live events, look for the FT.1X2 market
            for market in results:
                if isinstance(market, dict) and market.get('MG') == 1:  # 1 is typically Full Time 1X2
                    odds = market.get('MA', [])
                    for odd in odds:
                        if not isinstance(odd, dict):
                            continue
                        
                        name = odd.get('NA', '')  # Team name or Draw
                        price = float(odd.get('OD', 0))  # Odds in decimal format
                        
                        # Convert to American odds
                        if price >= 2:
                            american = int((price - 1) * 100)
                        else:
                            american = int(-100 / (price - 1)) if price != 1 else -10000

                        money_line.append({
                            'type': name,
                            'decimal': price,
                            'american': american
                        })
        except Exception as e:
            print(f"Error parsing live odds: {e}")
            return {'money_line': []}

        return {'money_line': money_line}

    def get_prematch_odds(self, event_id):
        """Get pre-match odds using the start_sp endpoint."""
        endpoint = f"{self.base_url}/bet365/start_sp"
        params = {
            'token': self.token,
            'FI': event_id
        }
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            if response.status_code != 200:
                print(f"Error fetching pre-match odds: {response.status_code}")
                return None
            data = response.json()
            if not data.get('success'):
                print("Error: Pre-match API request failed")
                return None
            
            return data
        except Exception as e:
            print(f"Error fetching pre-match odds: {e}")
            return None

    def parse_prematch_odds(self, odds_data):
        """Parse and return formatted money line (1x2) odds data for pre-match odds."""
        if not odds_data or not isinstance(odds_data, dict):
            return {'money_line': []}

        results = odds_data.get('results', [])
        if not results:
            return {'money_line': []}

        money_line = []
        try:
            # For pre-match odds, look for the FT.1X2 market
            for market in results:
                if isinstance(market, dict) and market.get('MG') == 1:  # 1 is typically Full Time 1X2
                    odds = market.get('MA', [])
                    for odd in odds:
                        if not isinstance(odd, dict):
                            continue
                        
                        name = odd.get('NA', '')  # Team name or Draw
                        price = float(odd.get('OD', 0))  # Odds in decimal format
                        
                        # Convert to American odds
                        if price >= 2:
                            american = int((price - 1) * 100)
                        else:
                            american = int(-100 / (price - 1)) if price != 1 else -10000

                        money_line.append({
                            'type': name,
                            'decimal': price,
                            'american': american
                        })
                    break  # Found the market we want
        except Exception as e:
            print(f"Error parsing pre-match odds: {e}")
            return {'money_line': []}

        return {'money_line': money_line}

    def get_match_time_value(self, match):
        """Get numeric value for match time for sorting (0' to 90+')."""
        timer = match.get('timer', {})
        time = str(timer.get('tm', '0'))
        
        if time == 'HT':
            return 45
        elif time == 'Break':
            return 90
        else:
            try:
                if '+' in time:
                    base_time, extra_time = time.split('+')
                    return int(base_time) + int(extra_time) * 0.1
                return int(time)
            except ValueError:
                return 0

    def format_soccer_match(self, match, odds):
        """Format soccer match with emojis, scores, time and odds"""
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
        timer_type = timer.get('tt')  # 0 = stopped/break, 1 = running
        
        # Get scores for each half
        scores = match.get('scores', {})
        first_half = scores.get('1', {'home': '0', 'away': '0'})
        
        try:
            minutes = int(time.split('+')[0] if '+' in time else time)
            is_first_half = minutes <= 45 and time != 'HT'
            
            # Calculate half scores
            if is_first_half:
                current_score = score.split('-')
                fh_home = current_score[0]
                fh_away = current_score[1]
                sh_home = '0'
                sh_away = '0'
            else:
                fh_home = first_half.get('home', '0')
                fh_away = first_half.get('away', '0')
                current_score = score.split('-')
                sh_home = str(int(current_score[0]) - int(fh_home))
                sh_away = str(int(current_score[1]) - int(fh_away))
        except (ValueError, IndexError):
            fh_home = '0'
            fh_away = '0'
            sh_home = '0'
            sh_away = '0'

        first_half_score = f"({fh_home}:{fh_away})"
        second_half_score = f"({sh_home}:{sh_away})"

        # Determine period and format time display
        if time == 'HT' or (minutes == 45 and timer_type == '0'):
            period = 'Half Time Break'
            time_display = 'HT'
            show_second_half = False
        elif time == 'Break':
            period = 'Break'
            time_display = 'Break'
            show_second_half = True
        else:
            try:
                minutes = int(time)
                ts = timer.get('ts', 0)
                ta = timer.get('ta', 0)
                
                if minutes >= 90:
                    if ta > 0:
                        time_display = f"90+{ta}"
                    elif ts > 0:
                        overtime_mins = (ts + 30) // 60
                        time_display = f"90+{overtime_mins}"
                    else:
                        time_display = "90"
                    period = 'Second Half'
                    show_second_half = True
                elif minutes > 45:
                    time_display = str(minutes)
                    period = 'Second Half'
                    show_second_half = True
                elif minutes == 45:
                    if ta > 0:
                        time_display = f"45+{ta}"
                    elif ts > 0:
                        overtime_mins = (ts + 30) // 60
                        time_display = f"45+{overtime_mins}"
                    else:
                        time_display = "45"
                    period = 'First Half'
                    show_second_half = False
                else:
                    time_display = str(minutes)
                    period = 'First Half'
                    show_second_half = False
            except ValueError:
                time_display = time
                period = 'First Half'
                show_second_half = False

        if show_second_half:
            score_display = f"{first_half_score}-{second_half_score}"
        else:
            score_display = first_half_score

        # Format the match info with emojis
        match_info = (f"⚽ {home} - {away}\n"
                     f"📊 Score:{main_score} {score_display}\n"
                     f"⏰ {time_display}' {period}")

        # Add odds information
        match_info += "\n---------------------------------------- PREMATCH ODDS ----------------------------------------\n\n"
        match_info += odds

        return match_info

    def display_odds(self, event, live_odds=None, prematch_odds=None):
        """Display both live and pre-match odds for an event."""
        league = event.get('league', {}).get('name', 'Unknown League')
        home = event.get('home', {}).get('name', 'Unknown Home')
        away = event.get('away', {}).get('name', 'Unknown Away')
        score = event.get('ss', '0-0')
        
        # Format time
        time = event.get('time', '')
        if time.isdigit():
            from datetime import datetime
            try:
                time_obj = datetime.fromtimestamp(int(time))
                time = time_obj.strftime('%H:%M')
            except:
                time = 'Unknown Time'
        elif not time:
            time = 'Unknown Time'
        
        # Format score display
        try:
            home_score, away_score = score.split('-')
            score_display = f"{home_score} ({score})"
        except:
            score_display = score
        
        print(f"\n {league}\n")
        print(f"⚽ {home} - {away}")
        print(f"📊 Score:{score_display}")
        print(f"⏰ {time}")
        
        print("-" * 40 + " LIVE ODDS " + "-" * 40)
        
        # Display live odds
        if live_odds and live_odds.get('money_line'):
            print("\n Money Line (1X2) - Live Odds:")
            for odd in live_odds['money_line']:
                print(f"{odd['type']}: {odd['decimal']} (American: {odd['american']})")
        else:
            print("\n Money Line (1X2) - Live Odds:")
            print("No money line odds available")
        
        print("\n" + "-" * 40 + " PREMATCH ODDS " + "-" * 39)
        
        # Display pre-match odds
        if prematch_odds and prematch_odds.get('money_line'):
            print("\n Money Line (1X2) - Pre-match Odds:")
            for odd in prematch_odds['money_line']:
                print(f"{odd['type']}: {odd['decimal']} (American: {odd['american']})")
        else:
            print("\n Money Line (1X2) - Pre-match Odds:")
            print("No money line odds available")
        
        print("\n" + "=" * 80)

def main():
    client = SoccerOddsClient("180846-0nb22aL4DeG73U")
    
    print("\nFetching live soccer events...")
    events = client.get_live_events()
    
    if not events:
        print("No live events found.")
        return
    
    print(f"\n Found {len(events)} live events")
    
    for event in events:
        if not isinstance(event, dict):
            print("Error: Invalid event format")
            continue
            
        event_id = event.get('id')
        if not event_id:
            print("Error: Event ID not found")
            continue
            
        try:
            # Get team names for matching
            home_team = event.get('home', {}).get('name', '')
            away_team = event.get('away', {}).get('name', '')
            
            # Get live odds
            live_odds_data = client.get_live_event_odds(event_id, home_team, away_team)
            live_odds = client.parse_live_odds(live_odds_data) if live_odds_data else None
            
            # Get pre-match odds
            prematch_odds_data = client.get_prematch_odds(event_id)
            prematch_odds = client.parse_prematch_odds(prematch_odds_data) if prematch_odds_data else None
            
            # Display both live and pre-match odds
            client.display_odds(event, live_odds, prematch_odds)
        except Exception as e:
            print(f"Error processing event {event_id}: {str(e)}")
            continue

if __name__ == "__main__":
    main()

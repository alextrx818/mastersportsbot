"""Sports Analyzer Agent"""
import os
import sys
import json
import redis

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)

from src.core.b365api import B365APISync, SportID

class SportsAnalyzer:
    """AI agent for analyzing sports data and suggesting improvements"""
    
    def __init__(self):
        """Initialize the analyzer"""
        self.api = B365APISync()
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def analyze_live_events(self, sport_id=None):
        """Analyze live events for patterns"""
        try:
            # Get events
            if sport_id:
                events = self.api.get_inplay_events(sport_id)
            else:
                # Get events for all sports
                events = {}
                for sport in SportID:
                    sport_events = self.api.get_inplay_events(sport.value)
                    events[sport.name] = sport_events
            
            # Analyze patterns
            analysis = self._analyze_patterns(events)
            
            # Store in Redis
            self.redis_client.setex(
                f"analysis:{sport_id or 'all'}", 
                3600,  # expire in 1 hour
                json.dumps(analysis)
            )
            
            return analysis
            
        except Exception as e:
            return {'error': str(e)}
    
    def _analyze_patterns(self, events):
        """Analyze events for interesting patterns"""
        patterns = {
            'by_sport': {},
            'suggested_alerts': []
        }
        
        # Analyze each sport's events
        for sport_name, sport_events in events.items():
            sport_patterns = {
                'scoring_patterns': self._analyze_scoring(sport_events),
                'time_patterns': self._analyze_time(sport_events),
                'momentum_shifts': self._analyze_momentum(sport_events)
            }
            patterns['by_sport'][sport_name] = sport_patterns
            
            # Generate alert suggestions
            alerts = self._suggest_alerts(sport_name, sport_patterns)
            patterns['suggested_alerts'].extend(alerts)
        
        return patterns
    
    def _analyze_scoring(self, events):
        """Analyze scoring patterns"""
        patterns = []
        for event in events.get('results', []):
            if 'ss' in event:
                try:
                    scores = event['ss'].split('-')
                    home = int(scores[0])
                    away = int(scores[1])
                    diff = abs(home - away)
                    
                    if 5 <= diff <= 15:
                        patterns.append({
                            'type': 'comeback_potential',
                            'event_id': event['id'],
                            'description': f'Team trailing by {diff} points'
                        })
                except (IndexError, ValueError):
                    continue
        return patterns
    
    def _analyze_time(self, events):
        """Analyze time-based patterns"""
        patterns = []
        for event in events.get('results', []):
            if 'time' in event:
                try:
                    time = int(event['time'])
                    if time >= 80:  # Late game
                        patterns.append({
                            'type': 'late_game',
                            'event_id': event['id'],
                            'description': f'Late game situation at {time} minutes'
                        })
                except (ValueError, TypeError):
                    continue
        return patterns
    
    def _analyze_momentum(self, events):
        """Analyze momentum shifts"""
        patterns = []
        for event in events.get('results', []):
            if 'scores' in event:
                scores = event['scores']
                periods = sorted(scores.keys())
                if len(periods) >= 2:
                    last = periods[-1]
                    prev = periods[-2]
                    try:
                        last_diff = abs(scores[last]['home'] - scores[last]['away'])
                        prev_diff = abs(scores[prev]['home'] - scores[prev]['away'])
                        if abs(last_diff - prev_diff) >= 5:
                            patterns.append({
                                'type': 'momentum_shift',
                                'event_id': event['id'],
                                'description': 'Significant momentum shift detected'
                            })
                    except (KeyError, TypeError):
                        continue
        return patterns
    
    def _suggest_alerts(self, sport, patterns):
        """Suggest possible alerts based on patterns"""
        suggestions = []
        
        # Score-based alerts
        if any(p['type'] == 'comeback_potential' for p in patterns.get('scoring_patterns', [])):
            suggestions.append({
                'sport': sport,
                'type': 'score_alert',
                'condition': 'comeback',
                'description': 'Alert when a team reduces deficit by X points in Y minutes'
            })
        
        # Time-based alerts
        if any(p['type'] == 'late_game' for p in patterns.get('time_patterns', [])):
            suggestions.append({
                'sport': sport,
                'type': 'time_alert',
                'condition': 'late_game',
                'description': 'Alert for close games in final minutes'
            })
        
        # Momentum alerts
        if any(p['type'] == 'momentum_shift' for p in patterns.get('momentum_shifts', [])):
            suggestions.append({
                'sport': sport,
                'type': 'momentum_alert',
                'condition': 'shift',
                'description': 'Alert when significant momentum shift is detected'
            })
        
        return suggestions

# Create analyzer instance
analyzer = SportsAnalyzer()

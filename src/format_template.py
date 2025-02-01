"""
Template module for experimenting with new sports data formatting.
This will serve as a sandbox for format changes before updating the main sports_format.py
"""

SPORTS = {
    1: {'name': 'Soccer', 'emoji': '⚽'},
    18: {'name': 'Basketball', 'emoji': '🏀'},
    13: {'name': 'Tennis', 'emoji': '🎾'},
    91: {'name': 'Volleyball', 'emoji': '🏐'},
    17: {'name': 'Ice Hockey', 'emoji': '🏒'},
    14: {'name': 'Snooker', 'emoji': '🎱'},
    78: {'name': 'Handball', 'emoji': '🤾‍♀️'},
    15: {'name': 'Darts', 'emoji': '🎯'},
    92: {'name': 'Table Tennis', 'emoji': '🏓'}
}

def format_soccer_match(match):
    """Format a soccer match with the current template"""
    pass

def format_basketball_match(match):
    """Format a basketball match with the current template"""
    pass

def format_tennis_match(match):
    """Format a tennis match with the current template"""
    pass

def format_volleyball_match(match):
    """Format a volleyball match with the current template"""
    pass

def format_hockey_match(match):
    """Format a hockey match with the current template"""
    pass

def format_match(match, sport_id):
    """Main format function that routes to sport-specific formatters"""
    pass

# Test data to help with format development
SAMPLE_MATCH_DATA = {
    'soccer': {
        'home': {'name': 'Team A'},
        'away': {'name': 'Team B'},
        'ss': '2-1',
        'time_status': '1',
        'timer': {'tm': '65', 'tt': '2'},
        'league': {'name': 'Premier League'}
    },
    'basketball': {
        'home': {'name': 'Team X'},
        'away': {'name': 'Team Y'},
        'ss': '78-82',
        'timer': {'q': '3', 'tm': '4:35'},
        'scores': {'1': '22-24', '2': '18-20', '3': '38-38'}
    }
    # Add more sample data for other sports as needed
}

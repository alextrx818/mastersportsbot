"""
This module contains all the formatting functions for different sports.
Each sport has its own format function that handles the specific display requirements.
"""

def format_soccer_match(match):
    """Format soccer match with half information and separate half scores"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    timer = match.get('timer', {})
    time = str(timer.get('tm', '0'))  # Convert to string
    
    # Get scores for each half
    scores = match.get('scores', {})
    first_half = scores.get('1', {'home': '0', 'away': '0'})
    second_half = scores.get('2', {'home': '0', 'away': '0'})
    
    # Format half scores
    first_half_score = f"{first_half.get('home', '0')}-{first_half.get('away', '0')}"
    second_half_score = f"{second_half.get('home', '0')}-{second_half.get('away', '0')}"
    
    # Determine period based on time
    is_second_half = False
    if time == 'HT':
        period = ''
        time_display = 'HT'
    else:
        time_display = f"{time}'"
        # Handle injury time (e.g., "45+2", "90+3")
        base_time = time.split('+')[0] if '+' in time else time
        try:
            minutes = int(base_time)
            is_second_half = minutes > 45
            period = f"({['1H', '2H'][is_second_half]})"
        except ValueError:
            period = ''
    
    # Format the scores line based on period
    scores_line = f"1H: {first_half_score}"
    if is_second_half:
        scores_line += f" | 2H: {second_half_score}"
    
    # Format the output
    return (f"⚽ {home} {score} {away}\n"
            f"{scores_line}\n"
            f"⏰ {time_display}{' ' + period if period else ''}")

def format_basketball_match(match):
    """Format basketball match with quarter-by-quarter scores"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    scores = match.get('scores', {})
    
    # Get current quarter and time
    timer = match.get('timer', {})
    current_quarter = int(timer.get('q', '1'))
    time_left = timer.get('tm', '0')
    
    # Initialize quarter scores
    quarter_scores = []
    
    # Get current total score
    current_score = match.get('ss', '0-0')
    
    # Get quarter scores directly (API provides individual quarter scores)
    for q in range(1, min(current_quarter + 1, 5)):  # Max 4 quarters
        quarter = str(q)
        if quarter in scores:
            score = scores[quarter]
            try:
                home_score = int(score['home'])
                away_score = int(score['away'])
                quarter_scores.append(f"Q{q}:{home_score}-{away_score}")
            except:
                continue
    
    # Format quarter scores
    quarters_display = ' | '.join(quarter_scores) if quarter_scores else ''
    
    return f"🏀 {home} vs {away}\n⏰ {time_left}' Q{current_quarter} ({current_score})\n📊 {quarters_display}\n"

def format_hockey_match(match):
    """Format hockey match with period-by-period scores"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    scores = match.get('scores', {})
    period_scores = []
    
    # Get current period
    current_period = int(match.get('timer', {}).get('p', '1'))
    
    # Track running total to calculate individual period scores
    home_total = 0
    away_total = 0
    
    # Only show scores up to the current period
    for i in range(1, current_period + 1):
        period = str(i)
        if period in scores:
            period_score = scores[period]
            current_home = int(period_score['home']) - home_total
            current_away = int(period_score['away']) - away_total
            period_scores.append(f"P{i}: {current_home}-{current_away}")
            home_total = int(period_score['home'])
            away_total = int(period_score['away'])
    
    period_info = ' | '.join(period_scores) if period_scores else ''
    current_score = match.get('ss', '0-0')
    
    timer = match.get('timer', {})
    time = timer.get('tm', '0')
    
    return f"🏒 {home} {current_score} {away}\n⏰ {time}' (P{current_period})\n📊 {period_info}"

def format_volleyball_match(match):
    """Format volleyball match with set scores"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    scores = match.get('scores', {})
    set_scores = []
    
    # Get set scores
    for i in range(1, 6):  # Volleyball can have up to 5 sets
        set_score = scores.get(str(i))
        if set_score:
            set_scores.append(f"{set_score['home']}-{set_score['away']}")
    
    sets_display = ' | '.join(set_scores)
    current_score = match.get('ss', '0-0')
    
    return f"🏐 {home} vs {away}\n📊 Sets: {sets_display}\n⏰ Current Set: {current_score}"

def format_tennis_match(match):
    """Format tennis match with set information"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', '')
    
    # Get the current set
    completed_sets = score.count(',')
    current_set = completed_sets + 1
    
    return f"🎾 {home} {score} {away}\n⏰ 0' (Set {current_set})"

def format_snooker_match(match):
    """Format snooker match with frame information"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    frame = match.get('timer', {}).get('f', '1')
    
    return f"🎱 {home} {score} {away}\n⏰ 0' (Frame {frame})"

def format_handball_match(match):
    """Format handball match with half information"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    time = match.get('timer', {}).get('tm', '0')
    
    # Determine half
    half = '1H' if int(time) <= 30 else '2H'
    
    return f"🤾‍♀️ {home} {score} {away}\n⏰ {time}' ({half})"

def format_darts_match(match):
    """Format darts match with set and leg information"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    timer = match.get('timer', {})
    set_info = timer.get('set', '1')
    leg = timer.get('leg', '1')
    
    return f"🎯 {home} {score} {away}\n⏰ 0' (Set {set_info} Leg {leg})"

def format_table_tennis_match(match):
    """Format table tennis match with game information"""
    home = match.get('home', {}).get('name', 'Unknown')
    away = match.get('away', {}).get('name', 'Unknown')
    score = match.get('ss', 'vs')
    game = match.get('timer', {}).get('game', '1')
    
    return f"🏓 {home} {score} {away}\n⏰ 0' (Game {game})"

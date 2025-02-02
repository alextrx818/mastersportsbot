import requests
import json
import os
from typing import Dict, List

# Create samples directory
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), 'samples')
os.makedirs(SAMPLES_DIR, exist_ok=True)

# List of sample files to fetch
SAMPLES = {
    'inplay': 'Inplay Events',
    'upcoming': 'Upcoming Events',
    'ended': 'Ended Events',
    'search': 'Events Search',
    'event_view': 'Event View',
    'event_history': 'Event History',
    'event_odds_summary': 'Event Odds Summary',
    'event_odds': 'Event Odds',
    'event_stats_trend': 'Event Stats Trend',
    'event_lineup': 'Event Lineup',
    'league': 'League',
    'league_table': 'League Table',
    'league_toplist': 'League TopList',
    'team': 'Team',
    'team_squad': 'Team Squad',
    'team_members': 'Team Members',
    'player': 'Player',
    'tennis_ranking': 'Tennis Ranking',
    'merge_history': 'Merge History'
}

def fetch_sample(name: str) -> Dict:
    """Fetch a sample JSON file from BetsAPI docs"""
    url = f"https://betsapi.com/docs/samples/{name}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {name}: {str(e)}")
        return {}

def save_sample(name: str, data: Dict):
    """Save sample data to a JSON file"""
    filepath = os.path.join(SAMPLES_DIR, f"{name}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def update_docs_with_samples():
    """Update documentation with sample responses"""
    doc_path = os.path.join(os.path.dirname(__file__), 'sportsbet_api_doc.md')
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add samples section if it doesn't exist
    if '## Sample Responses' not in content:
        content += '\n\n## Sample Responses\n'
        
        for name, title in SAMPLES.items():
            sample_path = os.path.join('samples', f'{name}.json')
            content += f'\n### {title}\n'
            content += f'See [`{sample_path}`](samples/{name}.json) for sample response.\n'

    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("Fetching sample responses...")
    for name in SAMPLES:
        print(f"Fetching {name}...")
        data = fetch_sample(name)
        if data:
            save_sample(name, data)
    
    print("Updating documentation...")
    update_docs_with_samples()
    print("Done!")

if __name__ == "__main__":
    main()

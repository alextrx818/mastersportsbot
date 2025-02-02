import requests
import json
import os

# Create the samples directory if it doesn't exist
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), 'samples')
os.makedirs(SAMPLES_DIR, exist_ok=True)

# List of JSON sample URLs
urls = {
    "Inplay Events": "https://betsapi.com/docs/samples/inplay.json",
    "Upcoming Events": "https://betsapi.com/docs/samples/upcoming.json",
    "Ended Events": "https://betsapi.com/docs/samples/ended.json",
    "Events Search": "https://betsapi.com/docs/samples/search.json",
    "Event View": "https://betsapi.com/docs/samples/event_view.json",
    "Event History": "https://betsapi.com/docs/samples/event_history.json",
    "Event Odds Summary": "https://betsapi.com/docs/samples/event_odds_summary.json",
    "Event Odds": "https://betsapi.com/docs/samples/event_odds.json",
    "Event Stats Trend": "https://betsapi.com/docs/samples/event_stats_trend.json",
    "Event Lineup": "https://betsapi.com/docs/samples/event_lineup.json",
    "League": "https://betsapi.com/docs/samples/league.json",
    "League Table": "https://betsapi.com/docs/samples/league_table.json",
    "League TopList": "https://betsapi.com/docs/samples/league_toplist.json",
    "Team": "https://betsapi.com/docs/samples/team.json",
    "Team Squad": "https://betsapi.com/docs/samples/team_squad.json",
    "Team Members": "https://betsapi.com/docs/samples/team_members.json",
    "Player": "https://betsapi.com/docs/samples/player.json",
    "Tennis Ranking": "https://betsapi.com/docs/samples/tennis_ranking.json",
    "Merge History": "https://betsapi.com/docs/samples/merge_history.json"
}

# Fetching and saving the data
for name, url in urls.items():
    try:
        print(f"Fetching data for '{name}'...")
        response = requests.get(url)
        response.raise_for_status()  # Ensure we catch any request errors
        data = response.json()

        # Create filename and full path
        filename = f'{name.replace(" ", "_").lower()}.json'
        filepath = os.path.join(SAMPLES_DIR, filename)

        # Save to a JSON file
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Data for '{name}' saved successfully to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for '{name}': {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON for '{name}': {e}")
    except Exception as e:
        print(f"Unexpected error for '{name}': {e}")

print("\nAll done! Files are saved in:", SAMPLES_DIR)

import sys
sys.path.append('/root/sportsbot/src')
from agents.loopgpt_tools import agent

def analyze_sport_endpoints():
    print("\nAsking LoopGPT to analyze sport-specific endpoints...")
    
    result = agent.tools["betsapi_doc_analyzer"].run("""
    Please analyze the BetsAPI documentation focusing on endpoints for specific sports:

    1. For each of these sports:
       - Soccer (sport_id=1)
       - Basketball (sport_id=18)
       - Volleyball (sport_id=91)
    
    Provide:
    1. Live event endpoint details:
       - How to get live events for each sport
       - Sport-specific parameters
       - Example API calls
    
    2. Prematch odds endpoint details:
       - How to get upcoming events
       - How to get odds
       - Sport-specific markets
       
    3. Historical data:
       - How to access past events
       - How to get historical odds
       
    Please include full endpoint URLs and all required parameters.
    """)
    
    print("\nLoopGPT Sport-Specific Analysis Results:")
    print(result)

if __name__ == "__main__":
    analyze_sport_endpoints()

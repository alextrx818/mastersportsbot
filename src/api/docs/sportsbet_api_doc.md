# Bets API Documentation

## Overview
Bets API is a RESTful service providing comprehensive sports data. This is a paid service starting at $10 per month.

## Authentication
Authentication can be done in two ways:

### Via Header:
```shell
curl "api_endpoint_here" -H "X-API-TOKEN: YOUR-TOKEN"
```

### Via Query Parameter:
```shell
curl "api_endpoint_here?token=YOUR-TOKEN"
```
Replace YOUR-TOKEN with your personal token obtained from support or Orders page.

## Base URL
All API endpoints start with: `https://api.betsapi.com/v1`

## Rate Limits
- Standard: 3,600 requests per hour
- Premium: 199,999 requests per hour (additional $50 for standalone server)

Rate limit headers:
- `X-RateLimit-Limit`: Maximum requests per hour
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Reset time in UTC epoch seconds

## API Endpoints

### Events API

#### 1. InPlay Events
```
GET https://api.betsapi.com/v1/events/inplay
```
Parameters:
- sport_id (required)
- league_id (optional)
- page (optional)

#### 2. Upcoming Events
```
GET https://api.betsapi.com/v1/events/upcoming
```
Parameters:
- sport_id (required)
- league_id (optional)
- team_id (optional)
- cc (optional) - Country code, e.g., 'co' for Colombia
- day (optional) - Format: YYYYMMDD
- page (optional)

#### 3. Ended Events
```
GET https://api.betsapi.com/v1/events/ended
```
Parameters:
- sport_id (required)
- league_id (optional)
- team_id (optional)
- cc (optional)
- day (optional)
- page (optional)

#### 4. Events Search
```
GET https://api.betsapi.com/v1/events/search
```
Parameters:
- sport_id (required)
- home (required) - Team ID or name
- away (required) - Team ID or name
- time (required) - UTC epoch or YYYYMMDD

### Event Details

#### 1. Event View
```
GET https://api.betsapi.com/v1/event/view
```
Parameters:
- event_id (required) - Support multiple IDs (max 10) with comma separation

#### 2. Event History
```
GET https://api.betsapi.com/v1/event/history
```
Parameters:
- event_id (required)
- qty (optional) - Default 10, range 1-20

#### 3. Event Odds
```
GET https://api.betsapi.com/v1/event/odds
```
Parameters:
- event_id (required)
- source (optional) - Default: bet365
- since_time (optional)

### League API

#### 1. League Information
```
GET https://api.betsapi.com/v1/league
```
Parameters:
- sport_id (required)
- cc (optional)
- page (optional)

#### 2. League Table
```
GET https://api.betsapi.com/v1/league/table
```
Parameters:
- league_id (required)

#### 3. League TopList
```
GET https://api.betsapi.com/v1/league/toplist
```
Parameters:
- league_id (required)

### Team API
```
GET https://api.betsapi.com/v1/team
```
Parameters:
- sport_id (required)
- page (optional)

### Bet365 Specific Endpoints

#### 1. Bet365 InPlay
```
GET https://api.betsapi.com/v1/bet365/inplay
```
Parameters:
- raw (optional) - Raw Bet365 body

#### 2. Bet365 Event
```
GET https://api.betsapi.com/v1/bet365/event
```
Parameters:
- FI (required)
- stats (optional)
- lineup (optional)
- raw (optional)

#### 3. Bet365 Upcoming Events
```
GET https://api.betsapi.com/v1/bet365/upcoming
```
Parameters:
- sport_id (required)
- league_id (optional)
- day (optional)
- page (optional)

## Response Format
All responses are in JSON format and include a `success` key indicating the request status. Successful requests return results in the response body, while failed requests return an error message.

## Notes
- Bet365 API features require additional permissions
- Some features require "Soccer Enhanced API" permission
- Team IDs may not be available for all teams (less than 5% of cases)
- Contact support for custom requirements or issues


## Sample Responses

### Inplay Events
See [`samples/inplay.json`](samples/inplay.json) for sample response.

### Upcoming Events
See [`samples/upcoming.json`](samples/upcoming.json) for sample response.

### Ended Events
See [`samples/ended.json`](samples/ended.json) for sample response.

### Events Search
See [`samples/search.json`](samples/search.json) for sample response.

### Event View
See [`samples/event_view.json`](samples/event_view.json) for sample response.

### Event History
See [`samples/event_history.json`](samples/event_history.json) for sample response.

### Event Odds Summary
See [`samples/event_odds_summary.json`](samples/event_odds_summary.json) for sample response.

### Event Odds
See [`samples/event_odds.json`](samples/event_odds.json) for sample response.

### Event Stats Trend
See [`samples/event_stats_trend.json`](samples/event_stats_trend.json) for sample response.

### Event Lineup
See [`samples/event_lineup.json`](samples/event_lineup.json) for sample response.

### League
See [`samples/league.json`](samples/league.json) for sample response.

### League Table
See [`samples/league_table.json`](samples/league_table.json) for sample response.

### League TopList
See [`samples/league_toplist.json`](samples/league_toplist.json) for sample response.

### Team
See [`samples/team.json`](samples/team.json) for sample response.

### Team Squad
See [`samples/team_squad.json`](samples/team_squad.json) for sample response.

### Team Members
See [`samples/team_members.json`](samples/team_members.json) for sample response.

### Player
See [`samples/player.json`](samples/player.json) for sample response.

### Tennis Ranking
See [`samples/tennis_ranking.json`](samples/tennis_ranking.json) for sample response.

### Merge History
See [`samples/merge_history.json`](samples/merge_history.json) for sample response.

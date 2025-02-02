# BetsAPI JSON Structures


## League

League information and details

### Structure

```json

{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 100,
    "total": 1665
  },
  "results": [
    {
      "id": "1",
      "name": "Mexico Liga de Ascenso Apertura",
      "cc": "mx",
      "has_leaguetable": 1,
      "has_toplist": 0
    },
    {
      "id": "2",
      "name": "Australia New South Wales League 2",
      "cc": "au",
      "has_leaguetable": 0,
      "has_toplist": 0
    },
    {
      "id": "3",
      "name": "Australia Queensland Premier League Women",
      "cc": "au",
      "has_leaguetable": 0,
      "has_toplist": 0
    },
    {
      "id": "4",
      "name": "Australia New South Wales U20 League",
      "cc": "au",
      "has_leaguetable": 0,
      "has_toplist": 0
    },
    {
      "id": "5",
      "name": "Australia WA Premier League Women",
      "cc": "au",
      "has_leaguetable": 0,
      "has_toplist": 0
    },
    {
      "id": "6",
      "name": "Fiji Cup",
      "cc": "fj",
      "has_leaguetable": 0,
      "has_toplist": 0
    },
    {
    

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **pager** (object)
  Pager
  Example: `{'page': 1, 'per_page': 100, 'total': 1665}`
  Nested fields:
  - **page** (integer)
    Page
    Example: `1`
  - **per_page** (integer)
    Per Page
    Example: `100`
  - **total** (integer)
    Total
    Example: `1665`
- **results** (array[object])
  Results
  Example: `{'id': '1', 'name': 'Mexico Liga de Ascenso Apertura', 'cc': 'mx', 'has_leaguetable': 1, 'has_toplis`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `1`
  - **name** (string)
    Display name
    Example: `Mexico Liga de Ascenso Apertura`
  - **cc** (string)
    Country code
    Example: `mx`
  - **has_leaguetable** (integer)
    Has Leaguetable
    Example: `1`
  - **has_toplist** (integer)
    Has Toplist
    Example: `0`

---

## Event History

Event History data

### Structure

```json

{
  "success": 1,
  "results": {
    "h2h": [
      {
        "id": "199439",
        "sport_id": "1",
        "league": {
          "id": "849",
          "name": "China Super League",
          "cc": "cn"
        },
        "home": {
          "id": "10121",
          "name": "Liaoning Hongyun",
          "image_id": "41429",
          "cc": "cn"
        },
        "away": {
          "id": "43806",
          "name": "Guangzhou R&F",
          "image_id": "3375",
          "cc": "cn"
        },
        "time": "1466924400",
        "ss": "3-1",
        "time_status": "3"
      }
    ],
    "home": [
      {
        "id": "199690",
        "sport_id": "1",
        "league": {
          "id": "849",
          "name": "China Super League",
          "cc": "cn"
        },
        "home": {
          "id": "11377",
          "name": "Changchun Yatai",
          "image_id": "34694",
          "cc": "cn"
        },
        "away": {
          "id": "10121",
          "name": "Liaoning Hongy

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'h2h': [{'id': '199439', 'sport_id': '1', 'league': {'id': '849', 'name': 'China Super League', 'cc`
  Nested fields:
  - **h2h** (array[object])
    H2H
    Example: `{'id': '199439', 'sport_id': '1', 'league': {'id': '849', 'name': 'China Super League', 'cc': 'cn'},`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `199439`
    - **sport_id** (string)
      Sport identifier
      Example: `1`
    - **league** (object)
      League information
      Example: `{'id': '849', 'name': 'China Super League', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `849`
      - **name** (string)
        Display name
        Example: `China Super League`
      - **cc** (string)
        Country code
        Example: `cn`
    - **home** (object)
      Home team information
      Example: `{'id': '10121', 'name': 'Liaoning Hongyun', 'image_id': '41429', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `10121`
      - **name** (string)
        Display name
        Example: `Liaoning Hongyun`
      - **image_id** (string)
        ID of the team/player image
        Example: `41429`
      - **cc** (string)
        Country code
        Example: `cn`
    - **away** (object)
      Away team information
      Example: `{'id': '43806', 'name': 'Guangzhou R&F', 'image_id': '3375', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `43806`
      - **name** (string)
        Display name
        Example: `Guangzhou R&F`
      - **image_id** (string)
        ID of the team/player image
        Example: `3375`
      - **cc** (string)
        Country code
        Example: `cn`
    - **time** (string)
      Unix timestamp
      Example: `1466924400`
    - **ss** (string)
      Current score
      Example: `3-1`
    - **time_status** (string)
      Status of the event (0=not started, 1=in play, 3=ended)
      Example: `3`
  - **home** (array[object])
    Home team information
    Example: `{'id': '199690', 'sport_id': '1', 'league': {'id': '849', 'name': 'China Super League', 'cc': 'cn'},`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `199690`
    - **sport_id** (string)
      Sport identifier
      Example: `1`
    - **league** (object)
      League information
      Example: `{'id': '849', 'name': 'China Super League', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `849`
      - **name** (string)
        Display name
        Example: `China Super League`
      - **cc** (string)
        Country code
        Example: `cn`
    - **home** (object)
      Home team information
      Example: `{'id': '11377', 'name': 'Changchun Yatai', 'image_id': '34694', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `11377`
      - **name** (string)
        Display name
        Example: `Changchun Yatai`
      - **image_id** (string)
        ID of the team/player image
        Example: `34694`
      - **cc** (string)
        Country code
        Example: `cn`
    - **away** (object)
      Away team information
      Example: `{'id': '10121', 'name': 'Liaoning Hongyun', 'image_id': '41429', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `10121`
      - **name** (string)
        Display name
        Example: `Liaoning Hongyun`
      - **image_id** (string)
        ID of the team/player image
        Example: `41429`
      - **cc** (string)
        Country code
        Example: `cn`
    - **time** (string)
      Unix timestamp
      Example: `1491721200`
    - **ss** (string)
      Current score
      Example: `1-1`
    - **time_status** (string)
      Status of the event (0=not started, 1=in play, 3=ended)
      Example: `3`
  - **away** (array[object])
    Away team information
    Example: `{'id': '183606', 'sport_id': '1', 'league': {'id': '849', 'name': 'China Super League', 'cc': 'cn'},`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `183606`
    - **sport_id** (string)
      Sport identifier
      Example: `1`
    - **league** (object)
      League information
      Example: `{'id': '849', 'name': 'China Super League', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `849`
      - **name** (string)
        Display name
        Example: `China Super League`
      - **cc** (string)
        Country code
        Example: `cn`
    - **home** (object)
      Home team information
      Example: `{'id': '11289', 'name': 'Guangzhou Evergrande', 'image_id': '24156', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `11289`
      - **name** (string)
        Display name
        Example: `Guangzhou Evergrande`
      - **image_id** (string)
        ID of the team/player image
        Example: `24156`
      - **cc** (string)
        Country code
        Example: `cn`
    - **away** (object)
      Away team information
      Example: `{'id': '43806', 'name': 'Guangzhou R&F', 'image_id': '3375', 'cc': 'cn'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `43806`
      - **name** (string)
        Display name
        Example: `Guangzhou R&F`
      - **image_id** (string)
        ID of the team/player image
        Example: `3375`
      - **cc** (string)
        Country code
        Example: `cn`
    - **time** (string)
      Unix timestamp
      Example: `1491651300`
    - **ss** (string)
      Current score
      Example: `2-2`
    - **time_status** (string)
      Status of the event (0=not started, 1=in play, 3=ended)
      Example: `3`

---

## Player

Player information and statistics

### Structure

```json

{
  "success": 1,
  "results": {
    "player": {
      "id": "750",
      "name": "Cristiano Ronaldo",
      "cc": "pt",
      "birthdate": "1985-02-05",
      "position": "Forward",
      "height": "185",
      "weight": "80",
      "foot": "Both"
    },
    "transfers": [
      {
        "start": "0",
        "end": "0",
        "type_id": "1",
        "active": "1",
        "team": {
          "id": "4509",
          "name": "Portugal",
          "image_id": "4704",
          "cc": "pt"
        }
      },
      {
        "start": "962409600",
        "end": "1025395200",
        "type_id": "1",
        "active": "0",
        "team": {
          "id": "6163",
          "name": "Sporting U19",
          "image_id": "78151",
          "cc": "pt"
        }
      },
      {
        "start": "1025481600",
        "end": "1060560000",
        "type_id": "1",
        "active": "0",
        "team": {
          "id": "1046",
          "name": "Sporting",
          "image_id": "3001",
        

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'player': {'id': '750', 'name': 'Cristiano Ronaldo', 'cc': 'pt', 'birthdate': '1985-02-05', 'positi`
  Nested fields:
  - **player** (object)
    Player
    Example: `{'id': '750', 'name': 'Cristiano Ronaldo', 'cc': 'pt', 'birthdate': '1985-02-05', 'position': 'Forwa`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `750`
    - **name** (string)
      Display name
      Example: `Cristiano Ronaldo`
    - **cc** (string)
      Country code
      Example: `pt`
    - **birthdate** (string)
      Birthdate
      Example: `1985-02-05`
    - **position** (string)
      Position
      Example: `Forward`
    - **height** (string)
      Height
      Example: `185`
    - **weight** (string)
      Weight
      Example: `80`
    - **foot** (string)
      Foot
      Example: `Both`
  - **transfers** (array[object])
    Transfers
    Example: `{'start': '0', 'end': '0', 'type_id': '1', 'active': '1', 'team': {'id': '4509', 'name': 'Portugal',`
    Nested fields:
    - **start** (string)
      Start
      Example: `0`
    - **end** (string)
      End
      Example: `0`
    - **type_id** (string)
      Type Id
      Example: `1`
    - **active** (string)
      Active
      Example: `1`
    - **team** (object)
      Team
      Example: `{'id': '4509', 'name': 'Portugal', 'image_id': '4704', 'cc': 'pt'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `4509`
      - **name** (string)
        Display name
        Example: `Portugal`
      - **image_id** (string)
        ID of the team/player image
        Example: `4704`
      - **cc** (string)
        Country code
        Example: `pt`
  - **events** (array[object])
    Events
    Example: `{'team_uid': '2687', 'starting': '1', 'substitutedIn': '0', 'substitutedOut': '0', 'minutesplayed': `
    Nested fields:
    - **team_uid** (string)
      Team Uid
      Example: `2687`
    - **starting** (string)
      Starting
      Example: `1`
    - **substitutedIn** (string)
      Substitutedin
      Example: `0`
    - **substitutedOut** (string)
      Substitutedout
      Example: `0`
    - **minutesplayed** (string)
      Minutesplayed
      Example: `90`
    - **goals** (string)
      Goals
      Example: `0`
    - **assists** (string)
      Assists
      Example: `0`
    - **yellowcard** (string)
      Yellowcard
      Example: ``
    - **yellowredcard** (string)
      Yellowredcard
      Example: ``
    - **redcard** (string)
      Redcard
      Example: ``
    - **shots** (string)
      Shots
      Example: `6`
    - **shots_on_goal** (string)
      Shots On Goal
      Example: `2`
    - **blocked_shots** (string)
      Blocked Shots
      Example: `2`
    - **corner** (string)
      Corner
      Example: `0`
    - **offside** (string)
      Offside
      Example: `0`
    - **updated_at** (string)
      Updated At
      Example: `1535763017`
    - **event** (object)
      Event
      Example: `{'id': '849303', 'sport_id': '1', 'league': {'id': '199', 'name': 'Italy Serie A', 'cc': 'it'}, 'hom`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `849303`
      - **sport_id** (string)
        Sport identifier
        Example: `1`
      - **league** (object)
        League information
        Example: `{'id': '199', 'name': 'Italy Serie A', 'cc': 'it'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `199`
        - **name** (string)
          Display name
          Example: `Italy Serie A`
        - **cc** (string)
          Country code
          Example: `it`
      - **home** (object)
        Home team information
        Example: `{'id': '22228', 'name': 'Juventus', 'image_id': '2687', 'cc': 'it'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `22228`
        - **name** (string)
          Display name
          Example: `Juventus`
        - **image_id** (string)
          ID of the team/player image
          Example: `2687`
        - **cc** (string)
          Country code
          Example: `it`
      - **away** (object)
        Away team information
        Example: `{'id': '43865', 'name': 'Lazio', 'image_id': '2699', 'cc': 'it'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `43865`
        - **name** (string)
          Display name
          Example: `Lazio`
        - **image_id** (string)
          ID of the team/player image
          Example: `2699`
        - **cc** (string)
          Country code
          Example: `it`
      - **time** (string)
        Unix timestamp
        Example: `1535212800`
      - **ss** (string)
        Current score
        Example: `2-0`
      - **time_status** (string)
        Status of the event (0=not started, 1=in play, 3=ended)
        Example: `3`

---

## Team Squad

Team Squad data

### Structure

```json

{
  "success": 1,
  "results": [
    {
      "id": "6019",
      "name": "Vincent Kompany",
      "cc": "be",
      "birthdate": "1986-04-09",
      "position": "Defender",
      "height": "193",
      "weight": "85",
      "foot": "Right",
      "shirtnumber": "4"
    },
    {
      "id": "11781",
      "name": "David Silva",
      "cc": "es",
      "birthdate": "1986-01-07",
      "position": "Midfielder",
      "height": "173",
      "weight": "67",
      "foot": "Left",
      "shirtnumber": "21"
    },
    {
      "id": "13249",
      "name": "Claudio Bravo",
      "cc": "cl",
      "birthdate": "1983-04-12",
      "position": "Guard",
      "height": "184",
      "weight": "80",
      "foot": "Right",
      "shirtnumber": "1"
    },
    {
      "id": "13630",
      "name": "Fernandinho",
      "cc": "br",
      "birthdate": "1985-05-03",
      "position": "Midfielder",
      "height": "179",
      "weight": "67",
      "foot": "Right",
      "shirtnumber": "25"
    },
    {
      

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (array[object])
  Results
  Example: `{'id': '6019', 'name': 'Vincent Kompany', 'cc': 'be', 'birthdate': '1986-04-09', 'position': 'Defend`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `6019`
  - **name** (string)
    Display name
    Example: `Vincent Kompany`
  - **cc** (string)
    Country code
    Example: `be`
  - **birthdate** (string)
    Birthdate
    Example: `1986-04-09`
  - **position** (string)
    Position
    Example: `Defender`
  - **height** (string)
    Height
    Example: `193`
  - **weight** (string)
    Weight
    Example: `85`
  - **foot** (string)
    Foot
    Example: `Right`
  - **shirtnumber** (string)
    Shirtnumber
    Example: `4`

---

## Event View

Detailed information about a specific match/event

### Structure

```json

{
  "success": 1,
  "results": [
    {
      "id": "2654397",
      "sport_id": "1",
      "time": "1602952200",
      "time_status": "3",
      "league": {
        "id": "94",
        "name": "England Premier League",
        "cc": "gb"
      },
      "home": {
        "id": "708",
        "name": "Man City",
        "image_id": "17",
        "cc": "gb"
      },
      "away": {
        "id": "17230",
        "name": "Arsenal",
        "image_id": "42",
        "cc": "gb"
      },
      "ss": "1-0",
      "scores": {
        "2": {
          "home": "1",
          "away": "0"
        },
        "1": {
          "home": "1",
          "away": "0"
        }
      },
      "stats": {
        "attacks": [
          "145",
          "69"
        ],
        "ball_safe": [
          "79",
          "79"
        ],
        "corners": [
          "6",
          "6"
        ],
        "corner_f": [
          "6",
          "6"
        ],
        "corner_h": [
          "4",
          "4"
       

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (array[object])
  Results
  Example: `{'id': '2654397', 'sport_id': '1', 'time': '1602952200', 'time_status': '3', 'league': {'id': '94', `
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `2654397`
  - **sport_id** (string)
    Sport identifier
    Example: `1`
  - **time** (string)
    Unix timestamp
    Example: `1602952200`
  - **time_status** (string)
    Status of the event (0=not started, 1=in play, 3=ended)
    Example: `3`
  - **league** (object)
    League information
    Example: `{'id': '94', 'name': 'England Premier League', 'cc': 'gb'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `94`
    - **name** (string)
      Display name
      Example: `England Premier League`
    - **cc** (string)
      Country code
      Example: `gb`
  - **home** (object)
    Home team information
    Example: `{'id': '708', 'name': 'Man City', 'image_id': '17', 'cc': 'gb'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `708`
    - **name** (string)
      Display name
      Example: `Man City`
    - **image_id** (string)
      ID of the team/player image
      Example: `17`
    - **cc** (string)
      Country code
      Example: `gb`
  - **away** (object)
    Away team information
    Example: `{'id': '17230', 'name': 'Arsenal', 'image_id': '42', 'cc': 'gb'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `17230`
    - **name** (string)
      Display name
      Example: `Arsenal`
    - **image_id** (string)
      ID of the team/player image
      Example: `42`
    - **cc** (string)
      Country code
      Example: `gb`
  - **ss** (string)
    Current score
    Example: `1-0`
  - **scores** (object)
    Detailed scores by period
    Example: `{'2': {'home': '1', 'away': '0'}, '1': {'home': '1', 'away': '0'}}`
    Nested fields:
    - **2** (object)
      2
      Example: `{'home': '1', 'away': '0'}`
      Nested fields:
      - **home** (string)
        Home team information
        Example: `1`
      - **away** (string)
        Away team information
        Example: `0`
    - **1** (object)
      1
      Example: `{'home': '1', 'away': '0'}`
      Nested fields:
      - **home** (string)
        Home team information
        Example: `1`
      - **away** (string)
        Away team information
        Example: `0`
  - **stats** (object)
    Match statistics
    Example: `{'attacks': ['145', '69'], 'ball_safe': ['79', '79'], 'corners': ['6', '6'], 'corner_f': ['6', '6'],`
    Nested fields:
    - **attacks** (array[string])
      Attacks
      Example: `['145', '69']`
    - **ball_safe** (array[string])
      Ball Safe
      Example: `['79', '79']`
    - **corners** (array[string])
      Corners
      Example: `['6', '6']`
    - **corner_f** (array[string])
      Corner F
      Example: `['6', '6']`
    - **corner_h** (array[string])
      Corner H
      Example: `['4', '4']`
    - **dangerous_attacks** (array[string])
      Dangerous Attacks
      Example: `['57', '30']`
    - **fouls** (array[string])
      Fouls
      Example: `['15', '10']`
    - **freekicks** (array[string])
      Freekicks
      Example: `['12', '15']`
    - **goalattempts** (array[string])
      Goalattempts
      Example: `['9', '7']`
    - **goalkicks** (array[string])
      Goalkicks
      Example: `['10', '4']`
    - **goals** (array[string])
      Goals
      Example: `['1', '0']`
    - **injuries** (array[string])
      Injuries
      Example: `['0', '1']`
    - **offsides** (array[string])
      Offsides
      Example: `['0', '2']`
    - **off_target** (array[string])
      Off Target
      Example: `['8', '8']`
    - **on_target** (array[string])
      On Target
      Example: `['5', '3']`
    - **penalties** (array[string])
      Penalties
      Example: `['0', '0']`
    - **possession_rt** (array[string])
      Possession Rt
      Example: `['56', '44']`
    - **redcards** (array[string])
      Redcards
      Example: `['0', '0']`
    - **saves** (array[string])
      Saves
      Example: `['3', '4']`
    - **shots_blocked** (array[string])
      Shots Blocked
      Example: `['4', '2']`
    - **substitutions** (array[string])
      Substitutions
      Example: `['2', '3']`
    - **throwins** (array[string])
      Throwins
      Example: `['13', '15']`
    - **yellowcards** (array[string])
      Yellowcards
      Example: `['4', '1']`
  - **extra** (object)
    Extra
    Example: `{'away_manager': {'id': '1152', 'name': 'Mikel Arteta', 'cc': 'es'}, 'home_manager': {'id': '53463',`
    Nested fields:
    - **away_manager** (object)
      Away Manager
      Example: `{'id': '1152', 'name': 'Mikel Arteta', 'cc': 'es'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `1152`
      - **name** (string)
        Display name
        Example: `Mikel Arteta`
      - **cc** (string)
        Country code
        Example: `es`
    - **home_manager** (object)
      Home Manager
      Example: `{'id': '53463', 'name': 'Pep Guardiola', 'cc': 'es'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `53463`
      - **name** (string)
        Display name
        Example: `Pep Guardiola`
      - **cc** (string)
        Country code
        Example: `es`
    - **length** (string)
      Length
      Example: `90`
    - **home_pos** (string)
      Home Pos
      Example: `14`
    - **away_pos** (string)
      Away Pos
      Example: `5`
    - **referee** (object)
      Referee
      Example: `{'id': '107059', 'name': 'Chris Kavanagh', 'cc': 'gb'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `107059`
      - **name** (string)
        Display name
        Example: `Chris Kavanagh`
      - **cc** (string)
        Country code
        Example: `gb`
    - **stadium** (string)
      Stadium
      Example: `Etihad Stadium`
    - **stadium_data** (object)
      Stadium Data
      Example: `{'id': '606', 'name': 'Etihad Stadium', 'city': 'Manchester', 'country': 'England', 'capacity': '467`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `606`
      - **name** (string)
        Display name
        Example: `Etihad Stadium`
      - **city** (string)
        City
        Example: `Manchester`
      - **country** (string)
        Country
        Example: `England`
      - **capacity** (string)
        Capacity
        Example: `46708`
      - **googlecoords** (string)
        Googlecoords
        Example: `53.484592,-2.202695`
    - **round** (string)
      Round
      Example: `5`
  - **events** (array[object])
    Events
    Example: `{'id': '69731049', 'text': '0:0 Cards 00:00 - 09:59'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `69731049`
    - **text** (string)
      Text
      Example: `0:0 Cards 00:00 - 09:59`
  - **has_lineup** (integer)
    Has Lineup
    Example: `1`
  - **inplay_created_at** (string)
    Inplay Created At
    Example: `1602951336`
  - **inplay_updated_at** (string)
    Inplay Updated At
    Example: `1602959006`
  - **confirmed_at** (string)
    Confirmed At
    Example: `1603489817`
  - **bet365_id** (string)
    Bet365 Id
    Example: `93624166`

---

## Event Stats Trend

Event Stats Trend data

### Structure

```json

{
  "success": 1,
  "results": {
    "attacks": {
      "away": [
        {
          "time_str": "0",
          "val": "3"
        },
        {
          "time_str": "1",
          "val": "4"
        },
        {
          "time_str": "2",
          "val": "6"
        },
        {
          "time_str": "3",
          "val": "7"
        },
        {
          "time_str": "4",
          "val": "11"
        },
        {
          "time_str": "5",
          "val": "13"
        },
        {
          "time_str": "6",
          "val": "14"
        },
        {
          "time_str": "7",
          "val": "17"
        },
        {
          "time_str": "8",
          "val": "17"
        },
        {
          "time_str": "9",
          "val": "19"
        },
        {
          "time_str": "10",
          "val": "21"
        },
        {
          "time_str": "11",
          "val": "21"
        },
        {
          "time_str": "12",
          "val": "23"
        },
        {
          "time

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'attacks': {'away': [{'time_str': '0', 'val': '3'}, {'time_str': '1', 'val': '4'}, {'time_str': '2'`
  Nested fields:
  - **attacks** (object)
    Attacks
    Example: `{'away': [{'time_str': '0', 'val': '3'}, {'time_str': '1', 'val': '4'}, {'time_str': '2', 'val': '6'`
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '0', 'val': '3'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `0`
      - **val** (string)
        Val
        Example: `3`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '1', 'val': '2'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `1`
      - **val** (string)
        Val
        Example: `2`
  - **dangerous_attacks** (object)
    Dangerous Attacks
    Example: `{'away': [{'time_str': '0', 'val': '2'}, {'time_str': '1', 'val': '3'}, {'time_str': '2', 'val': '3'`
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '0', 'val': '2'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `0`
      - **val** (string)
        Val
        Example: `2`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '2', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `2`
      - **val** (string)
        Val
        Example: `1`
  - **possession** (object)
    Possession
    Example: `{'away': [{'time_str': '0', 'val': '100'}, {'time_str': '1', 'val': '73'}, {'time_str': '2', 'val': `
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '0', 'val': '100'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `0`
      - **val** (string)
        Val
        Example: `100`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '1', 'val': '27'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `1`
      - **val** (string)
        Val
        Example: `27`
  - **off_target** (object)
    Off Target
    Example: `{'away': [{'time_str': '1', 'val': '1'}, {'time_str': '2', 'val': '1'}, {'time_str': '3', 'val': '1'`
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '1', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `1`
      - **val** (string)
        Val
        Example: `1`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '24', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `24`
      - **val** (string)
        Val
        Example: `1`
  - **on_target** (object)
    On Target
    Example: `{'home': [{'time_str': '6', 'val': '1'}, {'time_str': '7', 'val': '1'}, {'time_str': '8', 'val': '1'`
    Nested fields:
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '6', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `6`
      - **val** (string)
        Val
        Example: `1`
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '10', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `10`
      - **val** (string)
        Val
        Example: `1`
  - **corners** (object)
    Corners
    Example: `{'away': [{'time_str': '23', 'val': '1'}, {'time_str': '33', 'val': '2'}, {'time_str': '46', 'val': `
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '23', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `23`
      - **val** (string)
        Val
        Example: `1`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '26', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `26`
      - **val** (string)
        Val
        Example: `1`
  - **goals** (object)
    Goals
    Example: `{'away': [{'time_str': '37', 'val': '1'}, {'time_str': '43', 'val': '2'}, {'time_str': '62', 'val': `
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '37', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `37`
      - **val** (string)
        Val
        Example: `1`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '47', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `47`
      - **val** (string)
        Val
        Example: `1`
  - **yellowcards** (object)
    Yellowcards
    Example: `{'away': [{'time_str': '40', 'val': '1'}, {'time_str': '55', 'val': '2'}], 'home': [{'time_str': '53`
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '40', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `40`
      - **val** (string)
        Val
        Example: `1`
    - **home** (array[object])
      Home team information
      Example: `{'time_str': '53', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `53`
      - **val** (string)
        Val
        Example: `1`
  - **redcards** (object)
    Redcards
    Example: `{'away': [{'time_str': '67', 'val': '1'}]}`
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '67', 'val': '1'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `67`
      - **val** (string)
        Val
        Example: `1`
  - **substitutions** (object)
    Substitutions
    Example: `{'away': [{'time_str': '67', 'val': '2'}, {'time_str': '77', 'val': '3'}, {'time_str': '78', 'val': `
    Nested fields:
    - **away** (array[object])
      Away team information
      Example: `{'time_str': '67', 'val': '2'}`
      Nested fields:
      - **time_str** (string)
        Time Str
        Example: `67`
      - **val** (string)
        Val
        Example: `2`

---

## Search

Search data

### Structure

```json

{
  "success": 1,
  "results": [
    {
      "id": "222577",
      "time": "1489672775",
      "time_status": "1",
      "league": {
        "id": "363",
        "name": "Europe Friendlies",
        "cc": "eu"
      },
      "home": {
        "id": "9844",
        "name": "Aalesund",
        "image_id": "677",
        "cc": "no"
      },
      "away": {
        "id": "1154",
        "name": "Odd BK",
        "image_id": "659",
        "cc": "no"
      },
      "timer": {
        "tm": 45,
        "ts": 0,
        "tt": "0"
      },
      "scores": {
        "2": {
          "home": "0",
          "away": "2"
        }
      }
    }
  ]
}

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (array[object])
  Results
  Example: `{'id': '222577', 'time': '1489672775', 'time_status': '1', 'league': {'id': '363', 'name': 'Europe F`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `222577`
  - **time** (string)
    Unix timestamp
    Example: `1489672775`
  - **time_status** (string)
    Status of the event (0=not started, 1=in play, 3=ended)
    Example: `1`
  - **league** (object)
    League information
    Example: `{'id': '363', 'name': 'Europe Friendlies', 'cc': 'eu'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `363`
    - **name** (string)
      Display name
      Example: `Europe Friendlies`
    - **cc** (string)
      Country code
      Example: `eu`
  - **home** (object)
    Home team information
    Example: `{'id': '9844', 'name': 'Aalesund', 'image_id': '677', 'cc': 'no'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `9844`
    - **name** (string)
      Display name
      Example: `Aalesund`
    - **image_id** (string)
      ID of the team/player image
      Example: `677`
    - **cc** (string)
      Country code
      Example: `no`
  - **away** (object)
    Away team information
    Example: `{'id': '1154', 'name': 'Odd BK', 'image_id': '659', 'cc': 'no'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `1154`
    - **name** (string)
      Display name
      Example: `Odd BK`
    - **image_id** (string)
      ID of the team/player image
      Example: `659`
    - **cc** (string)
      Country code
      Example: `no`
  - **timer** (object)
    Match timer information
    Example: `{'tm': 45, 'ts': 0, 'tt': '0'}`
    Nested fields:
    - **tm** (integer)
      Tm
      Example: `45`
    - **ts** (integer)
      Ts
      Example: `0`
    - **tt** (string)
      Tt
      Example: `0`
  - **scores** (object)
    Detailed scores by period
    Example: `{'2': {'home': '0', 'away': '2'}}`
    Nested fields:
    - **2** (object)
      2
      Example: `{'home': '0', 'away': '2'}`
      Nested fields:
      - **home** (string)
        Home team information
        Example: `0`
      - **away** (string)
        Away team information
        Example: `2`

---

## Event Odds

Betting odds information for an event

### Structure

```json

{
  "success": 1,
  "results": {
    "stats": {
      "matching_dir": 1,
      "odds_update": {
        "1_1": 1546802176,
        "1_2": 1546802220,
        "1_3": 1546802220,
        "1_4": 1546802102,
        "1_5": 1546798316,
        "1_6": 1546798316,
        "1_7": 1546798316,
        "1_8": 1546798375
      }
    },
    "odds": {
      "1_1": [
        {
          "id": "28948880",
          "home_od": "401.000",
          "draw_od": "51.000",
          "away_od": "1.002",
          "ss": "0-2",
          "time_str": "89",
          "add_time": "1546802147"
        },
        {
          "id": "28948859",
          "home_od": "351.000",
          "draw_od": "51.000",
          "away_od": "1.002",
          "ss": "0-2",
          "time_str": "88",
          "add_time": "1546802110"
        },
        {
          "id": "28948826",
          "home_od": "301.000",
          "draw_od": "41.000",
          "away_od": "1.004",
          "ss": "0-2",
          "time_str": "87",
       

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'stats': {'matching_dir': 1, 'odds_update': {'1_1': 1546802176, '1_2': 1546802220, '1_3': 154680222`
  Nested fields:
  - **stats** (object)
    Match statistics
    Example: `{'matching_dir': 1, 'odds_update': {'1_1': 1546802176, '1_2': 1546802220, '1_3': 1546802220, '1_4': `
    Nested fields:
    - **matching_dir** (integer)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546802176, '1_2': 1546802220, '1_3': 1546802220, '1_4': 1546802102, '1_5': 1546798316, '1_6`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546802176`
      - **1_2** (integer)
        1 2
        Example: `1546802220`
      - **1_3** (integer)
        1 3
        Example: `1546802220`
      - **1_4** (integer)
        1 4
        Example: `1546802102`
      - **1_5** (integer)
        1 5
        Example: `1546798316`
      - **1_6** (integer)
        1 6
        Example: `1546798316`
      - **1_7** (integer)
        1 7
        Example: `1546798316`
      - **1_8** (integer)
        1 8
        Example: `1546798375`
  - **odds** (object)
    Odds
    Example: `{'1_1': [{'id': '28948880', 'home_od': '401.000', 'draw_od': '51.000', 'away_od': '1.002', 'ss': '0-`
    Nested fields:
    - **1_1** (array[object])
      1 1
      Example: `{'id': '28948880', 'home_od': '401.000', 'draw_od': '51.000', 'away_od': '1.002', 'ss': '0-2', 'time`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `28948880`
      - **home_od** (string)
        Home Od
        Example: `401.000`
      - **draw_od** (string)
        Draw Od
        Example: `51.000`
      - **away_od** (string)
        Away Od
        Example: `1.002`
      - **ss** (string)
        Current score
        Example: `0-2`
      - **time_str** (string)
        Time Str
        Example: `89`
      - **add_time** (string)
        Add Time
        Example: `1546802147`
    - **1_2** (array[object])
      1 2
      Example: `{'id': '28439955', 'home_od': '1.850', 'handicap': '0.0', 'away_od': '2.050', 'ss': '0-2', 'time_str`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `28439955`
      - **home_od** (string)
        Home Od
        Example: `1.850`
      - **handicap** (string)
        Handicap
        Example: `0.0`
      - **away_od** (string)
        Away Od
        Example: `2.050`
      - **ss** (string)
        Current score
        Example: `0-2`
      - **time_str** (string)
        Time Str
        Example: `89`
      - **add_time** (string)
        Add Time
        Example: `1546802177`
    - **1_3** (array[object])
      1 3
      Example: `{'id': '50385504', 'over_od': '6.150', 'handicap': '2.5', 'under_od': '1.135', 'ss': '0-2', 'time_st`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `50385504`
      - **over_od** (string)
        Over Od
        Example: `6.150`
      - **handicap** (string)
        Handicap
        Example: `2.5`
      - **under_od** (string)
        Under Od
        Example: `1.135`
      - **ss** (string)
        Current score
        Example: `0-2`
      - **time_str** (string)
        Time Str
        Example: `90`
      - **add_time** (string)
        Add Time
        Example: `1546802216`
    - **1_4** (array[object])
      1 4
      Example: `{'id': '28989960', 'over_od': '1.950', 'handicap': '14.5', 'under_od': '1.850', 'ss': '0-2', 'time_s`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `28989960`
      - **over_od** (string)
        Over Od
        Example: `1.950`
      - **handicap** (string)
        Handicap
        Example: `14.5`
      - **under_od** (string)
        Under Od
        Example: `1.850`
      - **ss** (string)
        Current score
        Example: `0-2`
      - **time_str** (string)
        Time Str
        Example: `88`
      - **add_time** (string)
        Add Time
        Example: `1546802099`
    - **1_5** (array[object])
      1 5
      Example: `{'id': '6760702', 'home_od': '3.650', 'handicap': '0.0,-0.5', 'away_od': '1.275', 'ss': '0-1', 'time`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `6760702`
      - **home_od** (string)
        Home Od
        Example: `3.650`
      - **handicap** (string)
        Handicap
        Example: `0.0,-0.5`
      - **away_od** (string)
        Away Od
        Example: `1.275`
      - **ss** (string)
        Current score
        Example: `0-1`
      - **time_str** (string)
        Time Str
        Example: `40`
      - **add_time** (string)
        Add Time
        Example: `1546798306`
    - **1_6** (array[object])
      1 6
      Example: `{'id': '13435943', 'over_od': '5.100', 'handicap': '1.5', 'under_od': '1.170', 'ss': '0-1', 'time_st`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `13435943`
      - **over_od** (string)
        Over Od
        Example: `5.100`
      - **handicap** (string)
        Handicap
        Example: `1.5`
      - **under_od** (string)
        Under Od
        Example: `1.170`
      - **ss** (string)
        Current score
        Example: `0-1`
      - **time_str** (string)
        Time Str
        Example: `40`
      - **add_time** (string)
        Add Time
        Example: `1546798315`
    - **1_7** (array[object])
      1 7
      Example: `{'id': '9094597', 'over_od': '1.875', 'handicap': '10.5', 'under_od': '1.925', 'ss': '0-1', 'time_st`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `9094597`
      - **over_od** (string)
        Over Od
        Example: `1.875`
      - **handicap** (string)
        Handicap
        Example: `10.5`
      - **under_od** (string)
        Under Od
        Example: `1.925`
      - **ss** (string)
        Current score
        Example: `0-1`
      - **time_str** (string)
        Time Str
        Example: `40`
      - **add_time** (string)
        Add Time
        Example: `1546798315`
    - **1_8** (array[object])
      1 8
      Example: `{'id': '9488263', 'home_od': '126.000', 'draw_od': '7.000', 'away_od': '1.100', 'ss': '0-1', 'time_s`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `9488263`
      - **home_od** (string)
        Home Od
        Example: `126.000`
      - **draw_od** (string)
        Draw Od
        Example: `7.000`
      - **away_od** (string)
        Away Od
        Example: `1.100`
      - **ss** (string)
        Current score
        Example: `0-1`
      - **time_str** (string)
        Time Str
        Example: `41`
      - **add_time** (string)
        Add Time
        Example: `1546798362`

---

## League Table

League Table data

### Structure

```json

{
  "success": 1,
  "results": [
    {
      "season": {
        "sport_id": "1",
        "start_time": "1659657600",
        "end_time": "1685318399",
        "has_topgoals": "1",
        "has_leaguetable": "1",
        "has_lineups": "1",
        "name": "Premier League 22/23"
      },
      "overall": {
        "tables": [
          {
            "name": "Premier League",
            "groupname": null,
            "currentround": "31",
            "maxrounds": "38",
            "rows": [
              {
                "pos": "1",
                "sort_pos": "1",
                "change": "0",
                "win": "23",
                "draw": "5",
                "loss": "3",
                "goalsfor": "74",
                "goalsagainst": "31",
                "points": "74",
                "pct": null,
                "goalDiffTotal": 43,
                "promotion": {
                  "name": "Champions League",
                  "shortname": "CL"
                },
       

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (array[object])
  Results
  Example: `{'season': {'sport_id': '1', 'start_time': '1659657600', 'end_time': '1685318399', 'has_topgoals': '`
  Nested fields:
  - **season** (object)
    Season
    Example: `{'sport_id': '1', 'start_time': '1659657600', 'end_time': '1685318399', 'has_topgoals': '1', 'has_le`
    Nested fields:
    - **sport_id** (string)
      Sport identifier
      Example: `1`
    - **start_time** (string)
      Start Time
      Example: `1659657600`
    - **end_time** (string)
      End Time
      Example: `1685318399`
    - **has_topgoals** (string)
      Has Topgoals
      Example: `1`
    - **has_leaguetable** (string)
      Has Leaguetable
      Example: `1`
    - **has_lineups** (string)
      Has Lineups
      Example: `1`
    - **name** (string)
      Display name
      Example: `Premier League 22/23`
  - **overall** (object)
    Overall
    Example: `{'tables': [{'name': 'Premier League', 'groupname': None, 'currentround': '31', 'maxrounds': '38', '`
    Nested fields:
    - **tables** (array[object])
      Tables
      Example: `{'name': 'Premier League', 'groupname': None, 'currentround': '31', 'maxrounds': '38', 'rows': [{'po`
      Nested fields:
      - **name** (string)
        Display name
        Example: `Premier League`
      - **groupname** (unknown)
        Groupname
      - **currentround** (string)
        Currentround
        Example: `31`
      - **maxrounds** (string)
        Maxrounds
        Example: `38`
      - **rows** (array[object])
        Rows
        Example: `{'pos': '1', 'sort_pos': '1', 'change': '0', 'win': '23', 'draw': '5', 'loss': '3', 'goalsfor': '74'`
        Nested fields:
        - **pos** (string)
          Pos
          Example: `1`
        - **sort_pos** (string)
          Sort Pos
          Example: `1`
        - **change** (string)
          Change
          Example: `0`
        - **win** (string)
          Win
          Example: `23`
        - **draw** (string)
          Draw
          Example: `5`
        - **loss** (string)
          Loss
          Example: `3`
        - **goalsfor** (string)
          Goalsfor
          Example: `74`
        - **goalsagainst** (string)
          Goalsagainst
          Example: `31`
        - **points** (string)
          Points
          Example: `74`
        - **pct** (unknown)
          Pct
        - **goalDiffTotal** (integer)
          Goaldifftotal
          Example: `43`
        - **promotion** (object)
          Promotion
          Example: `{'name': 'Champions League', 'shortname': 'CL'}`
          Nested fields:
          - **name** (string)
            Display name
            Example: `Champions League`
          - **shortname** (string)
            Shortname
            Example: `CL`
        - **team** (object)
          Team
          Example: `{'id': '17230', 'name': 'Arsenal', 'image_id': '42', 'cc': 'gb'}`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `17230`
          - **name** (string)
            Display name
            Example: `Arsenal`
          - **image_id** (string)
            ID of the team/player image
            Example: `42`
          - **cc** (string)
            Country code
            Example: `gb`
  - **home** (object)
    Home team information
    Example: `{'tables': [{'name': 'Premier League', 'groupname': None, 'currentround': '31', 'maxrounds': '38', '`
    Nested fields:
    - **tables** (array[object])
      Tables
      Example: `{'name': 'Premier League', 'groupname': None, 'currentround': '31', 'maxrounds': '38', 'rows': [{'po`
      Nested fields:
      - **name** (string)
        Display name
        Example: `Premier League`
      - **groupname** (unknown)
        Groupname
      - **currentround** (string)
        Currentround
        Example: `31`
      - **maxrounds** (string)
        Maxrounds
        Example: `38`
      - **rows** (array[object])
        Rows
        Example: `{'pos': '1', 'sort_pos': '1', 'change': '1', 'win': '13', 'draw': '1', 'loss': '1', 'goalsfor': '50'`
        Nested fields:
        - **pos** (string)
          Pos
          Example: `1`
        - **sort_pos** (string)
          Sort Pos
          Example: `1`
        - **change** (string)
          Change
          Example: `1`
        - **win** (string)
          Win
          Example: `13`
        - **draw** (string)
          Draw
          Example: `1`
        - **loss** (string)
          Loss
          Example: `1`
        - **goalsfor** (string)
          Goalsfor
          Example: `50`
        - **goalsagainst** (string)
          Goalsagainst
          Example: `15`
        - **points** (string)
          Points
          Example: `40`
        - **pct** (unknown)
          Pct
        - **extra** (unknown)
          Extra
        - **promotion** (object)
          Promotion
          Example: `{'name': 'Champions League', 'shortname': 'CL'}`
          Nested fields:
          - **name** (string)
            Display name
            Example: `Champions League`
          - **shortname** (string)
            Shortname
            Example: `CL`
        - **team** (object)
          Team
          Example: `{'id': '708', 'name': 'Man City', 'image_id': '17', 'cc': 'gb'}`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `708`
          - **name** (string)
            Display name
            Example: `Man City`
          - **image_id** (string)
            ID of the team/player image
            Example: `17`
          - **cc** (string)
            Country code
            Example: `gb`
  - **away** (object)
    Away team information
    Example: `{'tables': [{'name': 'Premier League', 'groupname': None, 'currentround': '31', 'maxrounds': '38', '`
    Nested fields:
    - **tables** (array[object])
      Tables
      Example: `{'name': 'Premier League', 'groupname': None, 'currentround': '31', 'maxrounds': '38', 'rows': [{'po`
      Nested fields:
      - **name** (string)
        Display name
        Example: `Premier League`
      - **groupname** (unknown)
        Groupname
      - **currentround** (string)
        Currentround
        Example: `31`
      - **maxrounds** (string)
        Maxrounds
        Example: `38`
      - **rows** (array[object])
        Rows
        Example: `{'pos': '1', 'sort_pos': '1', 'change': '0', 'win': '11', 'draw': '3', 'loss': '2', 'goalsfor': '32'`
        Nested fields:
        - **pos** (string)
          Pos
          Example: `1`
        - **sort_pos** (string)
          Sort Pos
          Example: `1`
        - **change** (string)
          Change
          Example: `0`
        - **win** (string)
          Win
          Example: `11`
        - **draw** (string)
          Draw
          Example: `3`
        - **loss** (string)
          Loss
          Example: `2`
        - **goalsfor** (string)
          Goalsfor
          Example: `32`
        - **goalsagainst** (string)
          Goalsagainst
          Example: `13`
        - **points** (string)
          Points
          Example: `36`
        - **pct** (unknown)
          Pct
        - **extra** (unknown)
          Extra
        - **promotion** (object)
          Promotion
          Example: `{'name': 'Champions League', 'shortname': 'CL'}`
          Nested fields:
          - **name** (string)
            Display name
            Example: `Champions League`
          - **shortname** (string)
            Shortname
            Example: `CL`
        - **team** (object)
          Team
          Example: `{'id': '17230', 'name': 'Arsenal', 'image_id': '42', 'cc': 'gb'}`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `17230`
          - **name** (string)
            Display name
            Example: `Arsenal`
          - **image_id** (string)
            ID of the team/player image
            Example: `42`
          - **cc** (string)
            Country code
            Example: `gb`

---

## League Toplist

League Toplist data

### Structure

```json

{
  "success": 1,
  "results": {
    "topgoals": [
      {
        "goal_points": "37",
        "goals": "28",
        "penalties": "1",
        "matches": "30",
        "minutes_played": "2393",
        "substituted_in": "2",
        "player": {
          "id": "159665",
          "name": "Mohamed Salah",
          "cc": "eg"
        },
        "team": {
          "id": "23451",
          "name": "Liverpool",
          "image_id": "44",
          "cc": "gb"
        }
      },
      {
        "goal_points": "26",
        "goals": "24",
        "penalties": "2",
        "matches": "29",
        "minutes_played": "2442",
        "substituted_in": "1",
        "player": {
          "id": "108579",
          "name": "Harry Kane",
          "cc": "gb"
        },
        "team": {
          "id": "17212",
          "name": "Tottenham",
          "image_id": "33",
          "cc": "gb"
        }
      },
      {
        "goal_points": "27",
        "goals": "21",
        "penalties": "4",
    

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'topgoals': [{'goal_points': '37', 'goals': '28', 'penalties': '1', 'matches': '30', 'minutes_playe`
  Nested fields:
  - **topgoals** (array[object])
    Topgoals
    Example: `{'goal_points': '37', 'goals': '28', 'penalties': '1', 'matches': '30', 'minutes_played': '2393', 's`
    Nested fields:
    - **goal_points** (string)
      Goal Points
      Example: `37`
    - **goals** (string)
      Goals
      Example: `28`
    - **penalties** (string)
      Penalties
      Example: `1`
    - **matches** (string)
      Matches
      Example: `30`
    - **minutes_played** (string)
      Minutes Played
      Example: `2393`
    - **substituted_in** (string)
      Substituted In
      Example: `2`
    - **player** (object)
      Player
      Example: `{'id': '159665', 'name': 'Mohamed Salah', 'cc': 'eg'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `159665`
      - **name** (string)
        Display name
        Example: `Mohamed Salah`
      - **cc** (string)
        Country code
        Example: `eg`
    - **team** (object)
      Team
      Example: `{'id': '23451', 'name': 'Liverpool', 'image_id': '44', 'cc': 'gb'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `23451`
      - **name** (string)
        Display name
        Example: `Liverpool`
      - **image_id** (string)
        ID of the team/player image
        Example: `44`
      - **cc** (string)
        Country code
        Example: `gb`
  - **topassists** (array[object])
    Topassists
    Example: `{'assists': '14', 'matches': '30', 'player': {'id': '70996', 'name': 'Kevin De Bruyne', 'cc': 'be'},`
    Nested fields:
    - **assists** (string)
      Assists
      Example: `14`
    - **matches** (string)
      Matches
      Example: `30`
    - **player** (object)
      Player
      Example: `{'id': '70996', 'name': 'Kevin De Bruyne', 'cc': 'be'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `70996`
      - **name** (string)
        Display name
        Example: `Kevin De Bruyne`
      - **cc** (string)
        Country code
        Example: `be`
    - **team** (object)
      Team
      Example: `{'id': '708', 'name': 'Man City', 'image_id': '17', 'cc': 'gb'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `708`
      - **name** (string)
        Display name
        Example: `Man City`
      - **image_id** (string)
        ID of the team/player image
        Example: `17`
      - **cc** (string)
        Country code
        Example: `gb`
  - **topcards** (array[object])
    Topcards
    Example: `{'matches': '22', 'minutes_played': '1555', 'red_cards': '1', 'yellowred_cards': '1', 'yellow_cards'`
    Nested fields:
    - **matches** (string)
      Matches
      Example: `22`
    - **minutes_played** (string)
      Minutes Played
      Example: `1555`
    - **red_cards** (string)
      Red Cards
      Example: `1`
    - **yellowred_cards** (string)
      Yellowred Cards
      Example: `1`
    - **yellow_cards** (string)
      Yellow Cards
      Example: `2`
    - **player** (object)
      Player
      Example: `{'id': '36465', 'name': 'Jonjo Shelvey', 'cc': 'gb'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `36465`
      - **name** (string)
        Display name
        Example: `Jonjo Shelvey`
      - **cc** (string)
        Country code
        Example: `gb`
    - **team** (object)
      Team
      Example: `{'id': '23478', 'name': 'Newcastle', 'image_id': '39', 'cc': 'gb'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `23478`
      - **name** (string)
        Display name
        Example: `Newcastle`
      - **image_id** (string)
        ID of the team/player image
        Example: `39`
      - **cc** (string)
        Country code
        Example: `gb`
  - **injuries** (array[object])
    Injuries
    Example: `{'missing': '1', 'status_id': '1', 'start': '1519945200', 'end': '0', 'doubtful': '0', 'comment': ''`
    Nested fields:
    - **missing** (string)
      Missing
      Example: `1`
    - **status_id** (string)
      Status Id
      Example: `1`
    - **start** (string)
      Start
      Example: `1519945200`
    - **end** (string)
      End
      Example: `0`
    - **doubtful** (string)
      Doubtful
      Example: `0`
    - **comment** (string)
      Comment
      Example: ``
    - **player** (object)
      Player
      Example: `{'id': '17651', 'name': 'Santi Cazorla', 'cc': 'es'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `17651`
      - **name** (string)
        Display name
        Example: `Santi Cazorla`
      - **cc** (string)
        Country code
        Example: `es`
    - **team** (object)
      Team
      Example: `{'id': '17230', 'name': 'Arsenal', 'image_id': '42', 'cc': 'gb'}`
      Nested fields:
      - **id** (string)
        Unique identifier
        Example: `17230`
      - **name** (string)
        Display name
        Example: `Arsenal`
      - **image_id** (string)
        ID of the team/player image
        Example: `42`
      - **cc** (string)
        Country code
        Example: `gb`

---

## Upcoming

Upcoming matches with scheduling information

### Structure

```json

{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 50,
    "total": 47764
  },
  "results": [
    {
      "id": "3915866",
      "sport_id": "1",
      "time": "1633184100",
      "time_status": "0",
      "league": {
        "id": "521",
        "name": "Belgium Super League Women",
        "cc": "be"
      },
      "home": {
        "id": "240427",
        "name": "Club Brugge Women",
        "image_id": "178250",
        "cc": "be"
      },
      "away": {
        "id": "8496",
        "name": "Genk Women",
        "image_id": "218146",
        "cc": "be"
      },
      "ss": null
    },
    {
      "id": "3305136",
      "sport_id": "1",
      "time": "1633185000",
      "time_status": "0",
      "league": {
        "id": "593",
        "name": "Sweden 2.div Norra Svealand",
        "cc": "se"
      },
      "home": {
        "id": "60607",
        "name": "Enkopings SK",
        "image_id": "1780",
        "cc": "se"
      },
      "away": {
        "id": "46782",
     

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **pager** (object)
  Pager
  Example: `{'page': 1, 'per_page': 50, 'total': 47764}`
  Nested fields:
  - **page** (integer)
    Page
    Example: `1`
  - **per_page** (integer)
    Per Page
    Example: `50`
  - **total** (integer)
    Total
    Example: `47764`
- **results** (array[object])
  Results
  Example: `{'id': '3915866', 'sport_id': '1', 'time': '1633184100', 'time_status': '0', 'league': {'id': '521',`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `3915866`
  - **sport_id** (string)
    Sport identifier
    Example: `1`
  - **time** (string)
    Unix timestamp
    Example: `1633184100`
  - **time_status** (string)
    Status of the event (0=not started, 1=in play, 3=ended)
    Example: `0`
  - **league** (object)
    League information
    Example: `{'id': '521', 'name': 'Belgium Super League Women', 'cc': 'be'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `521`
    - **name** (string)
      Display name
      Example: `Belgium Super League Women`
    - **cc** (string)
      Country code
      Example: `be`
  - **home** (object)
    Home team information
    Example: `{'id': '240427', 'name': 'Club Brugge Women', 'image_id': '178250', 'cc': 'be'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `240427`
    - **name** (string)
      Display name
      Example: `Club Brugge Women`
    - **image_id** (string)
      ID of the team/player image
      Example: `178250`
    - **cc** (string)
      Country code
      Example: `be`
  - **away** (object)
    Away team information
    Example: `{'id': '8496', 'name': 'Genk Women', 'image_id': '218146', 'cc': 'be'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `8496`
    - **name** (string)
      Display name
      Example: `Genk Women`
    - **image_id** (string)
      ID of the team/player image
      Example: `218146`
    - **cc** (string)
      Country code
      Example: `be`
  - **ss** (unknown)
    Current score

---

## Inplay

Live in-play match information including scores and statistics

### Structure

```json

{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 1000,
    "total": 267
  },
  "results": [
    {
      "id": "4140581",
      "sport_id": "1",
      "time": "1633179600",
      "time_status": "1",
      "league": {
        "id": "825",
        "name": "Tunisia League 1",
        "cc": "tn"
      },
      "home": {
        "id": "47374",
        "name": "JS Kairouanaise",
        "image_id": "59632",
        "cc": "tn"
      },
      "away": {
        "id": "71185",
        "name": "Club Olympique Medenine",
        "image_id": "294214",
        "cc": "tn"
      },
      "ss": "1-1",
      "scores": {
        "2": {
          "home": "1",
          "away": "1"
        },
        "1": {
          "home": "1",
          "away": "1"
        }
      },
      "stats": {
        "attacks": [
          "45",
          "41"
        ],
        "corners": [
          "2",
          "2"
        ],
        "corner_h": [
          "2",
          "2"
        ],
        "dangerous_attack

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **pager** (object)
  Pager
  Example: `{'page': 1, 'per_page': 1000, 'total': 267}`
  Nested fields:
  - **page** (integer)
    Page
    Example: `1`
  - **per_page** (integer)
    Per Page
    Example: `1000`
  - **total** (integer)
    Total
    Example: `267`
- **results** (array[object])
  Results
  Example: `{'id': '4140581', 'sport_id': '1', 'time': '1633179600', 'time_status': '1', 'league': {'id': '825',`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `4140581`
  - **sport_id** (string)
    Sport identifier
    Example: `1`
  - **time** (string)
    Unix timestamp
    Example: `1633179600`
  - **time_status** (string)
    Status of the event (0=not started, 1=in play, 3=ended)
    Example: `1`
  - **league** (object)
    League information
    Example: `{'id': '825', 'name': 'Tunisia League 1', 'cc': 'tn'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `825`
    - **name** (string)
      Display name
      Example: `Tunisia League 1`
    - **cc** (string)
      Country code
      Example: `tn`
  - **home** (object)
    Home team information
    Example: `{'id': '47374', 'name': 'JS Kairouanaise', 'image_id': '59632', 'cc': 'tn'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `47374`
    - **name** (string)
      Display name
      Example: `JS Kairouanaise`
    - **image_id** (string)
      ID of the team/player image
      Example: `59632`
    - **cc** (string)
      Country code
      Example: `tn`
  - **away** (object)
    Away team information
    Example: `{'id': '71185', 'name': 'Club Olympique Medenine', 'image_id': '294214', 'cc': 'tn'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `71185`
    - **name** (string)
      Display name
      Example: `Club Olympique Medenine`
    - **image_id** (string)
      ID of the team/player image
      Example: `294214`
    - **cc** (string)
      Country code
      Example: `tn`
  - **ss** (string)
    Current score
    Example: `1-1`
  - **scores** (object)
    Detailed scores by period
    Example: `{'2': {'home': '1', 'away': '1'}, '1': {'home': '1', 'away': '1'}}`
    Nested fields:
    - **2** (object)
      2
      Example: `{'home': '1', 'away': '1'}`
      Nested fields:
      - **home** (string)
        Home team information
        Example: `1`
      - **away** (string)
        Away team information
        Example: `1`
    - **1** (object)
      1
      Example: `{'home': '1', 'away': '1'}`
      Nested fields:
      - **home** (string)
        Home team information
        Example: `1`
      - **away** (string)
        Away team information
        Example: `1`
  - **stats** (object)
    Match statistics
    Example: `{'attacks': ['45', '41'], 'corners': ['2', '2'], 'corner_h': ['2', '2'], 'dangerous_attacks': ['28',`
    Nested fields:
    - **attacks** (array[string])
      Attacks
      Example: `['45', '41']`
    - **corners** (array[string])
      Corners
      Example: `['2', '2']`
    - **corner_h** (array[string])
      Corner H
      Example: `['2', '2']`
    - **dangerous_attacks** (array[string])
      Dangerous Attacks
      Example: `['28', '20']`
    - **goals** (array[string])
      Goals
      Example: `['1', '1']`
    - **off_target** (array[string])
      Off Target
      Example: `['5', '3']`
    - **on_target** (array[string])
      On Target
      Example: `['3', '2']`
    - **penalties** (array[string])
      Penalties
      Example: `['0', '0']`
    - **possession_rt** (array[string])
      Possession Rt
      Example: `['47', '53']`
    - **redcards** (array[string])
      Redcards
      Example: `['0', '0']`
    - **substitutions** (array[string])
      Substitutions
      Example: `['1', '3']`
    - **yellowcards** (array[string])
      Yellowcards
      Example: `['2', '1']`
  - **bet365_id** (string)
    Bet365 Id
    Example: `108742033`
  - **timer** (object)
    Match timer information
    Example: `{'tm': 54, 'ts': 14, 'tt': '1', 'ta': 0, 'md': 1}`
    Nested fields:
    - **tm** (integer)
      Tm
      Example: `54`
    - **ts** (integer)
      Ts
      Example: `14`
    - **tt** (string)
      Tt
      Example: `1`
    - **ta** (integer)
      Ta
      Example: `0`
    - **md** (integer)
      Md
      Example: `1`

---

## Team Members

Team Members data

### Structure

```json

{
  "success": 1,
  "results": [
    {
      "id": "189876",
      "name": "Joao Lucas Reis da Silva",
      "image_id": 0,
      "cc": "br"
    },
    {
      "id": "189740",
      "name": "Matheus P De Almeida",
      "image_id": 0,
      "cc": "br"
    }
  ]
}

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (array[object])
  Results
  Example: `{'id': '189876', 'name': 'Joao Lucas Reis da Silva', 'image_id': 0, 'cc': 'br'}`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `189876`
  - **name** (string)
    Display name
    Example: `Joao Lucas Reis da Silva`
  - **image_id** (integer)
    ID of the team/player image
    Example: `0`
  - **cc** (string)
    Country code
    Example: `br`

---

## Event Odds Summary

Event Odds Summary data

### Structure

```json

{
  "success": 1,
  "results": {
    "Bet365": {
      "matching_dir": 1,
      "odds_update": {
        "1_1": 1546938229,
        "1_2": 1546938229,
        "1_3": 1546938229,
        "1_4": 1546938229,
        "1_5": 1546938229,
        "1_6": 1546938229,
        "1_7": 1546938229,
        "1_8": 1546938229
      },
      "odds": {
        "start": {
          "1_1": {
            "id": "28952207",
            "home_od": "2.050",
            "draw_od": "3.500",
            "away_od": "3.400",
            "ss": null,
            "time_str": null,
            "add_time": "1546807911"
          },
          "1_2": {
            "id": "28442802",
            "home_od": "2.069",
            "handicap": "-0.50",
            "away_od": "1.830",
            "ss": null,
            "time_str": null,
            "add_time": "1546807897"
          },
          "1_3": {
            "id": "50390513",
            "over_od": "1.660",
            "handicap": "2.5",
            "under_od": "2.200",


... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'Bet365': {'matching_dir': 1, 'odds_update': {'1_1': 1546938229, '1_2': 1546938229, '1_3': 15469382`
  Nested fields:
  - **Bet365** (object)
    Bet365
    Example: `{'matching_dir': 1, 'odds_update': {'1_1': 1546938229, '1_2': 1546938229, '1_3': 1546938229, '1_4': `
    Nested fields:
    - **matching_dir** (integer)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938229, '1_2': 1546938229, '1_3': 1546938229, '1_4': 1546938229, '1_5': 1546938229, '1_6`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938229`
      - **1_2** (integer)
        1 2
        Example: `1546938229`
      - **1_3** (integer)
        1 3
        Example: `1546938229`
      - **1_4** (integer)
        1 4
        Example: `1546938229`
      - **1_5** (integer)
        1 5
        Example: `1546938229`
      - **1_6** (integer)
        1 6
        Example: `1546938229`
      - **1_7** (integer)
        1 7
        Example: `1546938229`
      - **1_8** (integer)
        1 8
        Example: `1546938229`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '28952207', 'home_od': '2.050', 'draw_od': '3.500', 'away_od': '3.400', 'ss`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '28952207', 'home_od': '2.050', 'draw_od': '3.500', 'away_od': '3.400', 'ss': None, '`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '28952207', 'home_od': '2.050', 'draw_od': '3.500', 'away_od': '3.400', 'ss': None, 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `28952207`
          - **home_od** (string)
            Home Od
            Example: `2.050`
          - **draw_od** (string)
            Draw Od
            Example: `3.500`
          - **away_od** (string)
            Away Od
            Example: `3.400`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546807911`
        - **1_2** (object)
          1 2
          Example: `{'id': '28442802', 'home_od': '2.069', 'handicap': '-0.50', 'away_od': '1.830', 'ss': None, 'time_st`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `28442802`
          - **home_od** (string)
            Home Od
            Example: `2.069`
          - **handicap** (string)
            Handicap
            Example: `-0.50`
          - **away_od** (string)
            Away Od
            Example: `1.830`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546807897`
        - **1_3** (object)
          1 3
          Example: `{'id': '50390513', 'over_od': '1.660', 'handicap': '2.5', 'under_od': '2.200', 'ss': None, 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `50390513`
          - **over_od** (string)
            Over Od
            Example: `1.660`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.200`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546807908`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '28975620', 'home_od': '2.050', 'draw_od': '3.750', 'away_od': '3.250', 'ss': '0-0', `
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '28975620', 'home_od': '2.050', 'draw_od': '3.750', 'away_od': '3.250', 'ss': '0-0', 'time_st`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `28975620`
          - **home_od** (string)
            Home Od
            Example: `2.050`
          - **draw_od** (string)
            Draw Od
            Example: `3.750`
          - **away_od** (string)
            Away Od
            Example: `3.250`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938229`
        - **1_2** (object)
          1 2
          Example: `{'id': '28469560', 'home_od': '2.050', 'handicap': '-0.5', 'away_od': '1.800', 'ss': '0-0', 'time_st`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `28469560`
          - **home_od** (string)
            Home Od
            Example: `2.050`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.800`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938229`
        - **1_3** (object)
          1 3
          Example: `{'id': '50429504', 'over_od': '1.925', 'handicap': '2.5,3.0', 'under_od': '1.925', 'ss': '0-0', 'tim`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `50429504`
          - **over_od** (string)
            Over Od
            Example: `1.925`
          - **handicap** (string)
            Handicap
            Example: `2.5,3.0`
          - **under_od** (string)
            Under Od
            Example: `1.925`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `5`
          - **add_time** (string)
            Add Time
            Example: `1546938087`
  - **10Bet** (object)
    10Bet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938224, '1_2': 1546938224, '1_3': 1546938224}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938224, '1_2': 1546938224, '1_3': 1546938224}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938224`
      - **1_2** (integer)
        1 2
        Example: `1546938224`
      - **1_3** (integer)
        1 3
        Example: `1546938224`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '46636626', 'home_od': '2.000', 'draw_od': '3.450', 'away_od': '3.450', 'ss`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '46636626', 'home_od': '2.000', 'draw_od': '3.450', 'away_od': '3.450', 'ss': None, '`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '46636626', 'home_od': '2.000', 'draw_od': '3.450', 'away_od': '3.450', 'ss': None, 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `46636626`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **draw_od** (string)
            Draw Od
            Example: `3.450`
          - **away_od** (string)
            Away Od
            Example: `3.450`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546684792`
        - **1_2** (object)
          1 2
          Example: `{'id': '49658768', 'home_od': '2.000', 'handicap': '-0.5', 'away_od': '1.763', 'ss': None, 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `49658768`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.763`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546684792`
        - **1_3** (object)
          1 3
          Example: `{'id': '52861813', 'over_od': '1.893', 'handicap': '2.75', 'under_od': '1.870', 'ss': None, 'time_st`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `52861813`
          - **over_od** (string)
            Over Od
            Example: `1.893`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.870`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546684792`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '46811659', 'home_od': '1.980', 'draw_od': '3.690', 'away_od': '3.350', 'ss': '0:0', `
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '46811659', 'home_od': '1.980', 'draw_od': '3.690', 'away_od': '3.350', 'ss': '0:0', 'time_st`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `46811659`
          - **home_od** (string)
            Home Od
            Example: `1.980`
          - **draw_od** (string)
            Draw Od
            Example: `3.690`
          - **away_od** (string)
            Away Od
            Example: `3.350`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `07:36`
          - **add_time** (string)
            Add Time
            Example: `1546938199`
        - **1_2** (object)
          1 2
          Example: `{'id': '49950427', 'home_od': '2.000', 'handicap': '-0.5', 'away_od': '1.813', 'ss': '0:0', 'time_st`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `49950427`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.813`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `07:23`
          - **add_time** (string)
            Add Time
            Example: `1546938181`
        - **1_3** (object)
          1 3
          Example: `{'id': '53216751', 'over_od': '1.901', 'handicap': '2.75', 'under_od': '1.901', 'ss': '0:0', 'time_s`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `53216751`
          - **over_od** (string)
            Over Od
            Example: `1.901`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.901`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `05:33`
          - **add_time** (string)
            Add Time
            Example: `1546938071`
  - **Ladbrokes** (object)
    Ladbrokes
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226, '1_3': 1546938226}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226, '1_3': 1546938226}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
      - **1_3** (integer)
        1 3
        Example: `1546938226`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '4820691', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.25', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '4820691', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.25', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '4820691', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.25', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4820691`
          - **home_od** (string)
            Home Od
            Example: `2.00`
          - **draw_od** (string)
            Draw Od
            Example: `3.40`
          - **away_od** (string)
            Away Od
            Example: `3.25`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546770894`
        - **1_2** (unknown)
          1 2
        - **1_3** (object)
          1 3
          Example: `{'id': '9436860', 'over_od': '1.66', 'handicap': '2.5', 'under_od': '2.15', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `9436860`
          - **over_od** (string)
            Over Od
            Example: `1.66`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.15`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546770894`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '4845976', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.25', 'ss': '0:0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '4845976', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.25', 'ss': '0:0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4845976`
          - **home_od** (string)
            Home Od
            Example: `2.00`
          - **draw_od** (string)
            Draw Od
            Example: `3.40`
          - **away_od** (string)
            Away Od
            Example: `3.25`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938199`
        - **1_2** (unknown)
          1 2
        - **1_3** (object)
          1 3
          Example: `{'id': '9465125', 'over_od': '1.70', 'handicap': '2.5', 'under_od': '2.10', 'ss': '0:0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `9465125`
          - **over_od** (string)
            Over Od
            Example: `1.70`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.10`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938226`
  - **YSB88** (object)
    Ysb88
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546937250, '1_2': 1546937242, '1_3': 1546937263}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546937250, '1_2': 1546937242, '1_3': 1546937263}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546937250`
      - **1_2** (integer)
        1 2
        Example: `1546937242`
      - **1_3** (integer)
        1 3
        Example: `1546937263`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_2': {'id': '1165074', 'home_od': '1.82', 'handicap': '0,-0.5', 'away_od': '2.13', 'ss'`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_2': {'id': '1165074', 'home_od': '1.82', 'handicap': '0,-0.5', 'away_od': '2.13', 'ss': None, 't`
        Nested fields:
        - **1_2** (object)
          1 2
          Example: `{'id': '1165074', 'home_od': '1.82', 'handicap': '0,-0.5', 'away_od': '2.13', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1165074`
          - **home_od** (string)
            Home Od
            Example: `1.82`
          - **handicap** (string)
            Handicap
            Example: `0,-0.5`
          - **away_od** (string)
            Away Od
            Example: `2.13`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546851122`
        - **1_3** (object)
          1 3
          Example: `{'id': '824744', 'over_od': '1.89', 'handicap': '2.5,3', 'under_od': '2.02', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `824744`
          - **over_od** (string)
            Over Od
            Example: `1.89`
          - **handicap** (string)
            Handicap
            Example: `2.5,3`
          - **under_od** (string)
            Under Od
            Example: `2.02`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546851137`
        - **1_1** (object)
          1 1
          Example: `{'id': '1261357', 'home_od': '2.07', 'draw_od': '3.6', 'away_od': '3.1', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1261357`
          - **home_od** (string)
            Home Od
            Example: `2.07`
          - **draw_od** (string)
            Draw Od
            Example: `3.6`
          - **away_od** (string)
            Away Od
            Example: `3.1`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546851129`
      - **end** (object)
        End
        Example: `{'1_2': {'id': '1166614', 'home_od': '1.74', 'handicap': '0,-0.5', 'away_od': '2.24', 'ss': None, 't`
        Nested fields:
        - **1_2** (object)
          1 2
          Example: `{'id': '1166614', 'home_od': '1.74', 'handicap': '0,-0.5', 'away_od': '2.24', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1166614`
          - **home_od** (string)
            Home Od
            Example: `1.74`
          - **handicap** (string)
            Handicap
            Example: `0,-0.5`
          - **away_od** (string)
            Away Od
            Example: `2.24`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937242`
        - **1_3** (object)
          1 3
          Example: `{'id': '825643', 'over_od': '1.8', 'handicap': '2.5,3', 'under_od': '2.12', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `825643`
          - **over_od** (string)
            Over Od
            Example: `1.8`
          - **handicap** (string)
            Handicap
            Example: `2.5,3`
          - **under_od** (string)
            Under Od
            Example: `2.12`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546935711`
        - **1_1** (object)
          1 1
          Example: `{'id': '1262771', 'home_od': '1.97', 'draw_od': '3.8', 'away_od': '3.3', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1262771`
          - **home_od** (string)
            Home Od
            Example: `1.97`
          - **draw_od** (string)
            Draw Od
            Example: `3.8`
          - **away_od** (string)
            Away Od
            Example: `3.3`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937250`
  - **WilliamHill** (object)
    Williamhill
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938227, '1_3': 1546937327}, 'odds': {'start': {'1_3`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938227, '1_3': 1546937327}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938227`
      - **1_3** (integer)
        1 3
        Example: `1546937327`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_3': {'id': '252946', 'over_od': '1.70', 'handicap': '2.5', 'under_od': '2.05', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_3': {'id': '252946', 'over_od': '1.70', 'handicap': '2.5', 'under_od': '2.05', 'ss': None, 'time`
        Nested fields:
        - **1_3** (object)
          1 3
          Example: `{'id': '252946', 'over_od': '1.70', 'handicap': '2.5', 'under_od': '2.05', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `252946`
          - **over_od** (string)
            Over Od
            Example: `1.70`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.05`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546697332`
        - **1_1** (object)
          1 1
          Example: `{'id': '2181547', 'home_od': '1.95', 'draw_od': '3.50', 'away_od': '3.60', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2181547`
          - **home_od** (string)
            Home Od
            Example: `1.95`
          - **draw_od** (string)
            Draw Od
            Example: `3.50`
          - **away_od** (string)
            Away Od
            Example: `3.60`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546697341`
      - **end** (object)
        End
        Example: `{'1_3': {'id': '253574', 'over_od': '1.60', 'handicap': '2.5', 'under_od': '2.25', 'ss': None, 'time`
        Nested fields:
        - **1_3** (object)
          1 3
          Example: `{'id': '253574', 'over_od': '1.60', 'handicap': '2.5', 'under_od': '2.25', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `253574`
          - **over_od** (string)
            Over Od
            Example: `1.60`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.25`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937327`
        - **1_1** (object)
          1 1
          Example: `{'id': '2201134', 'home_od': 'EVS', 'draw_od': '3.600', 'away_od': '3.500', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2201134`
          - **home_od** (string)
            Home Od
            Example: `EVS`
          - **draw_od** (string)
            Draw Od
            Example: `3.600`
          - **away_od** (string)
            Away Od
            Example: `3.500`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `00:53`
          - **add_time** (string)
            Add Time
            Example: `1546937795`
  - **BetClic** (object)
    Betclic
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546937223, '1_3': 1546937223}, 'odds': {'start': {'1_3`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546937223, '1_3': 1546937223}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546937223`
      - **1_3** (integer)
        1 3
        Example: `1546937223`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_3': {'id': '1180701', 'over_od': '1.75', 'handicap': '2.5', 'under_od': '2.10', 'ss': `
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_3': {'id': '1180701', 'over_od': '1.75', 'handicap': '2.5', 'under_od': '2.10', 'ss': None, 'tim`
        Nested fields:
        - **1_3** (object)
          1 3
          Example: `{'id': '1180701', 'over_od': '1.75', 'handicap': '2.5', 'under_od': '2.10', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1180701`
          - **over_od** (string)
            Over Od
            Example: `1.75`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.10`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546682880`
        - **1_1** (object)
          1 1
          Example: `{'id': '2401010', 'home_od': '2.06', 'draw_od': '3.50', 'away_od': '3.57', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2401010`
          - **home_od** (string)
            Home Od
            Example: `2.06`
          - **draw_od** (string)
            Draw Od
            Example: `3.50`
          - **away_od** (string)
            Away Od
            Example: `3.57`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546682880`
      - **end** (object)
        End
        Example: `{'1_3': {'id': '1183269', 'over_od': '1.62', 'handicap': '2.5', 'under_od': '2.31', 'ss': None, 'tim`
        Nested fields:
        - **1_3** (object)
          1 3
          Example: `{'id': '1183269', 'over_od': '1.62', 'handicap': '2.5', 'under_od': '2.31', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1183269`
          - **over_od** (string)
            Over Od
            Example: `1.62`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.31`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937223`
        - **1_1** (object)
          1 1
          Example: `{'id': '2404788', 'home_od': '1.94', 'draw_od': '3.73', 'away_od': '3.62', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2404788`
          - **home_od** (string)
            Home Od
            Example: `1.94`
          - **draw_od** (string)
            Draw Od
            Example: `3.73`
          - **away_od** (string)
            Away Od
            Example: `3.62`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937223`
  - **PinnacleSports** (object)
    Pinnaclesports
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546937388, '1_2': 1546937388, '1_3': 1546937388}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546937388, '1_2': 1546937388, '1_3': 1546937388}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546937388`
      - **1_2** (integer)
        1 2
        Example: `1546937388`
      - **1_3** (integer)
        1 3
        Example: `1546937388`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '373970', 'home_od': '2.120', 'draw_od': '3.660', 'away_od': '3.570', 'ss':`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '373970', 'home_od': '2.120', 'draw_od': '3.660', 'away_od': '3.570', 'ss': None, 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '373970', 'home_od': '2.120', 'draw_od': '3.660', 'away_od': '3.570', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `373970`
          - **home_od** (string)
            Home Od
            Example: `2.120`
          - **draw_od** (string)
            Draw Od
            Example: `3.660`
          - **away_od** (string)
            Away Od
            Example: `3.570`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546891213`
        - **1_2** (object)
          1 2
          Example: `{'id': '333293', 'home_od': '1.833', 'handicap': '0-0.5', 'away_od': '2.100', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `333293`
          - **home_od** (string)
            Home Od
            Example: `1.833`
          - **handicap** (string)
            Handicap
            Example: `0-0.5`
          - **away_od** (string)
            Away Od
            Example: `2.100`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546891213`
        - **1_3** (object)
          1 3
          Example: `{'id': '280486', 'over_od': '1.833', 'handicap': '2.75', 'under_od': '2.070', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `280486`
          - **over_od** (string)
            Over Od
            Example: `1.833`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `2.070`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546891213`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '374452', 'home_od': '2.000', 'draw_od': '3.850', 'away_od': '3.750', 'ss': None, 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '374452', 'home_od': '2.000', 'draw_od': '3.850', 'away_od': '3.750', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `374452`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **draw_od** (string)
            Draw Od
            Example: `3.850`
          - **away_od** (string)
            Away Od
            Example: `3.750`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937381`
        - **1_2** (object)
          1 2
          Example: `{'id': '333734', 'home_od': '2.000', 'handicap': '0.5', 'away_od': '1.917', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `333734`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **handicap** (string)
            Handicap
            Example: `0.5`
          - **away_od** (string)
            Away Od
            Example: `1.917`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937243`
        - **1_3** (object)
          1 3
          Example: `{'id': '280863', 'over_od': '2.070', 'handicap': '3', 'under_od': '1.833', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `280863`
          - **over_od** (string)
            Over Od
            Example: `2.070`
          - **handicap** (string)
            Handicap
            Example: `3`
          - **under_od** (string)
            Under Od
            Example: `1.833`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937381`
  - **PlanetWin365** (object)
    Planetwin365
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938228, '1_3': 1546938228}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938228, '1_3': 1546938228}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938228`
      - **1_3** (integer)
        1 3
        Example: `1546938228`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '18508499', 'home_od': '1.88', 'draw_od': '3.77', 'away_od': '3.40', 'ss': `
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '18508499', 'home_od': '1.88', 'draw_od': '3.77', 'away_od': '3.40', 'ss': '0-0', 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '18508499', 'home_od': '1.88', 'draw_od': '3.77', 'away_od': '3.40', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `18508499`
          - **home_od** (string)
            Home Od
            Example: `1.88`
          - **draw_od** (string)
            Draw Od
            Example: `3.77`
          - **away_od** (string)
            Away Od
            Example: `3.40`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `00:00`
          - **add_time** (string)
            Add Time
            Example: `1546937771`
        - **1_3** (object)
          1 3
          Example: `{'id': '11112554', 'over_od': '1.63', 'handicap': '2.5', 'under_od': '2.14', 'ss': '0-0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `11112554`
          - **over_od** (string)
            Over Od
            Example: `1.63`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.14`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `00:00`
          - **add_time** (string)
            Add Time
            Example: `1546937771`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '18508525', 'home_od': '1.91', 'draw_od': '3.64', 'away_od': '3.42', 'ss': '0-0', 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '18508525', 'home_od': '1.91', 'draw_od': '3.64', 'away_od': '3.42', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `18508525`
          - **home_od** (string)
            Home Od
            Example: `1.91`
          - **draw_od** (string)
            Draw Od
            Example: `3.64`
          - **away_od** (string)
            Away Od
            Example: `3.42`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:00`
          - **add_time** (string)
            Add Time
            Example: `1546938196`
        - **1_3** (object)
          1 3
          Example: `{'id': '11112580', 'over_od': '1.76', 'handicap': '2.5', 'under_od': '1.95', 'ss': '0-0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `11112580`
          - **over_od** (string)
            Over Od
            Example: `1.76`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `1.95`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:00`
          - **add_time** (string)
            Add Time
            Example: `1546938196`
  - **188Bet** (object)
    188Bet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938227, '1_2': 1546938227, '1_3': 1546938227}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938227, '1_2': 1546938227, '1_3': 1546938227}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938227`
      - **1_2** (integer)
        1 2
        Example: `1546938227`
      - **1_3** (integer)
        1 3
        Example: `1546938227`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '2065500', 'home_od': '0.00', 'draw_od': '0.00', 'away_od': '0.00', 'ss': '`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '2065500', 'home_od': '0.00', 'draw_od': '0.00', 'away_od': '0.00', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '2065500', 'home_od': '0.00', 'draw_od': '0.00', 'away_od': '0.00', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2065500`
          - **home_od** (string)
            Home Od
            Example: `0.00`
          - **draw_od** (string)
            Draw Od
            Example: `0.00`
          - **away_od** (string)
            Away Od
            Example: `0.00`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: ``
          - **add_time** (string)
            Add Time
            Example: `1546937410`
        - **1_2** (object)
          1 2
          Example: `{'id': '95020', 'home_od': '0.00', 'handicap': '-0.5', 'away_od': '0.00', 'ss': '0-0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `95020`
          - **home_od** (string)
            Home Od
            Example: `0.00`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `0.00`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: ``
          - **add_time** (string)
            Add Time
            Example: `1546937410`
        - **1_3** (object)
          1 3
          Example: `{'id': '144897', 'over_od': '0.00', 'handicap': '2.5/3', 'under_od': '0.00', 'ss': '0-0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `144897`
          - **over_od** (string)
            Over Od
            Example: `0.00`
          - **handicap** (string)
            Handicap
            Example: `2.5/3`
          - **under_od** (string)
            Under Od
            Example: `0.00`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: ``
          - **add_time** (string)
            Add Time
            Example: `1546937410`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '2065554', 'home_od': '1.98', 'draw_od': '3.70', 'away_od': '3.30', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '2065554', 'home_od': '1.98', 'draw_od': '3.70', 'away_od': '3.30', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2065554`
          - **home_od** (string)
            Home Od
            Example: `1.98`
          - **draw_od** (string)
            Draw Od
            Example: `3.70`
          - **away_od** (string)
            Away Od
            Example: `3.30`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `06:43`
          - **add_time** (string)
            Add Time
            Example: `1546938141`
        - **1_2** (object)
          1 2
          Example: `{'id': '95148', 'home_od': '2.02', 'handicap': '-0.5', 'away_od': '1.90', 'ss': '0-0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `95148`
          - **home_od** (string)
            Home Od
            Example: `2.02`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.90`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `08:10`
          - **add_time** (string)
            Add Time
            Example: `1546938227`
        - **1_3** (object)
          1 3
          Example: `{'id': '145045', 'over_od': '1.95', 'handicap': '2.5/3', 'under_od': '1.95', 'ss': '0-0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `145045`
          - **over_od** (string)
            Over Od
            Example: `1.95`
          - **handicap** (string)
            Handicap
            Example: `2.5/3`
          - **under_od** (string)
            Under Od
            Example: `1.95`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `08:10`
          - **add_time** (string)
            Add Time
            Example: `1546938227`
  - **UniBet** (object)
    Unibet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938227, '1_2': 1546938028, '1_3': 1546938028}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938227, '1_2': 1546938028, '1_3': 1546938028}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938227`
      - **1_2** (integer)
        1 2
        Example: `1546938028`
      - **1_3** (integer)
        1 3
        Example: `1546938028`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '10200178', 'home_od': '2.04', 'draw_od': '3.55', 'away_od': '3.6', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '10200178', 'home_od': '2.04', 'draw_od': '3.55', 'away_od': '3.6', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '10200178', 'home_od': '2.04', 'draw_od': '3.55', 'away_od': '3.6', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `10200178`
          - **home_od** (string)
            Home Od
            Example: `2.04`
          - **draw_od** (string)
            Draw Od
            Example: `3.55`
          - **away_od** (string)
            Away Od
            Example: `3.6`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546796904`
        - **1_2** (object)
          1 2
          Example: `{'id': '2756213', 'home_od': '1.94', 'handicap': '-0.5', 'away_od': '1.81', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2756213`
          - **home_od** (string)
            Home Od
            Example: `1.94`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.81`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `00:00`
          - **add_time** (string)
            Add Time
            Example: `1546936355`
        - **1_3** (object)
          1 3
          Example: `{'id': '3928631', 'over_od': '1.68', 'handicap': '2.5', 'under_od': '2.18', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3928631`
          - **over_od** (string)
            Over Od
            Example: `1.68`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.18`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546799916`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '10215880', 'home_od': '1.96', 'draw_od': '3.7', 'away_od': '3.6', 'ss': '0-0', 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '10215880', 'home_od': '1.96', 'draw_od': '3.7', 'away_od': '3.6', 'ss': '0-0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `10215880`
          - **home_od** (string)
            Home Od
            Example: `1.96`
          - **draw_od** (string)
            Draw Od
            Example: `3.7`
          - **away_od** (string)
            Away Od
            Example: `3.6`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:10`
          - **add_time** (string)
            Add Time
            Example: `1546938172`
        - **1_2** (object)
          1 2
          Example: `{'id': '2756241', 'home_od': '1.87', 'handicap': '-0.5', 'away_od': '1.87', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2756241`
          - **home_od** (string)
            Home Od
            Example: `1.87`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.87`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `03:29`
          - **add_time** (string)
            Add Time
            Example: `1546937951`
        - **1_3** (object)
          1 3
          Example: `{'id': '3935761', 'over_od': '1.61', 'handicap': '2.5', 'under_od': '2.23', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3935761`
          - **over_od** (string)
            Over Od
            Example: `1.61`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.23`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `03:29`
          - **add_time** (string)
            Add Time
            Example: `1546937951`
  - **BWin** (object)
    Bwin
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938229, '1_3': 1546938229}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938229, '1_3': 1546938229}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938229`
      - **1_3** (integer)
        1 3
        Example: `1546938229`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '12954250', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.4', 'ss': '0-0'`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '12954250', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.4', 'ss': '0-0', 'time_st`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '12954250', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.4', 'ss': '0-0', 'time_str': '5',`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `12954250`
          - **home_od** (string)
            Home Od
            Example: `2`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `3.4`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `5`
          - **add_time** (string)
            Add Time
            Example: `1546934504`
        - **1_3** (object)
          1 3
          Example: `{'id': '55939718', 'over_od': '1.65', 'handicap': '2.5', 'under_od': '2.1', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `55939718`
          - **over_od** (string)
            Over Od
            Example: `1.65`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.1`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `5`
          - **add_time** (string)
            Add Time
            Example: `1546934505`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '12954370', 'home_od': '1.9', 'draw_od': '3.4', 'away_od': '3.9', 'ss': '0-0', 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '12954370', 'home_od': '1.9', 'draw_od': '3.4', 'away_od': '3.9', 'ss': '0-0', 'time_str': '7`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `12954370`
          - **home_od** (string)
            Home Od
            Example: `1.9`
          - **draw_od** (string)
            Draw Od
            Example: `3.4`
          - **away_od** (string)
            Away Od
            Example: `3.9`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `7`
          - **add_time** (string)
            Add Time
            Example: `1546938157`
        - **1_3** (object)
          1 3
          Example: `{'id': '55947607', 'over_od': '1.65', 'handicap': '2.5', 'under_od': '2.1', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `55947607`
          - **over_od** (string)
            Over Od
            Example: `1.65`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.1`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `7`
          - **add_time** (string)
            Add Time
            Example: `1546938157`
  - **BetFair** (object)
    Betfair
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226}, 'odds': {'start': {'1_1': {'id': '19611253`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '19611253', 'home_od': '2.1', 'draw_od': '3.7', 'away_od': '3.4', 'ss': Non`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '19611253', 'home_od': '2.1', 'draw_od': '3.7', 'away_od': '3.4', 'ss': None, 'time_s`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '19611253', 'home_od': '2.1', 'draw_od': '3.7', 'away_od': '3.4', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `19611253`
          - **home_od** (string)
            Home Od
            Example: `2.1`
          - **draw_od** (string)
            Draw Od
            Example: `3.7`
          - **away_od** (string)
            Away Od
            Example: `3.4`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546853048`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '19627623', 'home_od': '1.9', 'draw_od': '3.5', 'away_od': '4', 'ss': '0-0', 'time_st`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '19627623', 'home_od': '1.9', 'draw_od': '3.5', 'away_od': '4', 'ss': '0-0', 'time_str': '7',`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `19627623`
          - **home_od** (string)
            Home Od
            Example: `1.9`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `4`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `7`
          - **add_time** (string)
            Add Time
            Example: `1546938221`
  - **BetFred** (object)
    Betfred
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546933517, '1_3': 1546933518}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546933517, '1_3': 1546933518}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546933517`
      - **1_3** (integer)
        1 3
        Example: `1546933518`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '1139393', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.50', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '1139393', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.50', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '1139393', 'home_od': '2.00', 'draw_od': '3.40', 'away_od': '3.50', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1139393`
          - **home_od** (string)
            Home Od
            Example: `2.00`
          - **draw_od** (string)
            Draw Od
            Example: `3.40`
          - **away_od** (string)
            Away Od
            Example: `3.50`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546688182`
        - **1_2** (unknown)
          1 2
        - **1_3** (object)
          1 3
          Example: `{'id': '316326', 'over_od': '1.04', 'handicap': '0.5', 'under_od': '10.00', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `316326`
          - **over_od** (string)
            Over Od
            Example: `1.04`
          - **handicap** (string)
            Handicap
            Example: `0.5`
          - **under_od** (string)
            Under Od
            Example: `10.00`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546688182`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '1142481', 'home_od': '1.95', 'draw_od': '3.60', 'away_od': '3.40', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '1142481', 'home_od': '1.95', 'draw_od': '3.60', 'away_od': '3.40', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1142481`
          - **home_od** (string)
            Home Od
            Example: `1.95`
          - **draw_od** (string)
            Draw Od
            Example: `3.60`
          - **away_od** (string)
            Away Od
            Example: `3.40`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546933517`
        - **1_2** (unknown)
          1 2
        - **1_3** (object)
          1 3
          Example: `{'id': '316946', 'over_od': '1.62', 'handicap': '2.5', 'under_od': '2.20', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `316946`
          - **over_od** (string)
            Over Od
            Example: `1.62`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.20`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546855406`
  - **CloudBet** (object)
    Cloudbet
    Example: `{'matching_dir': '1', 'odds_update': {}, 'odds': {'start': {'1_1': None, '1_2': None, '1_3': None}, `
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{}`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': None, '1_2': None, '1_3': None}, 'end': {'1_1': None, '1_2': None, '1_3': None}}`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': None, '1_2': None, '1_3': None}`
        Nested fields:
        - **1_1** (unknown)
          1 1
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
      - **end** (object)
        End
        Example: `{'1_1': None, '1_2': None, '1_3': None}`
        Nested fields:
        - **1_1** (unknown)
          1 1
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
  - **Betsson** (object)
    Betsson
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938225, '1_3': 1546938225}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938225, '1_3': 1546938225}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938225`
      - **1_3** (integer)
        1 3
        Example: `1546938225`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '15761888', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None,`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '15761888', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, 'time_str`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '15761888', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, 'time_str': None,`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `15761888`
          - **home_od** (string)
            Home Od
            Example: `2`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `3.5`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546694543`
        - **1_3** (object)
          1 3
          Example: `{'id': '23577862', 'over_od': '2.7', 'handicap': '3.5', 'under_od': '1.41', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `23577862`
          - **over_od** (string)
            Over Od
            Example: `2.7`
          - **handicap** (string)
            Handicap
            Example: `3.5`
          - **under_od** (string)
            Under Od
            Example: `1.41`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546694543`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '15841063', 'home_od': '1.95', 'draw_od': '3.7', 'away_od': '3.5', 'ss': '0-0', 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '15841063', 'home_od': '1.95', 'draw_od': '3.7', 'away_od': '3.5', 'ss': '0-0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `15841063`
          - **home_od** (string)
            Home Od
            Example: `1.95`
          - **draw_od** (string)
            Draw Od
            Example: `3.7`
          - **away_od** (string)
            Away Od
            Example: `3.5`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `7`
          - **add_time** (string)
            Add Time
            Example: `1546938184`
        - **1_3** (object)
          1 3
          Example: `{'id': '23673270', 'over_od': '1.69', 'handicap': '2.5', 'under_od': '2.07', 'ss': '0-0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `23673270`
          - **over_od** (string)
            Over Od
            Example: `1.69`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.07`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938214`
  - **PaddyPower** (object)
    Paddypower
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938228}, 'odds': {'start': {'1_1': {'id': '1153297'`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938228}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938228`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '1153297', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.25', 'ss': None,`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '1153297', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.25', 'ss': None, 'time_str`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '1153297', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.25', 'ss': None, 'time_str': None,`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1153297`
          - **home_od** (string)
            Home Od
            Example: `2`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `3.25`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546795531`
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
      - **end** (object)
        End
        Example: `{'1_1': {'id': '1168675', 'home_od': '1.83', 'draw_od': '3.5', 'away_od': '3.75', 'ss': '0-0', 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '1168675', 'home_od': '1.83', 'draw_od': '3.5', 'away_od': '3.75', 'ss': '0-0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1168675`
          - **home_od** (string)
            Home Od
            Example: `1.83`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `3.75`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938228`
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
  - **SBOBET** (object)
    Sbobet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226, '1_2': 1546938226, '1_3': 1546938226}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226, '1_2': 1546938226, '1_3': 1546938226}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
      - **1_2** (integer)
        1 2
        Example: `1546938226`
      - **1_3** (integer)
        1 3
        Example: `1546938226`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '7479800', 'home_od': '2.09', 'draw_od': '3.3', 'away_od': '3.35', 'ss': No`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '7479800', 'home_od': '2.09', 'draw_od': '3.3', 'away_od': '3.35', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '7479800', 'home_od': '2.09', 'draw_od': '3.3', 'away_od': '3.35', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `7479800`
          - **home_od** (string)
            Home Od
            Example: `2.09`
          - **draw_od** (string)
            Draw Od
            Example: `3.3`
          - **away_od** (string)
            Away Od
            Example: `3.35`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546735352`
        - **1_2** (object)
          1 2
          Example: `{'id': '4866950', 'home_od': '1.84', 'handicap': '0.25', 'away_od': '2.08', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4866950`
          - **home_od** (string)
            Home Od
            Example: `1.84`
          - **handicap** (string)
            Handicap
            Example: `0.25`
          - **away_od** (string)
            Away Od
            Example: `2.08`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546735352`
        - **1_3** (object)
          1 3
          Example: `{'id': '6529331', 'over_od': '1.97', 'handicap': '2.75', 'under_od': '1.93', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6529331`
          - **over_od** (string)
            Over Od
            Example: `1.97`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.93`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546735352`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '7562650', 'home_od': '2.11', 'draw_od': '3.35', 'away_od': '3.25', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '7562650', 'home_od': '2.11', 'draw_od': '3.35', 'away_od': '3.25', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `7562650`
          - **home_od** (string)
            Home Od
            Example: `2.11`
          - **draw_od** (string)
            Draw Od
            Example: `3.35`
          - **away_od** (string)
            Away Od
            Example: `3.25`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938226`
        - **1_2** (object)
          1 2
          Example: `{'id': '4921480', 'home_od': '2.11', 'handicap': '0.5', 'away_od': '1.82', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4921480`
          - **home_od** (string)
            Home Od
            Example: `2.11`
          - **handicap** (string)
            Handicap
            Example: `0.5`
          - **away_od** (string)
            Away Od
            Example: `1.82`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938226`
        - **1_3** (object)
          1 3
          Example: `{'id': '6605217', 'over_od': '1.96', 'handicap': '2.75', 'under_od': '1.94', 'ss': '0-0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6605217`
          - **over_od** (string)
            Over Od
            Example: `1.96`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.94`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8`
          - **add_time** (string)
            Add Time
            Example: `1546938224`
  - **888Sport** (object)
    888Sport
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226, '1_2': 1546938224, '1_3': 1546938224}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226, '1_2': 1546938224, '1_3': 1546938224}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
      - **1_2** (integer)
        1 2
        Example: `1546938224`
      - **1_3** (integer)
        1 3
        Example: `1546938224`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '8697455', 'home_od': '1.96', 'draw_od': '3.4', 'away_od': '3.45', 'ss': No`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '8697455', 'home_od': '1.96', 'draw_od': '3.4', 'away_od': '3.45', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '8697455', 'home_od': '1.96', 'draw_od': '3.4', 'away_od': '3.45', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `8697455`
          - **home_od** (string)
            Home Od
            Example: `1.96`
          - **draw_od** (string)
            Draw Od
            Example: `3.4`
          - **away_od** (string)
            Away Od
            Example: `3.45`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546796717`
        - **1_2** (object)
          1 2
          Example: `{'id': '2969864', 'home_od': '1.94', 'handicap': '-0.5', 'away_od': '1.81', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2969864`
          - **home_od** (string)
            Home Od
            Example: `1.94`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.81`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `00:00`
          - **add_time** (string)
            Add Time
            Example: `1546936225`
        - **1_3** (object)
          1 3
          Example: `{'id': '4210372', 'over_od': '1.68', 'handicap': '2.5', 'under_od': '2.18', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4210372`
          - **over_od** (string)
            Over Od
            Example: `1.68`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.18`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546799721`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '8712079', 'home_od': '1.96', 'draw_od': '3.7', 'away_od': '3.6', 'ss': '0-0', 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '8712079', 'home_od': '1.96', 'draw_od': '3.7', 'away_od': '3.6', 'ss': '0-0', 'time_str': '0`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `8712079`
          - **home_od** (string)
            Home Od
            Example: `1.96`
          - **draw_od** (string)
            Draw Od
            Example: `3.7`
          - **away_od** (string)
            Away Od
            Example: `3.6`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:13`
          - **add_time** (string)
            Add Time
            Example: `1546938169`
        - **1_2** (object)
          1 2
          Example: `{'id': '2969915', 'home_od': '1.93', 'handicap': '-0.5', 'away_od': '1.81', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2969915`
          - **home_od** (string)
            Home Od
            Example: `1.93`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.81`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:18`
          - **add_time** (string)
            Add Time
            Example: `1546938179`
        - **1_3** (object)
          1 3
          Example: `{'id': '4217989', 'over_od': '1.68', 'handicap': '2.5', 'under_od': '2.1', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4217989`
          - **over_od** (string)
            Over Od
            Example: `1.68`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.1`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:18`
          - **add_time** (string)
            Add Time
            Example: `1546938179`
  - **TitanBet** (object)
    Titanbet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546937257}, 'odds': {'start': {'1_1': {'id': '3575360'`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546937257}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546937257`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '3575360', 'home_od': '2.05', 'draw_od': '3.55', 'away_od': '3.35', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '3575360', 'home_od': '2.05', 'draw_od': '3.55', 'away_od': '3.35', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '3575360', 'home_od': '2.05', 'draw_od': '3.55', 'away_od': '3.35', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3575360`
          - **home_od** (string)
            Home Od
            Example: `2.05`
          - **draw_od** (string)
            Draw Od
            Example: `3.55`
          - **away_od** (string)
            Away Od
            Example: `3.35`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546887488`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '3575618', 'home_od': '2.00', 'draw_od': '3.70', 'away_od': '3.30', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '3575618', 'home_od': '2.00', 'draw_od': '3.70', 'away_od': '3.30', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3575618`
          - **home_od** (string)
            Home Od
            Example: `2.00`
          - **draw_od** (string)
            Draw Od
            Example: `3.70`
          - **away_od** (string)
            Away Od
            Example: `3.30`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936722`
  - **BetAtHome** (object)
    Betathome
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546912791, '1_3': 1546912364}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546912791, '1_3': 1546912364}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546912791`
      - **1_3** (integer)
        1 3
        Example: `1546912364`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '1090347', 'home_od': '1.96', 'draw_od': '3.40', 'away_od': '3.39', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '1090347', 'home_od': '1.96', 'draw_od': '3.40', 'away_od': '3.39', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '1090347', 'home_od': '1.96', 'draw_od': '3.40', 'away_od': '3.39', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1090347`
          - **home_od** (string)
            Home Od
            Example: `1.96`
          - **draw_od** (string)
            Draw Od
            Example: `3.40`
          - **away_od** (string)
            Away Od
            Example: `3.39`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546754101`
        - **1_3** (object)
          1 3
          Example: `{'id': '518691', 'over_od': '2.09', 'handicap': '2.50', 'under_od': '1.67', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `518691`
          - **over_od** (string)
            Over Od
            Example: `2.09`
          - **handicap** (string)
            Handicap
            Example: `2.50`
          - **under_od** (string)
            Under Od
            Example: `1.67`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546816251`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '1092674', 'home_od': '1.99', 'draw_od': '3.46', 'away_od': '3.25', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '1092674', 'home_od': '1.99', 'draw_od': '3.46', 'away_od': '3.25', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `1092674`
          - **home_od** (string)
            Home Od
            Example: `1.99`
          - **draw_od** (string)
            Draw Od
            Example: `3.46`
          - **away_od** (string)
            Away Od
            Example: `3.25`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546878573`
        - **1_3** (object)
          1 3
          Example: `{'id': '518849', 'over_od': '2.16', 'handicap': '2.50', 'under_od': '1.62', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `518849`
          - **over_od** (string)
            Over Od
            Example: `2.16`
          - **handicap** (string)
            Handicap
            Example: `2.50`
          - **under_od** (string)
            Under Od
            Example: `1.62`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546853695`
  - **DafaBet** (object)
    Dafabet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938073}, 'odds': {'start': {'1_1': {'id': '9441158'`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938073}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938073`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '9441158', 'home_od': '1.94', 'draw_od': '3.74', 'away_od': '3.62', 'ss': '`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '9441158', 'home_od': '1.94', 'draw_od': '3.74', 'away_od': '3.62', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '9441158', 'home_od': '1.94', 'draw_od': '3.74', 'away_od': '3.62', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `9441158`
          - **home_od** (string)
            Home Od
            Example: `1.94`
          - **draw_od** (string)
            Draw Od
            Example: `3.74`
          - **away_od** (string)
            Away Od
            Example: `3.62`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937109`
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
      - **end** (object)
        End
        Example: `{'1_1': {'id': '9441230', 'home_od': '2.01', 'draw_od': '3.72', 'away_od': '3.67', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '9441230', 'home_od': '2.01', 'draw_od': '3.72', 'away_od': '3.67', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `9441230`
          - **home_od** (string)
            Home Od
            Example: `2.01`
          - **draw_od** (string)
            Draw Od
            Example: `3.72`
          - **away_od** (string)
            Away Od
            Example: `3.67`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `5:27`
          - **add_time** (string)
            Add Time
            Example: `1546938073`
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
  - **Marathonbet** (object)
    Marathonbet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226}, 'odds': {'start': {'1_1': {'id': '2952046'`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '2952046', 'home_od': '1.98', 'draw_od': '3.62', 'away_od': '3.62', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '2952046', 'home_od': '1.98', 'draw_od': '3.62', 'away_od': '3.62', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '2952046', 'home_od': '1.98', 'draw_od': '3.62', 'away_od': '3.62', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2952046`
          - **home_od** (string)
            Home Od
            Example: `1.98`
          - **draw_od** (string)
            Draw Od
            Example: `3.62`
          - **away_od** (string)
            Away Od
            Example: `3.62`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937417`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '2952192', 'home_od': '2.01', 'draw_od': '3.48', 'away_od': '3.65', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '2952192', 'home_od': '2.01', 'draw_od': '3.48', 'away_od': '3.65', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2952192`
          - **home_od** (string)
            Home Od
            Example: `2.01`
          - **draw_od** (string)
            Draw Od
            Example: `3.48`
          - **away_od** (string)
            Away Od
            Example: `3.65`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546938196`
  - **BetVictor** (object)
    Betvictor
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226, '1_2': 1546938229, '1_3': 1546938211}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226, '1_2': 1546938229, '1_3': 1546938211}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
      - **1_2** (integer)
        1 2
        Example: `1546938229`
      - **1_3** (integer)
        1 3
        Example: `1546938211`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '6943802', 'home_od': '2.2', 'draw_od': '3.7', 'away_od': '3.125', 'ss': No`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '6943802', 'home_od': '2.2', 'draw_od': '3.7', 'away_od': '3.125', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '6943802', 'home_od': '2.2', 'draw_od': '3.7', 'away_od': '3.125', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6943802`
          - **home_od** (string)
            Home Od
            Example: `2.2`
          - **draw_od** (string)
            Draw Od
            Example: `3.7`
          - **away_od** (string)
            Away Od
            Example: `3.125`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546923912`
        - **1_2** (object)
          1 2
          Example: `{'id': '6979538', 'home_od': '1.65', 'handicap': '0', 'away_od': '2.36', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6979538`
          - **home_od** (string)
            Home Od
            Example: `1.65`
          - **handicap** (string)
            Handicap
            Example: `0`
          - **away_od** (string)
            Away Od
            Example: `2.36`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546923912`
        - **1_3** (object)
          1 3
          Example: `{'id': '7399381', 'over_od': '1.833', 'handicap': '2.5,3', 'under_od': '2.02', 'ss': None, 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `7399381`
          - **over_od** (string)
            Over Od
            Example: `1.833`
          - **handicap** (string)
            Handicap
            Example: `2.5,3`
          - **under_od** (string)
            Under Od
            Example: `2.02`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546923912`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '6944060', 'home_od': '2', 'draw_od': '3.6', 'away_od': '3.4', 'ss': '0-0', 'time_str`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '6944060', 'home_od': '2', 'draw_od': '3.6', 'away_od': '3.4', 'ss': '0-0', 'time_str': '08:0`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6944060`
          - **home_od** (string)
            Home Od
            Example: `2`
          - **draw_od** (string)
            Draw Od
            Example: `3.6`
          - **away_od** (string)
            Away Od
            Example: `3.4`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `08:07`
          - **add_time** (string)
            Add Time
            Example: `1546938226`
        - **1_2** (object)
          1 2
          Example: `{'id': '6980456', 'home_od': '2.03', 'handicap': '-0.5', 'away_od': '1.86', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6980456`
          - **home_od** (string)
            Home Od
            Example: `2.03`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.86`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `08:07`
          - **add_time** (string)
            Add Time
            Example: `1546938229`
        - **1_3** (object)
          1 3
          Example: `{'id': '7399913', 'over_od': '1.909', 'handicap': '2.5,3', 'under_od': '1.925', 'ss': '0-0', 'time_s`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `7399913`
          - **over_od** (string)
            Over Od
            Example: `1.909`
          - **handicap** (string)
            Handicap
            Example: `2.5,3`
          - **under_od** (string)
            Under Od
            Example: `1.925`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:32`
          - **add_time** (string)
            Add Time
            Example: `1546938196`
  - **Intertops** (object)
    Intertops
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546936705, '1_2': 1546936705, '1_3': 1546936705}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546936705, '1_2': 1546936705, '1_3': 1546936705}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546936705`
      - **1_2** (integer)
        1 2
        Example: `1546936705`
      - **1_3** (integer)
        1 3
        Example: `1546936705`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '293350', 'home_od': '1.95', 'draw_od': '3.35', 'away_od': '3.3', 'ss': Non`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '293350', 'home_od': '1.95', 'draw_od': '3.35', 'away_od': '3.3', 'ss': None, 'time_s`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '293350', 'home_od': '1.95', 'draw_od': '3.35', 'away_od': '3.3', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `293350`
          - **home_od** (string)
            Home Od
            Example: `1.95`
          - **draw_od** (string)
            Draw Od
            Example: `3.35`
          - **away_od** (string)
            Away Od
            Example: `3.3`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546790619`
        - **1_2** (object)
          1 2
          Example: `{'id': '87268', 'home_od': '1.75', 'handicap': '-0.25', 'away_od': '1.95', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `87268`
          - **home_od** (string)
            Home Od
            Example: `1.75`
          - **handicap** (string)
            Handicap
            Example: `-0.25`
          - **away_od** (string)
            Away Od
            Example: `1.95`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546790619`
        - **1_3** (object)
          1 3
          Example: `{'id': '128495', 'over_od': '1.65', 'handicap': '2.5', 'under_od': '2.1', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `128495`
          - **over_od** (string)
            Over Od
            Example: `1.65`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.1`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546790619`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '293888', 'home_od': '1.95', 'draw_od': '3.45', 'away_od': '3.35', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '293888', 'home_od': '1.95', 'draw_od': '3.45', 'away_od': '3.35', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `293888`
          - **home_od** (string)
            Home Od
            Example: `1.95`
          - **draw_od** (string)
            Draw Od
            Example: `3.45`
          - **away_od** (string)
            Away Od
            Example: `3.35`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546934703`
        - **1_2** (object)
          1 2
          Example: `{'id': '87572', 'home_od': '1.7', 'handicap': '-0.25', 'away_od': '2', 'ss': None, 'time_str': None,`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `87572`
          - **home_od** (string)
            Home Od
            Example: `1.7`
          - **handicap** (string)
            Handicap
            Example: `-0.25`
          - **away_od** (string)
            Away Od
            Example: `2`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546930754`
        - **1_3** (object)
          1 3
          Example: `{'id': '128615', 'over_od': '1.6', 'handicap': '2.5', 'under_od': '2.2', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `128615`
          - **over_od** (string)
            Over Od
            Example: `1.6`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.2`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546852758`
  - **Interwetten** (object)
    Interwetten
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546937574}, 'odds': {'start': {'1_1': {'id': '539276',`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546937574}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546937574`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '539276', 'home_od': '1.97', 'draw_od': '3.40', 'away_od': '3.40', 'ss': No`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '539276', 'home_od': '1.97', 'draw_od': '3.40', 'away_od': '3.40', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '539276', 'home_od': '1.97', 'draw_od': '3.40', 'away_od': '3.40', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `539276`
          - **home_od** (string)
            Home Od
            Example: `1.97`
          - **draw_od** (string)
            Draw Od
            Example: `3.40`
          - **away_od** (string)
            Away Od
            Example: `3.40`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546703129`
        - **1_2** (unknown)
          1 2
      - **end** (object)
        End
        Example: `{'1_1': {'id': '542190', 'home_od': '1.95', 'draw_od': '3.50', 'away_od': '3.35', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '542190', 'home_od': '1.95', 'draw_od': '3.50', 'away_od': '3.35', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `542190`
          - **home_od** (string)
            Home Od
            Example: `1.95`
          - **draw_od** (string)
            Draw Od
            Example: `3.50`
          - **away_od** (string)
            Away Od
            Example: `3.35`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936212`
        - **1_2** (unknown)
          1 2
  - **Betway** (object)
    Betway
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546936583, '1_3': 1546936583}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546936583, '1_3': 1546936583}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546936583`
      - **1_3** (integer)
        1 3
        Example: `1546936583`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '3260395', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, `
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '3260395', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, 'time_str'`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '3260395', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, 'time_str': None, `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3260395`
          - **home_od** (string)
            Home Od
            Example: `2`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `3.5`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546684254`
        - **1_3** (object)
          1 3
          Example: `{'id': '4467716', 'over_od': '1.727', 'handicap': '5', 'under_od': '2', 'ss': None, 'time_str': None`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4467716`
          - **over_od** (string)
            Over Od
            Example: `1.727`
          - **handicap** (string)
            Handicap
            Example: `5`
          - **under_od** (string)
            Under Od
            Example: `2`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546684254`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '3262886', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, 'time_str'`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '3262886', 'home_od': '2', 'draw_od': '3.5', 'away_od': '3.5', 'ss': None, 'time_str': None, `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3262886`
          - **home_od** (string)
            Home Od
            Example: `2`
          - **draw_od** (string)
            Draw Od
            Example: `3.5`
          - **away_od** (string)
            Away Od
            Example: `3.5`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546934513`
        - **1_3** (object)
          1 3
          Example: `{'id': '4469270', 'over_od': '1.615', 'handicap': '5', 'under_od': '2.2', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `4469270`
          - **over_od** (string)
            Over Od
            Example: `1.615`
          - **handicap** (string)
            Handicap
            Example: `5`
          - **under_od** (string)
            Under Od
            Example: `2.2`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546923453`
  - **1XBet** (object)
    1Xbet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938228, '1_2': 1546938164, '1_3': 1546938228}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938228, '1_2': 1546938164, '1_3': 1546938228}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938228`
      - **1_2** (integer)
        1 2
        Example: `1546938164`
      - **1_3** (integer)
        1 3
        Example: `1546938228`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '5666401', 'home_od': '2.09', 'draw_od': '3.88', 'away_od': '3.26', 'ss': '`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '5666401', 'home_od': '2.09', 'draw_od': '3.88', 'away_od': '3.26', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '5666401', 'home_od': '2.09', 'draw_od': '3.88', 'away_od': '3.26', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `5666401`
          - **home_od** (string)
            Home Od
            Example: `2.09`
          - **draw_od** (string)
            Draw Od
            Example: `3.88`
          - **away_od** (string)
            Away Od
            Example: `3.26`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936574`
        - **1_2** (object)
          1 2
          Example: `{'id': '3179794', 'home_od': '2.57', 'handicap': '-1', 'away_od': '1.57', 'ss': '0-0', 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3179794`
          - **home_od** (string)
            Home Od
            Example: `2.57`
          - **handicap** (string)
            Handicap
            Example: `-1`
          - **away_od** (string)
            Away Od
            Example: `1.57`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936769`
        - **1_3** (object)
          1 3
          Example: `{'id': '6088623', 'over_od': '2.095', 'handicap': '3', 'under_od': '1.825', 'ss': '0-0', 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6088623`
          - **over_od** (string)
            Over Od
            Example: `2.095`
          - **handicap** (string)
            Handicap
            Example: `3`
          - **under_od** (string)
            Under Od
            Example: `1.825`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936574`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '5666788', 'home_od': '1.94', 'draw_od': '3.82', 'away_od': '3.76', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '5666788', 'home_od': '1.94', 'draw_od': '3.82', 'away_od': '3.76', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `5666788`
          - **home_od** (string)
            Home Od
            Example: `1.94`
          - **draw_od** (string)
            Draw Od
            Example: `3.82`
          - **away_od** (string)
            Away Od
            Example: `3.76`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `07:18`
          - **add_time** (string)
            Add Time
            Example: `1546938176`
        - **1_2** (object)
          1 2
          Example: `{'id': '3179991', 'home_od': '2.64', 'handicap': '-1', 'away_od': '1.54', 'ss': '0-0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `3179991`
          - **home_od** (string)
            Home Od
            Example: `2.64`
          - **handicap** (string)
            Handicap
            Example: `-1`
          - **away_od** (string)
            Away Od
            Example: `1.54`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `06:01`
          - **add_time** (string)
            Add Time
            Example: `1546938099`
        - **1_3** (object)
          1 3
          Example: `{'id': '6088963', 'over_od': '2.216', 'handicap': '3', 'under_od': '1.74', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `6088963`
          - **over_od** (string)
            Over Od
            Example: `2.216`
          - **handicap** (string)
            Handicap
            Example: `3`
          - **under_od** (string)
            Under Od
            Example: `1.74`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `08:05`
          - **add_time** (string)
            Add Time
            Example: `1546938224`
  - **NitrogenSports** (object)
    Nitrogensports
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938185, '1_2': 1546937256, '1_3': 1546937256}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938185, '1_2': 1546937256, '1_3': 1546937256}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938185`
      - **1_2** (integer)
        1 2
        Example: `1546937256`
      - **1_3** (integer)
        1 3
        Example: `1546937256`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '857049', 'home_od': '2.127', 'draw_od': '3.680', 'away_od': '3.449', 'ss':`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '857049', 'home_od': '2.127', 'draw_od': '3.680', 'away_od': '3.449', 'ss': None, 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '857049', 'home_od': '2.127', 'draw_od': '3.680', 'away_od': '3.449', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `857049`
          - **home_od** (string)
            Home Od
            Example: `2.127`
          - **draw_od** (string)
            Draw Od
            Example: `3.680`
          - **away_od** (string)
            Away Od
            Example: `3.449`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546905662`
        - **1_2** (object)
          1 2
          Example: `{'id': '691706', 'home_od': '2.122', 'handicap': '-0.50', 'away_od': '1.785', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `691706`
          - **home_od** (string)
            Home Od
            Example: `2.122`
          - **handicap** (string)
            Handicap
            Example: `-0.50`
          - **away_od** (string)
            Away Od
            Example: `1.785`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546905663`
        - **1_3** (object)
          1 3
          Example: `{'id': '572300', 'over_od': '2.073', 'handicap': '3.00', 'under_od': '1.798', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `572300`
          - **over_od** (string)
            Over Od
            Example: `2.073`
          - **handicap** (string)
            Handicap
            Example: `3.00`
          - **under_od** (string)
            Under Od
            Example: `1.798`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546905663`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '857319', 'home_od': '1.988', 'draw_od': '3.860', 'away_od': '3.727', 'ss': None, 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '857319', 'home_od': '1.988', 'draw_od': '3.860', 'away_od': '3.727', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `857319`
          - **home_od** (string)
            Home Od
            Example: `1.988`
          - **draw_od** (string)
            Draw Od
            Example: `3.860`
          - **away_od** (string)
            Away Od
            Example: `3.727`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937256`
        - **1_2** (object)
          1 2
          Example: `{'id': '691952', 'home_od': '1.984', 'handicap': '-0.50', 'away_od': '1.901', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `691952`
          - **home_od** (string)
            Home Od
            Example: `1.984`
          - **handicap** (string)
            Handicap
            Example: `-0.50`
          - **away_od** (string)
            Away Od
            Example: `1.901`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937256`
        - **1_3** (object)
          1 3
          Example: `{'id': '572504', 'over_od': '2.033', 'handicap': '3.00', 'under_od': '1.839', 'ss': None, 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `572504`
          - **over_od** (string)
            Over Od
            Example: `2.033`
          - **handicap** (string)
            Handicap
            Example: `3.00`
          - **under_od** (string)
            Under Od
            Example: `1.839`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937256`
  - **Winner** (object)
    Winner
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226}, 'odds': {'start': {'1_1': {'id': '2567518'`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '2567518', 'home_od': '2.05', 'draw_od': '3.50', 'away_od': '3.45', 'ss': N`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '2567518', 'home_od': '2.05', 'draw_od': '3.50', 'away_od': '3.45', 'ss': None, 'time`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '2567518', 'home_od': '2.05', 'draw_od': '3.50', 'away_od': '3.45', 'ss': None, 'time_str': N`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2567518`
          - **home_od** (string)
            Home Od
            Example: `2.05`
          - **draw_od** (string)
            Draw Od
            Example: `3.50`
          - **away_od** (string)
            Away Od
            Example: `3.45`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546790309`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '2573290', 'home_od': '2.05', 'draw_od': '3.55', 'away_od': '3.40', 'ss': '0-0', 'tim`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '2573290', 'home_od': '2.05', 'draw_od': '3.55', 'away_od': '3.40', 'ss': '0-0', 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `2573290`
          - **home_od** (string)
            Home Od
            Example: `2.05`
          - **draw_od** (string)
            Draw Od
            Example: `3.55`
          - **away_od** (string)
            Away Od
            Example: `3.40`
          - **ss** (string)
            Current score
            Example: `0-0`
          - **time_str** (string)
            Time Str
            Example: `8:03`
          - **add_time** (string)
            Add Time
            Example: `1546938226`
  - **BetRegal** (object)
    Betregal
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546938226, '1_2': 1546938226, '1_3': 1546938226}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546938226, '1_2': 1546938226, '1_3': 1546938226}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546938226`
      - **1_2** (integer)
        1 2
        Example: `1546938226`
      - **1_3** (integer)
        1 3
        Example: `1546938226`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '575646', 'home_od': '2.010', 'draw_od': '3.700', 'away_od': '3.120', 'ss':`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '575646', 'home_od': '2.010', 'draw_od': '3.700', 'away_od': '3.120', 'ss': '0:0', 't`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '575646', 'home_od': '2.010', 'draw_od': '3.700', 'away_od': '3.120', 'ss': '0:0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `575646`
          - **home_od** (string)
            Home Od
            Example: `2.010`
          - **draw_od** (string)
            Draw Od
            Example: `3.700`
          - **away_od** (string)
            Away Od
            Example: `3.120`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937027`
        - **1_2** (object)
          1 2
          Example: `{'id': '468732', 'home_od': '1.541', 'handicap': '0', 'away_od': '2.400', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `468732`
          - **home_od** (string)
            Home Od
            Example: `1.541`
          - **handicap** (string)
            Handicap
            Example: `0`
          - **away_od** (string)
            Away Od
            Example: `2.400`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546765487`
        - **1_3** (object)
          1 3
          Example: `{'id': '918454', 'over_od': '1.787', 'handicap': '2.75', 'under_od': '2.030', 'ss': '0:0', 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `918454`
          - **over_od** (string)
            Over Od
            Example: `1.787`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `2.030`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546937027`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '575865', 'home_od': '1.962', 'draw_od': '3.640', 'away_od': '3.300', 'ss': '0:0', 't`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '575865', 'home_od': '1.962', 'draw_od': '3.640', 'away_od': '3.300', 'ss': '0:0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `575865`
          - **home_od** (string)
            Home Od
            Example: `1.962`
          - **draw_od** (string)
            Draw Od
            Example: `3.640`
          - **away_od** (string)
            Away Od
            Example: `3.300`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `07:36`
          - **add_time** (string)
            Add Time
            Example: `1546938193`
        - **1_2** (object)
          1 2
          Example: `{'id': '521941', 'home_od': '2.000', 'handicap': '-0.5', 'away_od': '1.813', 'ss': '0:0', 'time_str'`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `521941`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **handicap** (string)
            Handicap
            Example: `-0.5`
          - **away_od** (string)
            Away Od
            Example: `1.813`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `07:21`
          - **add_time** (string)
            Add Time
            Example: `1546938179`
        - **1_3** (object)
          1 3
          Example: `{'id': '918671', 'over_od': '1.901', 'handicap': '2.75', 'under_od': '1.901', 'ss': '0:0', 'time_str`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `918671`
          - **over_od** (string)
            Over Od
            Example: `1.901`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.901`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `05:35`
          - **add_time** (string)
            Add Time
            Example: `1546938072`
  - **SkyBet** (object)
    Skybet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546936239, '1_3': 1546936239}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546936239, '1_3': 1546936239}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546936239`
      - **1_3** (integer)
        1 3
        Example: `1546936239`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '574515', 'home_od': '2.000', 'draw_od': '3.400', 'away_od': '3.400', 'ss':`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '574515', 'home_od': '2.000', 'draw_od': '3.400', 'away_od': '3.400', 'ss': None, 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '574515', 'home_od': '2.000', 'draw_od': '3.400', 'away_od': '3.400', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `574515`
          - **home_od** (string)
            Home Od
            Example: `2.000`
          - **draw_od** (string)
            Draw Od
            Example: `3.400`
          - **away_od** (string)
            Away Od
            Example: `3.400`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546691856`
        - **1_3** (object)
          1 3
          Example: `{'id': '303539', 'over_od': '1.667', 'handicap': '2.5', 'under_od': '2.100', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `303539`
          - **over_od** (string)
            Over Od
            Example: `1.667`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.100`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546691856`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '579068', 'home_od': '1.950', 'draw_od': '3.500', 'away_od': '3.400', 'ss': None, 'ti`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '579068', 'home_od': '1.950', 'draw_od': '3.500', 'away_od': '3.400', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `579068`
          - **home_od** (string)
            Home Od
            Example: `1.950`
          - **draw_od** (string)
            Draw Od
            Example: `3.500`
          - **away_od** (string)
            Away Od
            Example: `3.400`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546929911`
        - **1_3** (object)
          1 3
          Example: `{'id': '305286', 'over_od': '1.615', 'handicap': '2.5', 'under_od': '2.200', 'ss': None, 'time_str':`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `305286`
          - **over_od** (string)
            Over Od
            Example: `1.615`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `2.200`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546854644`
  - **MarsBet** (object)
    Marsbet
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546936124, '1_2': 1546936124, '1_3': 1546936124}, 'odd`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546936124, '1_2': 1546936124, '1_3': 1546936124}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546936124`
      - **1_2** (integer)
        1 2
        Example: `1546936124`
      - **1_3** (integer)
        1 3
        Example: `1546936124`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '817894', 'home_od': '3.46', 'draw_od': '3.4', 'away_od': '2.01', 'ss': Non`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '817894', 'home_od': '3.46', 'draw_od': '3.4', 'away_od': '2.01', 'ss': None, 'time_s`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '817894', 'home_od': '3.46', 'draw_od': '3.4', 'away_od': '2.01', 'ss': None, 'time_str': Non`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `817894`
          - **home_od** (string)
            Home Od
            Example: `3.46`
          - **draw_od** (string)
            Draw Od
            Example: `3.4`
          - **away_od** (string)
            Away Od
            Example: `2.01`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546686414`
        - **1_2** (object)
          1 2
          Example: `{'id': '606246', 'home_od': '1.76', 'handicap': '0.5', 'away_od': '1.99', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `606246`
          - **home_od** (string)
            Home Od
            Example: `1.76`
          - **handicap** (string)
            Handicap
            Example: `0.5`
          - **away_od** (string)
            Away Od
            Example: `1.99`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546686414`
        - **1_3** (object)
          1 3
          Example: `{'id': '480356', 'over_od': '1.83', 'handicap': '2.75', 'under_od': '1.91', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `480356`
          - **over_od** (string)
            Over Od
            Example: `1.83`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.91`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546686414`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '823822', 'home_od': '3.33', 'draw_od': '3.49', 'away_od': '2.03', 'ss': None, 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '823822', 'home_od': '3.33', 'draw_od': '3.49', 'away_od': '2.03', 'ss': None, 'time_str': No`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `823822`
          - **home_od** (string)
            Home Od
            Example: `3.33`
          - **draw_od** (string)
            Draw Od
            Example: `3.49`
          - **away_od** (string)
            Away Od
            Example: `2.03`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936124`
        - **1_2** (object)
          1 2
          Example: `{'id': '611901', 'home_od': '1.75', 'handicap': '0.5', 'away_od': '2', 'ss': None, 'time_str': None,`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `611901`
          - **home_od** (string)
            Home Od
            Example: `1.75`
          - **handicap** (string)
            Handicap
            Example: `0.5`
          - **away_od** (string)
            Away Od
            Example: `2`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936124`
        - **1_3** (object)
          1 3
          Example: `{'id': '484512', 'over_od': '1.99', 'handicap': '2.75', 'under_od': '1.76', 'ss': None, 'time_str': `
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `484512`
          - **over_od** (string)
            Over Od
            Example: `1.99`
          - **handicap** (string)
            Handicap
            Example: `2.75`
          - **under_od** (string)
            Under Od
            Example: `1.76`
          - **ss** (unknown)
            Current score
          - **time_str** (unknown)
            Time Str
          - **add_time** (string)
            Add Time
            Example: `1546936124`
  - **CashPoint** (object)
    Cashpoint
    Example: `{'matching_dir': '1', 'odds_update': {'1_1': 1546937936, '1_3': 1546938154}, 'odds': {'start': {'1_1`
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{'1_1': 1546937936, '1_3': 1546938154}`
      Nested fields:
      - **1_1** (integer)
        1 1
        Example: `1546937936`
      - **1_3** (integer)
        1 3
        Example: `1546938154`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': {'id': '29041', 'home_od': '1.88', 'draw_od': '3.50', 'away_od': '3.50', 'ss': '0:`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': {'id': '29041', 'home_od': '1.88', 'draw_od': '3.50', 'away_od': '3.50', 'ss': '0:0', 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '29041', 'home_od': '1.88', 'draw_od': '3.50', 'away_od': '3.50', 'ss': '0:0', 'time_str': '4`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `29041`
          - **home_od** (string)
            Home Od
            Example: `1.88`
          - **draw_od** (string)
            Draw Od
            Example: `3.50`
          - **away_od** (string)
            Away Od
            Example: `3.50`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `4`
          - **add_time** (string)
            Add Time
            Example: `1546937936`
        - **1_3** (object)
          1 3
          Example: `{'id': '54624', 'over_od': '2.50', 'handicap': '3.5', 'under_od': '1.43', 'ss': '0:0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `54624`
          - **over_od** (string)
            Over Od
            Example: `2.50`
          - **handicap** (string)
            Handicap
            Example: `3.5`
          - **under_od** (string)
            Under Od
            Example: `1.43`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `2`
          - **add_time** (string)
            Add Time
            Example: `1546937813`
      - **end** (object)
        End
        Example: `{'1_1': {'id': '29041', 'home_od': '1.88', 'draw_od': '3.50', 'away_od': '3.50', 'ss': '0:0', 'time_`
        Nested fields:
        - **1_1** (object)
          1 1
          Example: `{'id': '29041', 'home_od': '1.88', 'draw_od': '3.50', 'away_od': '3.50', 'ss': '0:0', 'time_str': '4`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `29041`
          - **home_od** (string)
            Home Od
            Example: `1.88`
          - **draw_od** (string)
            Draw Od
            Example: `3.50`
          - **away_od** (string)
            Away Od
            Example: `3.50`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `4`
          - **add_time** (string)
            Add Time
            Example: `1546937936`
        - **1_3** (object)
          1 3
          Example: `{'id': '54636', 'over_od': '1.68', 'handicap': '2.5', 'under_od': '1.98', 'ss': '0:0', 'time_str': '`
          Nested fields:
          - **id** (string)
            Unique identifier
            Example: `54636`
          - **over_od** (string)
            Over Od
            Example: `1.68`
          - **handicap** (string)
            Handicap
            Example: `2.5`
          - **under_od** (string)
            Under Od
            Example: `1.98`
          - **ss** (string)
            Current score
            Example: `0:0`
          - **time_str** (string)
            Time Str
            Example: `7`
          - **add_time** (string)
            Add Time
            Example: `1546938154`
  - **VBet** (object)
    Vbet
    Example: `{'matching_dir': '1', 'odds_update': {}, 'odds': {'start': {'1_1': None, '1_2': None, '1_3': None}, `
    Nested fields:
    - **matching_dir** (string)
      Matching Dir
      Example: `1`
    - **odds_update** (object)
      Odds Update
      Example: `{}`
    - **odds** (object)
      Odds
      Example: `{'start': {'1_1': None, '1_2': None, '1_3': None}, 'end': {'1_1': None, '1_2': None, '1_3': None}}`
      Nested fields:
      - **start** (object)
        Start
        Example: `{'1_1': None, '1_2': None, '1_3': None}`
        Nested fields:
        - **1_1** (unknown)
          1 1
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3
      - **end** (object)
        End
        Example: `{'1_1': None, '1_2': None, '1_3': None}`
        Nested fields:
        - **1_1** (unknown)
          1 1
        - **1_2** (unknown)
          1 2
        - **1_3** (unknown)
          1 3

---

## Event Lineup

Event Lineup data

### Structure

```json

{
  "success": 1,
  "results": {
    "home": {
      "formation": "4-3-3",
      "startinglineup": [
        {
          "player": {
            "id": "232422",
            "name": "Kepa Arrizabalaga",
            "cc": "es"
          },
          "shirtnumber": "1",
          "pos": "Guard"
        },
        {
          "player": {
            "id": "21555",
            "name": "Cesar Azpilicueta",
            "cc": "es"
          },
          "shirtnumber": "28",
          "pos": "Defender"
        },
        {
          "player": {
            "id": "186795",
            "name": "Andreas Christensen",
            "cc": "dk"
          },
          "shirtnumber": "4",
          "pos": "Defender"
        },
        {
          "player": {
            "id": "142622",
            "name": "Antonio Rudiger",
            "cc": "de"
          },
          "shirtnumber": "2",
          "pos": "Defender"
        },
        {
          "player": {
            "id": "69408",
            "name":

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (object)
  Results
  Example: `{'home': {'formation': '4-3-3', 'startinglineup': [{'player': {'id': '232422', 'name': 'Kepa Arrizab`
  Nested fields:
  - **home** (object)
    Home team information
    Example: `{'formation': '4-3-3', 'startinglineup': [{'player': {'id': '232422', 'name': 'Kepa Arrizabalaga', '`
    Nested fields:
    - **formation** (string)
      Formation
      Example: `4-3-3`
    - **startinglineup** (array[object])
      Startinglineup
      Example: `{'player': {'id': '232422', 'name': 'Kepa Arrizabalaga', 'cc': 'es'}, 'shirtnumber': '1', 'pos': 'Gu`
      Nested fields:
      - **player** (object)
        Player
        Example: `{'id': '232422', 'name': 'Kepa Arrizabalaga', 'cc': 'es'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `232422`
        - **name** (string)
          Display name
          Example: `Kepa Arrizabalaga`
        - **cc** (string)
          Country code
          Example: `es`
      - **shirtnumber** (string)
        Shirtnumber
        Example: `1`
      - **pos** (string)
        Pos
        Example: `Guard`
    - **substitutes** (array[object])
      Substitutes
      Example: `{'player': {'id': '139227', 'name': 'Kurt Zouma', 'cc': 'fr'}, 'shirtnumber': '15', 'pos': 'Defender`
      Nested fields:
      - **player** (object)
        Player
        Example: `{'id': '139227', 'name': 'Kurt Zouma', 'cc': 'fr'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `139227`
        - **name** (string)
          Display name
          Example: `Kurt Zouma`
        - **cc** (string)
          Country code
          Example: `fr`
      - **shirtnumber** (string)
        Shirtnumber
        Example: `15`
      - **pos** (string)
        Pos
        Example: `Defender`
  - **away** (object)
    Away team information
    Example: `{'formation': '4-3-3', 'startinglineup': [{'player': {'id': '254491', 'name': 'Ederson', 'cc': 'br'}`
    Nested fields:
    - **formation** (string)
      Formation
      Example: `4-3-3`
    - **startinglineup** (array[object])
      Startinglineup
      Example: `{'player': {'id': '254491', 'name': 'Ederson', 'cc': 'br'}, 'shirtnumber': '31', 'pos': 'Guard'}`
      Nested fields:
      - **player** (object)
        Player
        Example: `{'id': '254491', 'name': 'Ederson', 'cc': 'br'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `254491`
        - **name** (string)
          Display name
          Example: `Ederson`
        - **cc** (string)
          Country code
          Example: `br`
      - **shirtnumber** (string)
        Shirtnumber
        Example: `31`
      - **pos** (string)
        Pos
        Example: `Guard`
    - **substitutes** (array[object])
      Substitutes
      Example: `{'player': {'id': '1299448', 'name': 'Thomas Doyle', 'cc': 'gb'}, 'shirtnumber': '69', 'pos': 'Midfi`
      Nested fields:
      - **player** (object)
        Player
        Example: `{'id': '1299448', 'name': 'Thomas Doyle', 'cc': 'gb'}`
        Nested fields:
        - **id** (string)
          Unique identifier
          Example: `1299448`
        - **name** (string)
          Display name
          Example: `Thomas Doyle`
        - **cc** (string)
          Country code
          Example: `gb`
      - **shirtnumber** (string)
        Shirtnumber
        Example: `69`
      - **pos** (string)
        Pos
        Example: `Midfielder`

---

## Merge History

Merge History data

### Structure

```json

{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 100,
    "total": 23467
  },
  "results": [
    {
      "from_id": "887111",
      "to_id": "887142",
      "created_at": "1534817422"
    },
    {
      "from_id": "862026",
      "to_id": "886849",
      "created_at": "1534817422"
    },
    {
      "from_id": "887112",
      "to_id": "887143",
      "created_at": "1534817417"
    },
    {
      "from_id": "877283",
      "to_id": "887058",
      "created_at": "1534813823"
    },
    {
      "from_id": "884111",
      "to_id": "886430",
      "created_at": "1534812491"
    },
    {
      "from_id": "862383",
      "to_id": "864529",
      "created_at": "1534810222"
    },
    {
      "from_id": "356192",
      "to_id": "505415",
      "created_at": "1534785071"
    },
    {
      "from_id": "105303",
      "to_id": "118120",
      "created_at": "1534785071"
    },
    {
      "from_id": "784621",
      "to_id": "886578",
      "created_at": "1534770642"
    },
    {
      

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **pager** (object)
  Pager
  Example: `{'page': 1, 'per_page': 100, 'total': 23467}`
  Nested fields:
  - **page** (integer)
    Page
    Example: `1`
  - **per_page** (integer)
    Per Page
    Example: `100`
  - **total** (integer)
    Total
    Example: `23467`
- **results** (array[object])
  Results
  Example: `{'from_id': '887111', 'to_id': '887142', 'created_at': '1534817422'}`
  Nested fields:
  - **from_id** (string)
    From Id
    Example: `887111`
  - **to_id** (string)
    To Id
    Example: `887142`
  - **created_at** (string)
    Created At
    Example: `1534817422`

---

## Ended

Ended data

### Structure

```json

{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 50,
    "total": 1381633
  },
  "results": [
    {
      "id": "3950619",
      "sport_id": "1",
      "time": "1633269600",
      "time_status": "5",
      "league": {
        "id": "69",
        "name": "Spain Tercera Group 12",
        "cc": "es"
      },
      "home": {
        "id": "57728",
        "name": "Tenisca",
        "image_id": "34755",
        "cc": "es"
      },
      "away": {
        "id": "6285",
        "name": "CD Marino",
        "image_id": "77395",
        "cc": "es"
      },
      "ss": null
    },
    {
      "id": "4073920",
      "sport_id": "1",
      "time": "1633266000",
      "time_status": "4",
      "league": {
        "id": "605",
        "name": "Italy Serie D",
        "cc": "it"
      },
      "home": {
        "id": "579136",
        "name": "Cittanova Interpiana",
        "image_id": "834562",
        "cc": "it"
      },
      "away": {
        "id": "831",
        "name": "Trapani",


... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **pager** (object)
  Pager
  Example: `{'page': 1, 'per_page': 50, 'total': 1381633}`
  Nested fields:
  - **page** (integer)
    Page
    Example: `1`
  - **per_page** (integer)
    Per Page
    Example: `50`
  - **total** (integer)
    Total
    Example: `1381633`
- **results** (array[object])
  Results
  Example: `{'id': '3950619', 'sport_id': '1', 'time': '1633269600', 'time_status': '5', 'league': {'id': '69', `
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `3950619`
  - **sport_id** (string)
    Sport identifier
    Example: `1`
  - **time** (string)
    Unix timestamp
    Example: `1633269600`
  - **time_status** (string)
    Status of the event (0=not started, 1=in play, 3=ended)
    Example: `5`
  - **league** (object)
    League information
    Example: `{'id': '69', 'name': 'Spain Tercera Group 12', 'cc': 'es'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `69`
    - **name** (string)
      Display name
      Example: `Spain Tercera Group 12`
    - **cc** (string)
      Country code
      Example: `es`
  - **home** (object)
    Home team information
    Example: `{'id': '57728', 'name': 'Tenisca', 'image_id': '34755', 'cc': 'es'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `57728`
    - **name** (string)
      Display name
      Example: `Tenisca`
    - **image_id** (string)
      ID of the team/player image
      Example: `34755`
    - **cc** (string)
      Country code
      Example: `es`
  - **away** (object)
    Away team information
    Example: `{'id': '6285', 'name': 'CD Marino', 'image_id': '77395', 'cc': 'es'}`
    Nested fields:
    - **id** (string)
      Unique identifier
      Example: `6285`
    - **name** (string)
      Display name
      Example: `CD Marino`
    - **image_id** (string)
      ID of the team/player image
      Example: `77395`
    - **cc** (string)
      Country code
      Example: `es`
  - **ss** (unknown)
    Current score

---

## Team

Team information and details

### Structure

```json

{
  "success": 1,
  "pager": {
    "page": 1,
    "per_page": 100,
    "total": 29084
  },
  "results": [
    {
      "id": "1",
      "name": "Dorados",
      "cc": "mx",
      "image_id": "5291",
      "has_squad": 1
    },
    {
      "id": "2",
      "name": "Coras Tepic",
      "cc": "mx",
      "image_id": "159944",
      "has_squad": 1
    },
    {
      "id": "3",
      "name": "Bankstown Berries",
      "cc": "au",
      "image_id": "0"
    },
    {
      "id": "4",
      "name": "St George",
      "cc": "et",
      "image_id": "94787"
    },
    {
      "id": "5",
      "name": "Fraser Park",
      "cc": "au",
      "image_id": "242396"
    },
    {
      "id": "6",
      "name": "Bankstown City Lions FC",
      "cc": "au",
      "image_id": "171998"
    },
    {
      "id": "7",
      "name": "Marconi Stallions",
      "cc": "au",
      "image_id": "2941",
      "has_squad": 1
    },
    {
      "id": "8",
      "name": "Spirit FC",
      "cc": "au",
      "image_id": "2943"

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **pager** (object)
  Pager
  Example: `{'page': 1, 'per_page': 100, 'total': 29084}`
  Nested fields:
  - **page** (integer)
    Page
    Example: `1`
  - **per_page** (integer)
    Per Page
    Example: `100`
  - **total** (integer)
    Total
    Example: `29084`
- **results** (array[object])
  Results
  Example: `{'id': '1', 'name': 'Dorados', 'cc': 'mx', 'image_id': '5291', 'has_squad': 1}`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `1`
  - **name** (string)
    Display name
    Example: `Dorados`
  - **cc** (string)
    Country code
    Example: `mx`
  - **image_id** (string)
    ID of the team/player image
    Example: `5291`
  - **has_squad** (integer)
    Has Squad
    Example: `1`

---

## Tennis Ranking

Tennis Ranking data

### Structure

```json

{
  "success": 1,
  "results": [
    {
      "id": "4140",
      "name": "Rafael Nadal",
      "cc": "es",
      "country": "Spain",
      "ranking": "1",
      "points": "9310"
    },
    {
      "id": "70618",
      "name": "Roger Federer",
      "cc": "ch",
      "country": "Switzerland",
      "ranking": "2",
      "points": "7080"
    },
    {
      "id": "2673",
      "name": "Alexander Zverev",
      "cc": "de",
      "country": "Germany",
      "ranking": "3",
      "points": "5665"
    },
    {
      "id": "3126",
      "name": "Juan Martin Del Potro",
      "cc": "ar",
      "country": "Argentina",
      "ranking": "4",
      "points": "5395"
    },
    {
      "id": "3564",
      "name": "Kevin Anderson",
      "cc": "za",
      "country": "South Africa",
      "ranking": "5",
      "points": "4655"
    },
    {
      "id": "2666",
      "name": "Grigor Dimitrov",
      "cc": "bg",
      "country": "Bulgaria",
      "ranking": "6",
      "points": "4610"
    },
    {
      "

... (truncated)
```

### Fields

- **success** (integer)
  API response status
  Example: `1`
- **results** (array[object])
  Results
  Example: `{'id': '4140', 'name': 'Rafael Nadal', 'cc': 'es', 'country': 'Spain', 'ranking': '1', 'points': '93`
  Nested fields:
  - **id** (string)
    Unique identifier
    Example: `4140`
  - **name** (string)
    Display name
    Example: `Rafael Nadal`
  - **cc** (string)
    Country code
    Example: `es`
  - **country** (string)
    Country
    Example: `Spain`
  - **ranking** (string)
    Ranking
    Example: `1`
  - **points** (string)
    Points
    Example: `9310`

---

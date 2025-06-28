--- Read Workflow ---
┌────────────────────────────┐
│  You ask a question:       │
│  "Do I have any meetings?" │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Cursor triggers MCP tool   │
│ from `.cursor/tools.json`: │
│→ `calendar_checker_run.py` │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Script parses date param  │
│  e.g., --date=tomorrow     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  `check_upcoming_meetings()`│
│  in `calendar_checker.py`   │
│  is called                  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  `auth.py` gets credentials│
│  (token.json or OAuth flow)│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Google Calendar API        │
│ → fetches events           │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Output is printed to      │
│  console by the script     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Cursor displays the       │
│  script's text output      │
└────────────────────────────┘

--- Create Workflow ---

┌────────────────────────────┐
│  You ask to create a meeting:│
│ "create a meeting..."      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Cursor triggers MCP tool   │
│→ `calendar_checker_run.py` │
│   with --create flag       │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Script parses --summary,   │
│ --start, --end arguments   │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  `create_event()` in        │
│ `calendar_checker.py`      │
│  is called                  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  `auth.py` gets credentials│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Google Calendar API        │
│ → inserts new event        │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Confirmation is printed    │
│ to console                 │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Cursor displays the       │
│  confirmation message      │
└────────────────────────────┘

--- Delete Workflow ---

┌────────────────────────────┐
│  You ask to delete a meeting:│
│ "delete meeting with ID..."│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Cursor triggers MCP tool   │
│→ `calendar_checker_run.py` │
│   with --delete flag & ID  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Script parses --delete     │
│ argument with event ID     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  `delete_event()` in        │
│ `calendar_checker.py`      │
│  is called                  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  `auth.py` gets credentials│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Google Calendar API        │
│ → deletes event by ID      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Confirmation is printed    │
│ to console                 │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Cursor displays the       │
│  confirmation message      │
└────────────────────────────┘

--- Weather Workflow ---

┌────────────────────────────┐
│  You ask for the weather:  │
│  "What's the weather in X?"│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Cursor triggers MCP tool   │
│ from `.cursor/tools.json`: │
│→ `weather_cli.py`          │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Script parses --city arg  │
│  (e.g., --city=Dhaka)      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  API key loaded from .env  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  OpenWeatherMap API        │
│  → fetches weather         │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Output is printed to      │
│  console by the script     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Cursor displays the       │
│  script's text output      │
└────────────────────────────┘

--- Stock Workflow ---

┌────────────────────────────┐
│  You ask for a stock price:│
│  "What's the price of X?"  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Cursor triggers MCP tool   │
│ from `.cursor/tools.json`: │
│→ `stock_cli.py`            │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Script parses --symbol arg│
│  (e.g., --symbol=SMCI)     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  yfinance fetches stock    │
│  data for the symbol       │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Output is printed to      │
│  console by the script     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Cursor displays the       │
│  script's text output      │
└────────────────────────────┘

--- Terminal-Based Workflow ---

┌────────────────────────────┐
│  You want to check:        │
│  - AI news                 │
│  - Meetings                │
│  - Stocks                  │
│  - Weather                 │
│  - Email                   │
│  - Tasks                   │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Run the relevant script   │
│  in your terminal:         │
│                            │
│  python ai_news_scraper.py │
│  python calendar_checker_run.py [options] │
│  python stock_cli.py --symbol=SMCI        │
│  python weather_cli.py --city=Antwerp     │
│  python email_checker.py                  │
│  python tasks_manager.py                  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Script fetches data from  │
│  the relevant API/service  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Output is printed to      │
│  your terminal             │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  You view the results      │
│  and take action as needed │
└────────────────────────────┘

---

# No mobile app or frontend is required. All workflows are handled via terminal-based Python scripts.

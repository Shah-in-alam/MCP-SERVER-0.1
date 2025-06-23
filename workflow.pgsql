┌────────────────────────────┐
│  You ask a question:       │
│  "Do I have any meetings?" │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Cursor triggers MCP tool   │
│ from `.cursor/tools.json`: │
│  → `calendar_checker_run.py` │
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
│  script’s text output      │
└────────────────────────────┘

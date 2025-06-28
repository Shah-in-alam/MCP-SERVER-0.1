# MCP-SERVER-0.1

A terminal-based productivity suite for managing AI news, meetings, stocks, weather, email, and tasks using Python scripts.

## Features
- **AI News:** Fetches the latest AI news headlines from Google News RSS.
- **Meetings:** Check, create, and delete Google Calendar meetings.
- **Stocks:** Get the latest stock prices using yfinance.
- **Weather:** Check the current weather for any city using OpenWeatherMap.
- **Email:** View unread emails from Gmail.
- **Tasks:** Manage your Google Tasks.

## Requirements
- Python 3.8+
- All dependencies in `requirements.txt`

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Set up Google API credentials** for Calendar, Gmail, and Tasks:
   - Download your `credentials.json` from Google Cloud Console and place it in the project root.
   - The first time you run a script that uses Google APIs, it will prompt you to authenticate and create a `token.json` file.
4. **(Optional) Set up environment variables:**
   - For weather, create a `.env` file with:
     ```
     OPENWEATHER_API_KEY=your_openweather_api_key
     ```

## Usage
Run any script directly from your terminal:

- **AI News:**
  ```
  python ai_news_scraper.py
  ```
- **Meetings:**
  ```
  python calendar_checker_run.py --date today
  python calendar_checker_run.py --create --summary "Meeting" --start "2025-07-01 16:00" --end "2025-07-01 17:00"
  python calendar_checker_run.py --delete <event_id>
  ```
- **Stocks:**
  ```
  python stock_cli.py --symbol=SMCI
  ```
- **Weather:**
  ```
  python weather_cli.py --city=Antwerp
  ```
- **Email:**
  ```
  python email_checker.py
  ```
- **Tasks:**
  ```
  python tasks_manager.py
  ```

## Notes
- All output is printed to your terminal.
- For Google APIs, make sure the required APIs are enabled in your Google Cloud project.
- For weather, sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.

## License
MIT 
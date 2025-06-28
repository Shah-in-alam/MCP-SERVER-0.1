import yfinance as yf
import argparse

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    if data.empty:
        print(f"No data found for symbol: {symbol}")
        return
    last_quote = data.iloc[-1]
    print(f"\nStock info for {symbol.upper()}:")
    print(f"  Date: {last_quote.name.date()}")
    print(f"  Open: {last_quote['Open']}")
    print(f"  High: {last_quote['High']}")
    print(f"  Low: {last_quote['Low']}")
    print(f"  Close: {last_quote['Close']}")
    print(f"  Volume: {int(last_quote['Volume'])}\n")

def main():
    parser = argparse.ArgumentParser(description="Get the latest stock price and info.")
    parser.add_argument('--symbol', type=str, help='Stock symbol, e.g., AAPL, MSFT, TSLA')
    args = parser.parse_args()
    symbol = args.symbol or input("Enter stock symbol: ").strip()
    get_stock_info(symbol)

if __name__ == "__main__":
    main() 
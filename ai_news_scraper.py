import requests
from bs4 import BeautifulSoup

GOOGLE_NEWS_RSS = 'https://news.google.com/rss/search?q=artificial+intelligence'

def fetch_ai_news():
    response = requests.get(GOOGLE_NEWS_RSS)
    if response.status_code != 200:
        print(f'Failed to fetch news: {response.status_code}')
        return
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    if not items:
        print('No AI news headlines found.')
        return
    print('Recent AI News Headlines (via Google News RSS):\n')
    for i, item in enumerate(items[:10], 1):
        title = item.title.get_text(strip=True)
        link = item.link.get_text(strip=True)
        print(f"{i}. {title}\n   {link}\n")

if __name__ == "__main__":
    fetch_ai_news() 
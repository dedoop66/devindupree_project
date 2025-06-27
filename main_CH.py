import feedparser
import urllib.parse  # to URL proof the search term

def get_news_headlines(query):
    safe_query = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={safe_query}"
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries]

if __name__ == "__main__":
    topic = "Taylor Swift"
    print(f"Fetching news about: {topic}")
    headlines = get_news_headlines(topic)
    for h in headlines:
        print("-", h)
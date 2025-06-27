import feedparser

def get_news_headlines(query):
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}"
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries]

if __name__ == "__main__":
    topic = "Taylor Swift"
    print(f"Fetching news about: {topic}")
    headlines = get_news_headlines(topic)
    for h in headlines:
        print("-", h)
General Description of the Project
This project will explore how public sentiment around individuals changes over time based on media coverage, using Google News headlines as the data source. The application will let a user enter one or more names (e.g., public figures, politicians, celebrities) and retrieve the most recent 100 headlines for each person using the Google News RSS feed. These headlines will then be analyzed for sentiment and visualized over time.
This version relies on publicly available and consistent RSS feeds, ensuring that data is live, accessible, and safe to use. Sentiment will be scored with standard text analysis tools like TextBlob or VADER, and the results will be shown on a simple line chart that shows positive vs. negative sentiment trends over time.
This version will run from a command line interface (CLI) or a basic local web interface using Flask. The goal of this project is not to predict public opinion but to give users a way to visualize the emotional tone of public news coverage around the people they're interested in.
Future enhancements could involve filtering by news source, comparing sentiment across people, or packaging the tool as an API that other projects could query remotely.

Task Vignettes
1. Entering Names
Jess wants to see how the tone of news coverage about Taylor Swift has changed in the past week. She opens the app and types "Taylor Swift" into the input box and clicks "Submit." The app uses the Google News RSS feed for that query, fetches the 100 most recent headlines, and displays a loading message.
Technical Details:
User input will be a single name or list of names.
Query constructed like: https://news.google.com/rss/search?q="Taylor+Swift"
Feed parsed using feedparser, storing headlines and publication dates.
2. Sentiment Processing
Behind the scenes, each headline is run through a sentiment analyzer. Each result is tagged with a sentiment polarity score from -1 to 1. Jess doesn’t see this step, but it determines what’s shown on the chart.
Technical Details:
Sentiment calculated with TextBlob or VADER (depending on performance).
Results stored in a list of dictionaries or pandas DataFrame: [{date, title, score}, ...]
3. Visualizing the Sentiment
A chart appears with the x-axis as headline date and y-axis as sentiment score. Jess sees a line graph that dips below zero for negative news and rises above for positive headlines. She can hover over a point to read the headline that generated that sentiment.
Technical Details:
Matplotlib or Plotly used for charting.
Optional: second line on the chart if Jess enters a second person (e.g., "Taylor Swift, Kanye West") for comparison.

Technical Flow
Core Blocks:
User Input Handler (CLI or Web UI)
Google News RSS Query (construct and fetch feeds)
Feed Parser (use feedparser to extract titles/dates)
Sentiment Analyzer (e.g., TextBlob or VADER)
Data Storage (temporary DataFrame for scoring and charting)
Visualizer (generates line chart showing sentiment trends)
Data Types:
Feed input: string (user query)
Headlines: list of dicts
Sentiment: float values (from -1 to 1)
Visual chart: PNG or embedded plot
User Interactions:
Input: Person name(s)
Output: Trend chart + optional headline list

Summary
This project lets users visualize the emotional tone of recent Google News coverage of public figures using sentiment analysis of headlines. It avoids API limits and scraping complexity while still offering dynamic and meaningful data. The tool will start as a CLI or local Flask app and has clear paths for expansion if desired.

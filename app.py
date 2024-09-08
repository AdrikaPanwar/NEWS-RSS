import feedparser
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

RSS_FEEDS = {
    'BBC News': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'CNN': 'http://rss.cnn.com/rss/cnn_topstories.rss',
    'Wired': 'https://www.wired.com/feed/rss',
    'TechCrunch': 'https://techcrunch.com/feed/',
}

def convert_to_datetime(t):
    """ Convert time.struct_time to datetime.datetime """
    return datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

@app.route('/')
def index():
    articles = []
    for source, feed in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(feed)
        for entry in parsed_feed.entries:
            if hasattr(entry, 'published_parsed'):
                published_date = convert_to_datetime(entry.published_parsed)
            else:
                published_date = datetime(1970, 1, 1)  # Default date for sorting
            articles.append((source, entry, published_date))
    
    articles.sort(key=lambda x: x[2], reverse=True)
    
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_articles = len(articles)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_articles = articles[start:end]
    
    total_pages = (total_articles + per_page - 1) // per_page
    
    return render_template('index.html', articles=[(source, entry) for source, entry, _ in paginated_articles], page=page, total_pages=total_pages)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    articles = []
    for source, feed in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(feed)
        for entry in parsed_feed.entries:
            if hasattr(entry, 'published_parsed'):
                published_date = convert_to_datetime(entry.published_parsed)
            else:
                published_date = datetime(1970, 1, 1)
            articles.append((source, entry, published_date))
    
    results = [article for article in articles if query.lower() in article[1].title.lower()]
    
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_articles = len(results)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_articles = results[start:end]
    
    total_pages = (total_articles + per_page - 1) // per_page
    
    return render_template('search_results.html', articles=[(source, entry) for source, entry, _ in paginated_articles], 
                           query=query, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)




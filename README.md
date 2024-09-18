# NEWS-RSS 📈📰
This project automates the collection and aggregation of news from major finance and technology websites using RSS feeds. Instead of manually visiting multiple sites daily, this system retrieves and displays the latest articles on a single page. The project focuses on finance and technology news but can be adapted for other interests by modifying the source websites.

## Setup Instructions: 🛠️
### ***Note*** = _I make this project on the Ubuntu(linux)_
***
1. ***Clone the Repository:***
   
   ``` git clone https://github.com/AdrikaPanwar/NEWS-RSS.git```
   ```cd NEWS-RSS```


3. ***Install the flask:***
 
    ``` sudo apt install python-3 flask``` 

    - if by chance this will not work use this command
   
   ``` sudo apt install python-3 flask python3-pip```

4. ***Install the Feedparser:***

   ```sudo apt install python3-feedparser```

5. ***Configure RSS Feeds:***

   - Ensure the RSS feed URLs for BBC News, CNN, Wired, and TechCrunch are correctly set in your script. Example configuration:
  ``` python
rss_feeds = {
    "BBC News": "http://feeds.bbci.co.uk/news/business/rss.xml",
    "CNN": "http://rss.cnn.com/rss/money_news_international.rss",
    "Wired": "https://www.wired.com/feed/rss",
    "TechCrunch": "https://techcrunch.com/feed/"
}
```

6. ***Run the Application:***

  ``` python app.py ```

  - Access the news aggregator through your web browser.

## How the Project Works 😄

   1. ***RSS Feed Parsing:***
      - Fetch RSS feeds from BBC News, CNN, Wired, and TechCrunch.
      - Parse the XML data to extract article titles, summaries, links, and publishing dates.

   2. ***Data Display:***
       - Aggregate the extracted data onto a single webpage or dashboard.
       - Users can view the latest headlines and summaries and follow links to full articles.

   3. ***Automation:***
        - The system periodically fetches updates from the RSS feeds and updates the displayed news automatically.
     
## Tools and Technologies Used 🐙

  - ***Python***:  Programming language for scripting and data processing.
    
  - ***feedparser***:  Python library for parsing RSS feeds.
    
  - ***datetime***:  Python module for handling and formatting dates.
    
  - ***HTML & Jinja5***:  Markup language for structuring web pages.
    
  - ***TailwindCSS***:  Style sheet language for designing and formatting the web page.
    
  - ***Flask***:  Web framework for building and serving the application.
    
  - ***Vercel***:  Deployment platform for hosting the web application.

## Now understand what is Feedparser? 📚 

***Feedparser*** _is a python library used for parsing and extracting information from RSS(Really simple Syndication) and atom feeds. These feeds are XML-based formats used to distribute and share content, such as news update, blog posts, and podcasts._

- It abstracts away the complexities of XML parsing and provides a straightforward API for accessing feed data.

## Then what is RSS?  📡

#### Let understand it in simple terms:

***RSS*** _( Really simple syndication or rich site summary) was created to address the need for a standardized way to distribute and consume web content efficiently._

- It allow websites to syndicate their content, making it easier for users to receive updates from multiple sources in one place.
- Instead of visiting each website individually, users can subscribe to an ***RSS Feed** and get updates delivered automatically

---

_But you can use the RSS Urls to subscribe to the RSS feeds using your preferred RSS reader or aggregator_.

## 📖 Website Presents ***RSS*** Readers are:-

- ***feedly***
- ***Inoreader***
- ***The Old Reader***
- ***Thunderbird etc***

  _yes! ***Thunderbird*** is also a RSS aggregator which is used for mail and RSS too in Linux OS_

  ## 📝 Note:

  If you want to contribute than feel free to contribute in it and yes apart from that If you raised any issue related to this project then I added a ```error.pdf``` too in this repository too; you can go through it and resolve the issues which I also faced during this project.

  #### ***Thanks to Read it!🙌😄***
    

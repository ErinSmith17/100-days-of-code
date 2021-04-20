#Parsing RSS feeds with Feedparser
import feedparser

FEED_FILE = "newreleases.xml"

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(entry.published + " - " + entry.title + ": " + entry.link)

#pull_xml.py uses the requests module to pull down the feed xml file for use in the xml parser script.
#This will result in just one call/request to the Steam webserver hosting this XML file.

import requests

URL = "http://store.steampowered.com/feeds/newreleases.xml"

if __name__ == "__main__":
	r = requests.get(URL)
	with open('newreleases.xml', 'wb') as f:
		f.write(r.content)
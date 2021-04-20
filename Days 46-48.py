#Web Scraping with BeautifulSoup4
import requests
import bs4

# URL of site we want to scrape
URL = "https://pybit.es/pages/projects.html"

def pull_site():
    raw_site_page = requests.get(URL) #Pull down the site.
    raw_site_page.raise_for_status()  #Confirm site was pulled. Error if not
    return raw_site_page

def scrape(site):
    header_list = []
    #Create BeautifulSoup object
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.projectHeader')

    for headers in html_header_list:
        header_list.append(headers.getText())
    for headers in header_list:
        print(headers)


if __name__ == "__main__":
    site = pull_site()
    scrape(site)

#shell commands for code
site = requests.get("https://pybit.es/pages/articles.html")
site.raise_for_status()
soup = bs4.BeautifulSoup(site.text, 'html.parser')

#Search for first <ul> tag on the page
soup.ul

#Search for all <ul> tags on the page
soup.find_all('ul')

#Search for all <ul> tags within the <main> tag
soup.main.ul

#Search for all <li> tags within the <main> tag and assign to variable
all_li = soup.main.find_all('li')

#Print out the text data for all of the <li> tags (titles of URLs)
for title in all_li:
    print(title.string)
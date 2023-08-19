import requests
from bs4 import BeautifulSoup

def get_parsed_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    else:
        return None

def extract_article_title(soup):
    title = soup.find('h1', id='1stHeading').text
    return title

def extract_article_text(soup):
    article_text = {}
    content = soup.find('div', class_='mw-content-ltr')
    
    current_heading = None
    for element in content.find_all(['h2', 'p']):
        if element.name == 'h2':
            current_heading = element.find('span', class_='mw-headline').text
            article_text[current_heading] = []
        elif element.name == 'p' and current_heading:
            article_text[current_heading].append(element.text)
    
    return article_text

# 1.4) Write a function to collect every link that redirects to another Wikipedia page
def collect_internal_links(soup):
    internal_links = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('/wiki/'):
            internal_links.append(link['href'])
    return internal_links

# 1.5) Wrap all the previous functions into a single function
def scrape_wikipedia_page(url):
    soup = get_parsed_html(url)
    if soup:
        title = extract_article_title(soup)
        article_text = extract_article_text(soup)
        internal_links = collect_internal_links(soup)
        
        return {
            'title': title,
            'article text': article_text,
            'internal links': internal_links
        }
    else:
        return None

# 1.6) Test the last function on a Wikipedia page of your choice
wikipedia_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
result = scrape_wikipedia_page(wikipedia_url)
if result:
    print("Title:", result['title'])
    print("Article Text:", result['article_text'])
    print("Internal Links:", result['internal_links'])
else:
    print("Failed to scrape the Wikipedia page.")

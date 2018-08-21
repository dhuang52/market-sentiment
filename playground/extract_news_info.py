from bs4 import BeautifulSoup
from urllib.request import urlopen
import json, pickle

error_counter = 0

def get_article_urls(news_response):
    news_urls = []
    for news in news_response:
        if news['status'] == 'ok':
            articles = news['articles']
            for article in articles:
                news_urls.append(article['url'])
        else:
            print('================ ERROR ERROR ERROR ERROR ERROR ERROR ================')
            print(news)
    return news_urls

def get_soup(url):
    global error_counter
    try:
        client = urlopen(url)
    except:
        print('an error occured')
        error_counter += 1
        return None
    if client.getcode() == 200:
        news_html = client.read()
        client.close()
    else:
        error_counter += 1
        client.close()
        return None
    return BeautifulSoup(news_html, 'html.parser')

with open('../data/iplg5ICngDWuMkLX_news_api.pickle', 'rb') as f:
    news_response = pickle.load(f)

print(len(news_response))

news_urls = get_article_urls(news_response)
for url in news_urls:
    soup = get_soup(url)
    if soup:
        i = 0
    else:
        print(url)
print(error_counter)

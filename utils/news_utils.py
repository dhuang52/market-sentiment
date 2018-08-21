import url_constants as urls
import credentials
import requests, json, math

# get a page of news articles covered by NewsAPI with the query and save the results
def get_top_results(query, sort_by, date, pages, page_number):
    format_url = (urls.news_api_everything, query, 'en', date, sort_by, pages, page_number)
    headers = {'Authorization': credentials.news_api_key}
    url = '{0[0]}?q={0[1]}&language={0[2]}&from={0[3]}&sortBy={0[4]}&pageSize={0[5]}&page={0[6]}'.format(format_url)
    news_request = requests.get(url, headers=headers)
    print (news_request.json())
    return news_request

# retrieve all articles and return list of response jsons for each page
# query: searching for
# sort_by: popularity, relevancy, publishedAt
# date_from: date to start querying from
# pages: max is 100, should always use 100 to minimize requests
def get_all_top_results(query, sort_by, date_from, pages):
    all_news = []

    news_response = get_top_results(query, 'popularity', date_from, '100', 1)
    news = news_response.json()
    all_news.append(news)

    # value of 100 should be stored as a constant
    total_requests = math.ceil(news['totalResults'] / 100)

    for request in range(2, total_requests+1):
        print('================ {0} ================'.format(request))
        news_response = get_top_results('snapchat', 'popularity', date_from, '100', request)
        news = news_response.json()
        all_news.append(news)
    return all_news

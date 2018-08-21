import credentials
import url_constants as urls
import requests, base64, json

def getBearerToken():
    bearer_token_credentials = '{0}:{1}'.format(credentials.twitter_consumer_key, credentials.twitter_consumer_secret)
    bearer_token_credentials_b64 = base64.b64encode(bytes(bearer_token_credentials, 'utf-8'))

    headers = {'Authorization': 'Basic {0}'.format(bearer_token_credentials_b64.decode('utf-8')), 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    payload = {'grant_type': 'client_credentials'}

    request = requests.post(urls.twitter_auth, data=payload, headers=headers)
    response_json = request.json()
    if response_json['token_type']:
        return response_json['access_token']
    return ''

# IMPROVE: add a body parameter so query is not fixed
def use_twitter_standard_search(twitter_header):
    return requests.get('{0}?q=snapchat%20stocks&filter:news&is:verified'.format(urls.twitter_search_2), headers=twitter_header)

def use_twitter_premium_search(twitter_payload, twitter_header):
    return requests.post(urls.twitter_search, data=twitter_payload, headers=twitter_header)

import sys
sys.path.append('./constants')
sys.path.append('./utils')

import url_constants as urls
import file_utils, twitter_utils
import requests, base64, json

# set to True when Premium Search requests are low
use_standard_search = True

def get_file_id():
    if use_standard_search:
        search_id = 'standard_search_twitter'
    else:
        search_id = 'premium_search_twitter'
    return search_id

def get_tweets(bearer_token):
    twitter_header = {'Authorization': 'Bearer {0}'.format(bearer_token)}
    twitter_payload = {'query': 'snapchat'}
    twitter_payload = json.dumps(twitter_payload)

    if use_standard_search:
        twitter_request = twitter_utils.use_twitter_standard_search(twitter_header)
    else:
        twitter_request = twitter_utils.use_twitter_premium_search(twitter_payload, twitter_header)

    twitter_response = twitter_request.json()
    print(twitter_response)
    return twitter_request

bearer_token = twitter_utils.getBearerToken()
print(bearer_token)
if bearer_token:
    twitter_response = get_tweets(bearer_token)

    search_id = get_file_id()
    text_id = file_utils.create_unique_id()
    file_id = '{0}_{1}.txt'.format(text_id, search_id)
    print(file_id)
    save_successful = file_utils.write_to_data_dir(file_id, twitter_response.text)

    if save_successful:
        print ('SAVE SUCCESSFUL')
    else:
        print('SAVE UNSUCCESSFUL')
else:
    print('COULD NOT GET BEARER TOKEN')

# ===========================================
    # print(len(twitter_response['statuses']))
    # for tweet in twitter_response['statuses']:
    #     print(tweet['text'])

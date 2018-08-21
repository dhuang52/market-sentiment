import json
from datetime import datetime, timedelta

"""
What this test has shown:
    Premium Search API returns 100 tweets everytime (unless restricted)
        All the 100 tweets are from today at different times, so we need
        to make multiple requests to the API in order to get a full week.
        Could be costly (in terms of the limit of 250 requests/mo)
    Chances are, a tweet will have pretty much 0 favorites and 0 retweets.
        This means Tweets would have a smaller weight compared to other
        other resources
    Certain tweets are useless, like: "follow me @username"
        Tweets like this should be filtered out
"""

# Check if a date is from a week ago
def check_week_ago(created_at):
    now = datetime.now()
    week_ago = now + timedelta(days=-7)
    if week_ago <= created_at <= now:
        return True
    else:
        return False

with open('../data/f2KYIvdHEACFdJHd_premium_search_twitter.txt') as f:
    data = f.read()
    twitter_json = json.loads(data)
    results = twitter_json['results']

# ================ PRINT TWEET INFO
    # for tweet in twitter_json['results']:
    #     print('Created: ', tweet['created_at'])
    #     print('Verified: ', tweet['user']['verified'])
    #     print('Followers: ', tweet['user']['followers_count'])
    #     print('Friends: ', tweet['user']['friends_count'])
    #     print('Text: ', tweet['text'], tweet['reply_count'])
    #     print('Retweets: ', tweet['retweet_count'])
    #     print('Favorites: ', tweet['favorite_count'], '\n')
# ================ PRINT DATES
    # for tweet in results:
    #     created_at = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
    #     about_a_week_ago_week_ago = timedelta(days=-7)
    #     print(created_at + about_a_week_ago_week_ago)

    # print(twitter_json['next'])

    test_created_at = datetime.now() + timedelta(days=-10)
    check_week_ago(test_created_at)

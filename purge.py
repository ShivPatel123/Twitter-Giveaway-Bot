# --- Imports ---
import time
import tweepy
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)

run = True

# Uncomment and input your Twitter ID in the 'id' variable below as an integer type.
# id =

client.wait_on_rate_limit = True

tweets = client.get_users_mentions(
    id=id, tweet_fields=['context_annotations', 'created_at', 'geo'], max_results=10)

for tweets in tweets.data:
    client.unretweet(tweets.id)
    client.unlike(tweets.id)

users = client.get_users_following(
    id=id, user_fields=['profile_image_url'], max_results=10)

for users in users.data:
    client.unfollow(users.id)

time.sleep(1800)

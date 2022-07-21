# --- Imports ---
import time
from datetime import datetime
import re
import tweepy
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET)


# --- Functions and Vars---

RUN = True
COUNT = 0
SUCCESSFUL_TWEETS = 1
BATCH_TOTAL = 0

regex_tagnum = re.compile(r'tag\s\d{1}')
regex_tagchar = re.compile(r'tag\ [a-zA-Z]\b')
regex_at = re.compile(r'@[a-zA-Z0-9_]*')

# INPUT TAGGED ACCOUNTS HERE
# Index 0 for 1 tag, Index 1 for 2 tags and so on...
tag_list = ['@', '@ @',
            '@ @ @',
            '@ @ @ @']

# INPUT QUERY KEYWORDS HERE
query_list = ['valorant', 'nft', 'csgo', 'steam', 'gaming', 'skin']


def regex_search(regex, search_str):
    """
    # Searches a block of text given a regex expression. Strips any @ symbols from
    the list in order to provide only handle names.
    """
    list_search = re.findall(regex, search_str)
    stripped_list = [s.strip('@') for s in list_search]
    nstripped_list = []
    for item in stripped_list:
        if item != '':
            nstripped_list.append(item)
    return nstripped_list


def return_twitterid(input_screen_name):
    """
    # Returns the Twitter ID of a user given their screen name.
    """
    # print("The screen name is: " + input_screen_name)
    twitterid = client.get_user(username=input_screen_name)
    # print(type(twitterid))  # to confirm the type of object
    # print(f"The Twitter ID is {twitterid.data.id}.")
    return twitterid.data.id


query = str(query_list[COUNT]) + ' giveaway RT -twitch -is:retweet -is:reply'

# --- Main Program ---
while RUN:

    dateTimeObj = datetime.now()

    START_TIME = (str(dateTimeObj.year) + '-' + str(dateTimeObj.month) +
                  '-' + str(dateTimeObj.day-2) + 'T00:00:00Z')

    client.wait_on_rate_limit = True

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                         user_fields=['profile_image_url'], sort_order="relevancy",
                                         expansions='author_id', start_time=START_TIME,
                                         max_results=20)

    for tweet in tweets.data:

        TWEET_STRING = (str(tweet.text).lower())

        client.follow(tweet.author_id)
        client.like(tweet.id)
        client.retweet(tweet.id)

        ats = regex_search(regex_at, TWEET_STRING)
        taga = regex_search(regex_tagchar, TWEET_STRING)
        tagnum = regex_search(regex_tagnum, TWEET_STRING)
        otagnum_strip = [x.replace('tag ', '') for x in tagnum]
        ntagnum_strip = list(map(int, otagnum_strip))

        for twt_screen_name in ats:

            client.follow(return_twitterid(twt_screen_name))

        if len(taga) > 0 or len(ntagnum_strip) > 0:
            try:
                if len(taga) > 0:
                    try:
                        # Place an @ handle below
                        client.create_tweet(text='Done :) @',
                                            in_reply_to_tweet_id=tweet.id)
                        print(str(SUCCESSFUL_TWEETS) +
                              " Tweets Successful! | " + str(datetime.now()))
                        SUCCESSFUL_TWEETS += 1
                    except tweepy.errors.Forbidden:
                        print(
                            "You are not allowed to create a Tweet with duplicate content. | "
                            + str(datetime.now()))
            except IndexError:
                print("list index out of range")

            try:
                if len(ntagnum_strip) > 0:
                    try:
                        client.create_tweet(
                            text='Done :) ' + tag_list[ntagnum_strip[0]-1],
                            in_reply_to_tweet_id=tweet.id)
                        print(str(SUCCESSFUL_TWEETS) +
                              " Tweets Successful! | " + str(datetime.now()))
                        SUCCESSFUL_TWEETS += 1
                    except tweepy.errors.Forbidden:
                        print(
                            "You are not allowed to create a Tweet with duplicate content. | "
                            + str(datetime.now()))
            except IndexError:
                print("list index out of range")

        else:
            try:
                client.create_tweet(text='Done <3',
                                    in_reply_to_tweet_id=tweet.id)
                print(str(SUCCESSFUL_TWEETS) +
                      " Tweets Successful! | " + str(datetime.now()))
                SUCCESSFUL_TWEETS += 1
            except tweepy.errors.Forbidden:
                print(
                    "You are not allowed to create a Tweet with duplicate content. | "
                    + str(datetime.now()))
    print('\n')
    COUNT += 1
    if COUNT > 5:
        COUNT = 0

    print(str(SUCCESSFUL_TWEETS - 1) + ' tweets succeeded.')

    SUCCESSFUL_TWEETS = 1
    BATCH_TOTAL += 1

    print('The batch total is: ' + str(BATCH_TOTAL) +
          "\nSleeping for 4 hours..." + '\nMoving to ' + query_list[COUNT] + ' entry.')

    time.sleep(14400)

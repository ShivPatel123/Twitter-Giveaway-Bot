# Twitter Giveaway Bot #
A short and simple python based Twitter bot created by myself and [anshul-rao](https://github.com/anshul-rao) using the [Tweepy](https://github.com/tweepy/tweepy) library. This bot will automatically enter giveaways by liking, commenting, retweeting, and following the author of the post. 

## Features ##
* Automates entering giveaways
  * Follows tweet author and anyone tagged in the original post
  * Retweets 
  * Likes the post
  * Comments a short message and tags the number of people required to enter the giveaway
* Open source
  
## Setup ##
To get started, you will need to create a Twitter developer account at https://developer.twitter.com/ and create a application with OAuth 2.0 with both read and write permissions enabled. 

After cloning the repository, add the keys generated from your application into **config.py** in the given strings. 

Head into **main.py** and add the accounts you want to be tagged in the comments in the tag_list in line 30 and the topics you want to find giveaways for in the query_list in line 35. Insert one account that the bot will tag in the comments in line 103. Run **main.py**.

If you choose to use the purge feature, input the account's Twitter ID on line 17 as an integer type and run **purge.py**. However, using this feature can get the account temporarily banned due to Twitter's API limitations.

## Disclaimer ##
This project was created for educational purposes only. By using this bot, there is a risk for your account to be banned and you are responsible for any liablities. Please read [Twitter's API Automation rules](https://help.twitter.com/en/rules-and-policies/twitter-automation) and use this repository with caution.

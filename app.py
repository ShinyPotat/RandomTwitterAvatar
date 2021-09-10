import os
from dotenv import load_dotenv
load_dotenv()
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

folders = []

for item in os.listdir("."):
    if os.path.isdir(os.path.join(".", item)):
        folders.append(item)

print(folders)

import os
import random
from dotenv import load_dotenv
load_dotenv()
import tweepy

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

folders = []
root = "."

for item in os.listdir("."):
    if item[0] != "." and os.path.isdir(os.path.join(root, item)):
        folders.append(item)

folder = random.choice(folders)
files = os.listdir(os.path.join(root, folder))

avatar = files[0]
banner = files[1]

api.update_profile_image(os.path.join(folder, avatar))
api.update_profile_banner(os.path.join(folder, banner))


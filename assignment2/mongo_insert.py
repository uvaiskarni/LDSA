#Program to insert all the tweets into MongoDB database

from pymongo import MongoClient
import glob
import json

#Connect to Mongodb client
client = MongoClient('mongodb://127.0.0.1:27017')

#Create database named tweets
db = client.tweets

#Get all the tweets.txt files and read to store all the tweets into tweets db
files = glob.glob("tweets/files/tweets_*.txt")
for file in files:
    file_read = open(file,"r")
    for line in file_read:
        if line.strip():
            tweet_line = json.loads(line)
            db.tweets.insert(tweet_line)

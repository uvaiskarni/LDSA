import os
import glob
import json
from pymongo import MongoClient

# read all files present in tweets directory
tweets_dir = "/home/ubuntu/tweets/files"
data_path = os.path.join(tweets_dir,'tweets*.txt')
files = glob.glob(data_path)

# connecting to mongo Database present in local on port 27017
client = MongoClient('mongodb://127.0.0.1:27017')

# List of pronoun
pronoun_list = {'hen':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'han':0}

#creating DB tweets_db
Db_client = client.tweets_db

for file in files:
    
    for tweet in open(file,"r"):
        
        if tweet.strip():
            
            parsed_tweet = json.loads(tweet)
            Db_client.tweets_db.insert(parsed_tweet)


# find the pronun matching tweets and calculate 
for Var1,Var2 in pronoun_list.items():
        List_Of_Matches = Db_client.tweets_db.aggregate([
              { '$project' : { 'pronoun' : { '$split': ["$text", " "] }} },
              { '$unwind' : "$pronoun" },
              { '$match' : {'pronoun': { '$regex' : '^'+ Var1 +'$','$options':'i'}}}]);
        for each_match in List_Of_Matches:
            pronoun_list[Var1] += 1
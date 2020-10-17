#!/usr/bin/env python

from pymongo import MongoClient

#List of pronouns to be found
pronouns = {'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0,'hen':0}

#Connect to the MongoDB client
client = MongoClient('mongodb://127.0.0.1:27017')
#Use db tweets
db = client['tweets']

#Loop over the pronouns list 
for k,v in pronouns.items():
        #Query the db for matching pronouns
        coll = db.tweets.aggregate([
              { '$project' : { 'pron' : { '$split': ["$text", " "] }} },
              { '$unwind' : "$pron" },
              { '$match' : {'pron': { '$regex' : '\\b'+ k +'\\b','$options':'i' } }}
              ]);
        #Loop over the cursor object and count the corresponding occurences of pronouns
        for col in coll:
            pronouns[k] += 1

print(pronouns)

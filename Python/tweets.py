import json
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet ID: ", tweetData[0]["id"])

print("Tweet ID: ", tweetData[0]["text"])

for tweet in tweetData:
    print("tweet text" + tweet["text"])

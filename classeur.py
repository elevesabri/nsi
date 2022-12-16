import json

try:
    with open('tweet_data.json') as f:
        data = json.load(f)
except:
    raise ValueError("Une erreur est apparue, verifie ton tweet_data.json")
    

for ligne in data:
    for name in ligne['trends']:
        name['name']
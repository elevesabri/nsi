
import requests
import json

with open('cle.json') as f:
    bearer = json.load(f)['access_token']

base_url = 'https://api.twitter.com/'

search_headers = {
    'Authorization': 'Bearer {}'.format(bearer)    
}

search_params = {
    'q': "FranceMaroc",
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

with open('messages.json', 'w', encoding='utf-8') as f:
    json.dump(search_resp.json(), f, indent=4)
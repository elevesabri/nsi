import requests
import json

with open('bearer.json') as f:
    bearer = json.load(f)['access_token']

base_url = 'https://api.twitter.com/'

woeid = 1 # https://www.woeids.com/


search_headers = {
    'Authorization': 'Bearer {}'.format(bearer)    
}

search_params = {
    'id': woeid,
}

search_url = '{}1.1/trends/place.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

with open('tweet_data.json', 'w', encoding='utf-8') as f:
    json.dump(search_resp.json(), f, indent=4)
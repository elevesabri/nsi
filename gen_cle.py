import requests
import base64
import json

# (1) Base de la requête

base_url = 'https://api.twitter.com/'

# (2) Auth (conversion en base64 obligatoire) (api key:secret)

connexion = base64.b64encode("CLE API".encode("ascii")).decode("ascii")

auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': f'Basic {connexion}',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data) # host, header(auth,cotent-type), data(grant_type) c'est le minimum

# Récupération de la clé pour faire les requêtes (3)

with open('bearer.json', 'w', encoding='utf-8') as f:
    json.dump(auth_resp.json(), f, indent=4)
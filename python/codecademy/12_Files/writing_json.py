data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

#convert dict into json

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)


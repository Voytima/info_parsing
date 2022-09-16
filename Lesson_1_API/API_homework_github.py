# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
# для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json

user = 'Voytima'
url = 'https://api.github.com'

response = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(response.json(), f)

for i in response.json():
    print(i['name'])

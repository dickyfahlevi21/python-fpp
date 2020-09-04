import requests
from pprint import pprint



r = requests.get('https://mul14.github.io/data/employees.json')

r_json = r.json()
print(list(filter(lambda x: x, r_json)))
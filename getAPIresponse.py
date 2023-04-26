import requests

api_key = '63bf1bb6967221fdecbcf27c712ff6d4'
url = 'http://localhost:5000/keyword_search'
data = {'words': 'roads'}
headers = {'api_key': api_key}
response = requests.post(url, data=data, headers=headers)

print(response.text)
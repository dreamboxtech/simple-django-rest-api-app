import requests

response = requests.get('http://127.0.0.1:8000/drinks/3')
print(response.json())
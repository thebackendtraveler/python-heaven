import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/search?q=pomeranian")
print(response.text)
import requests

response = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=beng")
print(response.text)
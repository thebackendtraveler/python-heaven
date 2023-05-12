import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/search?q=pomeranian")
print("Content type:", response.headers.get("Content-Type"))
print("Server:", response.headers.get("Server"))
response = requests.get("https://picsum.photos/200/300")
print("Content type:", response.headers.get("Content-Type"))
print("Server:", response.headers.get("Server"))
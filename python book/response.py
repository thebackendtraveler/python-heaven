import requests
import io
import os

response = requests.get("https://api.thedogapi.com/v1/breeds/search?q=pomeranian")
print("JSON content type:", type(response.json()))
print("JSON content: ", response.json())
print("JSON content - specific value - name: ", response.json()[0]["name"])
print("JSON content - specific value - bred-for: ", response.json()[0]["bred_for"])

response = requests.get("https://picsum.photos/640/480")
print("Image content type: ", type(response.content))
print("Image content: ", response.content)
my_file = open("placeholder.jpg", "wb")
my_file.write(response.content)
my_file.close()
os.system("open placeholder.jpg")
import requests
import io
import os

response = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=mcoo")
print("JSON content type:", type(response.json()))
print("JSON content: ", response.json())
print(response.text)

response = requests.get("https://picsum.photos/640/480")
print("Image content type: ", type(response.content))
print("Image content: ", response.content)
my_file = open("placeholder.jpg", "wb")
my_file.write(response.content)
my_file.close()
os.system("open placeholder.jpg")
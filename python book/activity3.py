import requests
import os

endpoint = "https://api.thecatapi.com/v1/images/search?breed_ids=mcoo"
api_key = "live_XbzUYdxkYci5P9s0fRXRiIVSgEmaxBgRGvR3v9RJuNqFdtncnvHFZnanIPd5ehsM"
query_parameters = {"api_key": api_key, "earth_date": "2021-03-22"}
response = requests.get(endpoint, params=query_parameters)

print(response.text)
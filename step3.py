import requests
import json

response = requests.post("http://challenge.code2040.org/api/haystack",
        json={"token": "377114ac072509b65418ac1f61fbdead"})

content = json.loads(response.content.decode("utf_8"))

index = content["haystack"].index(content["needle"])

requests.post("http://challenge.code2040.org/api/haystack/validate",
        json={"token": "377114ac072509b65418ac1f61fbdead", "needle": index})

import requests
import json

response = requests.post("http://challenge.code2040.org/api/prefix",
        json={"token": "377114ac072509b65418ac1f61fbdead"})

content = json.loads(response.content.decode("utf_8"))

prefix = content["prefix"]
array = content["array"]

new_array = [s for s in array if not s.startswith(prefix)]

requests.post("http://challenge.code2040.org/api/prefix/validate",
        json={"token": "377114ac072509b65418ac1f61fbdead", "array": new_array})

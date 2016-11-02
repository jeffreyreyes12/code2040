import requests

response1 = requests.post("http://challenge.code2040.org/api/reverse",
        json={"token": "377114ac072509b65418ac1f61fbdead"})

requests.post("http://challenge.code2040.org/api/reverse/validate", 
        json={"token": "377114ac072509b65418ac1f61fbdead",
              "string": response1.content[::-1].decode("utf_8")})

import json
from datetime import datetime, timedelta

import requests

response = requests.post("http://challenge.code2040.org/api/dating",
        json={"token": "377114ac072509b65418ac1f61fbdead"})

content = json.loads(response.content.decode("utf_8"))

date = datetime.strptime(content["datestamp"], "%Y-%m-%dT%H:%M:%SZ")
delta = timedelta(seconds=content["interval"])

newdate = date + delta

requests.post("http://challenge.code2040.org/api/dating/validate",
        json={"token": "377114ac072509b65418ac1f61fbdead", 
              "datestamp": newdate.strftime("%Y-%m-%dT%H:%M:%SZ")})

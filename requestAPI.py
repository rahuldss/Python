import requests

# Generate API here for questions
# https://opentdb.com/api_config.php

r = requests.get("https://opentdb.com/api.php?amount=1&category=18")
print(r.status_code)
print(r.text)

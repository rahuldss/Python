import requests
import json
import pprint

# Generate API here for questions
# https://opentdb.com/api_config.php

r = requests.get("https://opentdb.com/api.php?amount=1&category=18")
print(r.status_code)
print(r.text)
result_text = json.loads(r.text)
category = result_text['results'][0]['category']
question = result_text['results'][0]['question']
correct_answer = result_text['results'][0]['correct_answer']
incorrect_answers = result_text['results'][0]['incorrect_answers']
pprint.pprint(category)
pprint.pprint(question)
pprint.pprint(incorrect_answers)

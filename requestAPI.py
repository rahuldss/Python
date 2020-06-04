import requests

# Generate API here for questions
# https://opentdb.com/api_config.php

# r = requests.get("https://opentdb.com/api.php?amount=1&category=18")
# print(r.status_code)
# print(r.text)

# url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

# querystring = {"date":"2020-05-02"}
querystring = {"country":"Canada"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

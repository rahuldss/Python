import requests

r = requests.get("https://www.google.com")
print(r.status_code)
print(r.headers)
print(r.headers["Date"])
print(r.text)

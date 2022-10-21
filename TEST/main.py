import requests


link = "https://api.github.com/"
f = requests.get(link)

print(f.text)
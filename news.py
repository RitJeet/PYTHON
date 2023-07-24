import requests
import json
import time
import datetime
x=datetime.datetime.now()
print("----------------------------------------")
print(f"|  Date = {x}  |")
print("----------------------------------------")
topic=input("What topic you want : ")
req=requests.get(f"https://newsapi.org/v2/everything?q={topic}&from=2023-06-09&sortBy=publishedAt&apiKey=383c037101f04de59d39fb9b81f9e28f")
articlex=json.loads(req.text)
i=0
for articles in articlex["articles"]:
    i=i+1
    print(f'{i}){articles["title"]}')
    print(f'Description :- {articles["description"]}')
    print("------------------------------------")
    time.sleep(2)
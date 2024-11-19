import pandas as pd
import json
import requests
import datetime
from datetime import date
import uuid
import os
# from google.cloud import storage


def fetch_news_data ():
    today = date.today()
    base_url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&apiKey={}"
    api_key = "3e8bbac7fb794c92b43c08c8b590db4f"
    start_date = str(today - datetime.timedelta(days=1))
    end_date = str(today)
    df = pd.DataFrame(columns=['sourceName','author','title','description','publishedAt','content'])
    url_extractor = base_url.format('bitcoin',start_date,end_date,api_key)

    response = requests.get(url_extractor)
    d = response.json()

    for i in d['articles']:
        source = i['source']
        sourceName= source['name']
        author = i['author']
        title = i['title']
        description = i['description']
        publishedAt = i['publishedAt']
        content = i['content'] if i['content'] is not None else ""

        new_row = pd.DataFrame({
            'sourceName':[sourceName],
            'author':[author],
            'title':[title],
            'description':[description],
            'publishedAt':[publishedAt],
            'content':[content]
        })
        df = pd.concat([df,new_row],ignore_index=True)
        print(df)
        break
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'run_{current_time}.json'
    df.to_json(filename)
fetch_news_data()
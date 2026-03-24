import pandas as pd
import numpy as np

from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key="92d9699269bc4045aedc892b1f37247a")

keywords = ['Apple-Stock', 'Apple-Revenue', 'Apple-Sales', 'Apple', 'AAPL']

# Dataframe to store the news article information
article_info = pd.DataFrame(columns=['Date', 'Title', 'Articles', 'Link'])

# Fetch news articles for each keyword
for keyword in keywords:
    # Fetch news articles using News API
    articles = newsapi.get_everything(q=keyword, language='en', sort_by='publishedAt', page_size=100)

    # Extract article details and append to the DataFrame
    for article in articles['articles']:
        date = pd.to_datetime(article['publishedAt'])
        title = article['title']
        articles = article['description']
        link = article['url']


        new_row = {'Date': date, 'Title': title,'Articles': articles, 'Link': link}
        new_rowdf = pd.DataFrame([new_row])
        # Note : DataFrame.append has been deprecated, use concat or loc instead
        article_info = pd.concat([article_info, new_rowdf], ignore_index=True)

# Resetting the index of the final result
article_info.index = pd.RangeIndex(start=1, stop=len(article_info) + 1, step=1)
print(article_info.tail())
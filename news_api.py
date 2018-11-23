"""
Created on Wed Oct 24 07:24:02 2018
@author: Jose Antonio Arias
"""

def newsApi(top_headlines):
    i = 0
    json_ = []
    articles = top_headlines['articles']
    if len(articles) > 0:
        json_.append(articles[i]['source']['name'])
        json_.append(articles[i]['description'])
        json_.append(articles[i]['url'])
        return(json_)

    else:
        return('no result')

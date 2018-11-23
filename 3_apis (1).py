"""
Created on Wed Oct 24 07:21:44 2018
@author: Jose Antonio Arias
"""
#libraries
import random
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random, string
import newsapi
""""
from newsapi import NewsApiClient
"""
from news_api import newsApi
from api_mysql2 import nytimes
from twython import Twython
from twitter import twitter
from multipro import myThread
from multipro import run_api
from query_fire import get_user
from insert_fire import insert_user
import firebase_admin
from firebase_admin import credentials
from multipro import Listener
from query_fire import get_searches
from query_fire import get_history
from insert_fire import insert_data

cred = credentials.Certificate("credentials.json")

#firebase_admin.initialize_app(cred)


thread1 = myThread(1, "Thread-1", 0)
thread2 = myThread(2, "Thread-2", 0)
thread3 = myThread(3, "Thread-3", 0)

thread1.start()
thread2.start()
thread3.start()
#api tokens
"""
newsapi = NewsApiClient(api_key='17a51cc53e444a46b84ce26ee223d40d')
"""
APP_KEY = "UKP4lexaxthDyD7JdSoPU6hit"
APP_SECRET = "bgPLO3BINx96qRQoF7r2d8cO2cvYxONJInz2t5lhDrQTRaHExR"
OAUTH_TOKEN = "1022907936287477760-l0Gr2wu8lkEvrg2666wRT1sVpfK4Aq"
OAUTH_TOKEN_SECRET = "Uzh5LhCW0FSEACH3fq93UE7nQDxIApJ2t9VBXSw87S1Zt"

#initiate flask
app = Flask(__name__)
api = Api(app)

#token generator
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


#Main Search Endpoint
class Search(Resource):
    def get(self, kwd1, kwd2, tkn):
           Listener(kwd1, kwd2, tkn)
           find_user = get_user(tkn)
           if find_user == True:
               print('si esta el usuario')
               searches = get_history(kwd1,kwd2)
               if len(searches)> 1:
                    insert_data(kwd1, kwd2, tkn, searches)
                    return(searches)
               else:
                   threadID = 1
                   while threadID < 4:
                        runner = run_api(threadID, kwd1, kwd2)
                        threadID += 1
                        insert_data(kwd1, kwd2, tkn, runner)
                        return(runner)

           else:
                insert_user(tkn)
                searches = get_history(kwd1,kwd2)
                if len(searches)> 1:
                    insert_data(kwd1, kwd2, tkn, searches)
                    return(searches)
                else:
                   threadID = 1
                   while threadID < 4:
                        runner = run_api(threadID, kwd1, kwd2)
                        threadID += 1
                        insert_data(kwd1, kwd2, tkn, runner)
                        return(runner)

#history endpoint
class History(Resource):
    def get(self, tkn):
        searches = get_searches(tkn)
        return(searches)


#endpoint params
"""
api.add_resource(Search, '/search/<kwd1>/<kwd2>/<tkn>') # Route_1
"""
api.add_resource(History, '/history/<tkn>') # Route_2
api.add_resource(Search, '/search/<kwd1>/<kwd2>/<tkn>') # Route_3


if __name__ == '__main__':
     app.run()

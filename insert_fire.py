"""
Created on Mon Oct 29 08:24:28 2018
@author: Jose Antonio Arias
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("credentials.json")
#firebase_admin.initialize_app(cred)

db = firestore.client()

def insert_data(kwd1, kwd2, token, search_result):

    insert_data_history = {
        u'keyword1': kwd1,
        u'keyword2': kwd2,
        u'search': search_result
    }

    insert_data_search = {
        u'keyword1': kwd1,
        u'keyword2': kwd2,
        u'user': token
    }

    # insert user data
    db.collection(u'searches').add(insert_data_search)
    db.collection(u'history').add(insert_data_history)


def insert_user(tkn):
    insert_data_user = {
        u'user': tkn
    }
    db.collection(u'users').add(insert_data_user)




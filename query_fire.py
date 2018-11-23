"""
Created on Tue Nov 20 10:22:36 2018
@author: Jose Antonio Arias
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user(token):    
    docs = db.collection(u'users').get()
    doc_list = []
    for doc in docs:
        doc_list.append(str(doc.to_dict()))            

    user = "{'user': "+token+"}"    
    if user in doc_list:
        return(True)

def get_searches(tkn):
    docs = db.collection(u'searches').get()
    doc_list = []
    for doc in docs:
        doc_list.append(str(doc.to_dict()))

    if tkn in str(doc_list):
        return(doc_list)

def get_history(kwd1, kwd2):
    docs = db.collection(u'history').get()
    doc_list = []
    for doc in docs:
        doc_list.append(str(doc.to_dict()))

    if kwd1 or kwd2 in str(doc_list):
        return(doc_list)


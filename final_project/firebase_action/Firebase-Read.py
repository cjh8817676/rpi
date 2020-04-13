#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
#Get Collection
doc_ref = db.collection('Q1', 'DOC1', 'Q2')
docs = doc_ref.get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

#Get Doc
doc_ref = db.collection('Q1', 'DOC1', 'Q2').document('DOC2')
docs = doc_ref.get()
print('姓名 => {}'.format(doc.to_dict()['姓名']))
print('年紀 => {}'.format(doc.to_dict()['年紀']))
print('工作 => {}'.format(doc.to_dict()['工作']))

print('Done')

"""
$ python Firebase-Read.py
DOC2 => {'年紀': '23', '工作': '魔法師', '姓名': '劉德華'}
姓名 => 劉德華
年紀 => 23
工作 => 魔法師
Done
"""
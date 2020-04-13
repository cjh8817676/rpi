import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def firebase_Write():
    doc_ref = db.collection('Users', 'DOC1', 'Q2').document('DOC2')
    doc_ref.set({
    '姓名': '劉德華',
    '年紀': '23',
    '工作': '爆肝工程師',
    })
#Method 2
    data = {
        '姓名': '劉德華',
        '年紀': '23',
        '工作': '爆肝工程師',
    }
    doc_ref.set(data)
    print('Done')

def firebase_Read():
    #!/usr/bin/python3

    doc_ref = db.collection('使用者們','jonathan1446171@gmail.cpm','汽車資訊')
    docs = doc_ref.get()
    print(docs)
    
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

def firebase_Update():
    doc_ref = db.collection('使用者們', 'jonathan1446171@gmail.cpm', '汽車資訊').document('車子狀態')
    #Method 1
    doc_ref.update({
        '車主': 'ssss',
    })
    #Method 2
    data = {
        '車牌': 'NH1958',
    }
    doc_ref.update(data)
    print('Done')


firebase_Update()
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("car-project-b45b3-firebase-adminsdk-41ei0-555cf34e12.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
#讀取停車格全部"預約及占用"資料
def firebase_Read_ParkingGridData():
    doc_ref = db.collection('parking grid')
    docs = doc_ref.get()
    '''
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    '''
    return docs
def firebase_Read_Available_Parking_Grid():
    parking_data = firebase_Read_ParkingGridData()
    parking_dict_data = {} #建立空辭典
    '''
    parking_data是一個  Generator object 也是一個 Iterator，帶有 __iter__ 和 __next__ attributes。
    可和外部進行雙向溝通，可以傳出也可以傳入值。
    '''
    #print(dir(parking_data))
    for doc in parking_data:
        #print(u'{} => {}'.format(doc.id, doc.to_dict()))
        #print(doc.to_dict()['預約中'])
        if doc.to_dict()['預約中'] == False and doc.to_dict()['使用中'] == False :
            parking_dict_data[doc.id] = doc.to_dict()
            
    return parking_dict_data
def firebase_Read_Occupied_Parking_Grid():
    parking_data = firebase_Read_ParkingGridData()
    parking_dict_data = {} #建立空辭典
    '''
    parking_data是一個  Generator object 也是一個 Iterator，帶有 __iter__ 和 __next__ attributes。
    可和外部進行雙向溝通，可以傳出也可以傳入值。
    '''
    for doc in parking_data:
        #print(u'{} => {}'.format(doc.id, doc.to_dict()))
        #print(doc.to_dict()['預約中'])
        if doc.to_dict()['預約中'] == True or doc.to_dict()['使用中'] == True :
            parking_dict_data[doc.to_dict()['預約車牌']] = doc.id
            
    return parking_dict_data

def firebase_Car_Enter_Add_and_Update(plate,grid_id):
    doc_ref = db.collection(u'parking grid').document(str(grid_id))
    
    try:
        doc = doc_ref.get() 
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
        
    doc_ref.update({
        '預約車牌': ' ',
        '使用中' : True,
        '預約中' : False,
    })
def firebase_Car_Exit_and_Update(plate,grid_id):
    doc_ref = db.collection(u'parking grid').document(u'A1')
    
    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
        
    doc_ref.update({
        '預約車牌': ' ',
        '使用中' : True,
        '預約中' : False,
    })


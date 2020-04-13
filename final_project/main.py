from setting_Car import Car
from setting_Manage import ParkManage
from auto_recognize import recognize_and_indicate
from firebase_action import firebase_action as data_action
import take_picture
import re
import cv2
import sys

import smbus
import time
from take_picture import make_photo
# 設定樹莓派I2C的總線
bus = smbus.SMBus(1)

# 設定Arduino 的I2C位置
address = 0x04


# 傳送訊息
def writeNumber(value):
    bus.write_byte(address, value)
    return -1

# 讀取訊息
def readNumber():
    number = bus.read_byte(address)
    return number

def check_car_number(car_number):    #判斷車牌號是否合法
    #pattern = re.compile(u'[\u4e00-\u9fa5]?')
    pattern1 = re.compile(u'[A-Z]+')
    pattern2 = re.compile(u'[0-9]+')

    #match = pattern.search(car_number)
    match1 = pattern1.search(car_number)
    match2 = pattern2.search(car_number)
    if match1 and match2:
        return True
    else:
        return False
def check_contact_way(contact_way):   #判斷手機號是否合法
    pattern = re.compile(u'0[1|2|3|4|5|6|7|8|9]\d{8}$')

    match = pattern.search(contact_way)
    if match:
        return True
    else:
        return False
def main():
    parkmanage=ParkManage()
    print ('Hi Arduino')
    while True:
        parkmanage.info()
        reservation_plate = data_action.firebase_Read_Occupied_Parking_Grid()
        # 指定var接受使用者輸入的指令
        var = int(input('Enter 1 – 9: '))
        #寫入使用的輸入的指令Var
        writeNumber(var)
        print ('RPI: Hi Arduino, I sent you ', var)
    
        # 等待1秒
        time.sleep(1)
    
        #接收Arduino回傳的訊息
        number = readNumber()
        print (type(number))
        if number==1:
               choice='1'
        print ('Arduino: Hey RPI, I received a digit ', number)
        
        if choice=='1':   #偵測到car
            make_photo()
            #35行新增拍照程式,現在先固定照片
            #picture_path = "/home/pi/ea7the.jpg"
            #make_photo()
            #car_number=recognize_and_indicate(picture_path)
            
            #for plate in reservation_plate:
                
                 #if plate == car_number:        
                    #check_error_list=[]
            
            #if check_car_number(car_number):
                #car_owner=input("請輸入車主姓名:")
                #contact_way=input("請輸入車主聯絡方式:")
                #if check_contact_way(contact_way):
                    #check_error_list=[car_number,car_owner,contact_way]
                    #for info in check_error_list:    #判斷輸入資訊的完整性
                        #if info=='':
                            #print("輸入資訊不全")
                            #break
                    #else:
                        #car = Car(car_number, car_owner, contact_way)
                        #parkmanage.add_car(car)
                #else:
                    #print("手機號無效")
            #else:
                #print("車牌號不合法")

        elif choice=='2':
            parkmanage.searchCar()
        elif choice =='3':
            parkmanage.display()
        elif choice=='4':
            parkmanage.change_Carinfo()
        elif choice=='5':
            car_number = input("輸入您要刪除的車輛的車牌號：")
            for car in parkmanage.car_list:
                if car.car_number == car_number:
                    parkmanage.delete_car(car)
                    break
            else:
                print("未找到車牌號為%s的車輛" % (car_number))

        elif choice=='6':
            parkmanage.statistics()
        elif choice=='7':
            print("歡迎下次使用！！！")
            exit()
        else:
            print("請輸入正確的選項")

if __name__ == '__main__':
    main()
    '''
    車牌經由辨識取得
    '''
    #c = data_action.firebase_Read_Occupied_Parking_Grid()
    #print (c)
    #print (c.values())
    #print (c.get(" EA7THE")) #get str
    #data_action.firebase_Car_Enter_Add_and_Update('EA7THE',c.get('EA7THE'))

        



        

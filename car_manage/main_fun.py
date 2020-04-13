import re
from  setting_Car import Car
from setting_Manage import ParkManage


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
    while True:
        parkmanage.info()
        choice=input("請輸入你要的功能:")
        if choice=='1':
            check_error_list=[]
            car_number=input("請輸入車牌號:")
            if check_car_number(car_number):
                car_owner=input("請輸入車主姓名:")
                contact_way=input("請輸入車主聯絡方式:")
                if check_contact_way(contact_way):
                    check_error_list=[car_number,car_owner,contact_way]
                    for info in check_error_list:    #判斷輸入資訊的完整性
                        if info=='':
                            print("輸入資訊不全")
                            break
                    else:
                        car = Car(car_number, car_owner, contact_way)
                        parkmanage.add_car(car)
                else:
                    print("手機號無效")
            else:
                print("車牌號不合法")

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
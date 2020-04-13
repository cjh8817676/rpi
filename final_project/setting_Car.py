import time
from setting_Manage import ParkManage

class Car():
    """一個關於車的類"""
    def __init__(self,car_number,car_owner,contact_way):
        super(Car, self).__init__()
        self.car_number=car_number
        self.car_owner=car_owner
        self.contact_way=contact_way
        self.balance=200
        self.entrance_time = 0
        self.exit_time = 0

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def slot_card(self):
        """根據時間計費"""
        park_time=time.mktime(time.strptime(self.exit_time)) - time.mktime(
            time.strptime(self.entrance_time))
        h=park_time//3600
        m=(park_time-h*3600)//60
        s=park_time-h*3600-m*60
        P_time="%.0f時%.0f分%.0f秒"%(h,m,s)
        consumption = ((park_time) / 3600) * 5
        self.balance -= consumption
        print("車牌號為:%s\n停車時長:%s\n本次消費:%.2f元\n卡里餘額:%.2f元\n" % (self.car_number,P_time, consumption, self.balance))

    def __str__(self): 
        '''將汽車資訊顯示成字串'''
        return "%s %s %s %s" %(self.car_number,self.car_owner,self.contact_way,self.entrance_time)
# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
# BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)    
# 输出模式    
GPIO.setup(13, GPIO.OUT)    

while True:    
     GPIO.output(13, GPIO.HIGH)    
     time.sleep(1)    
     GPIO.output(13, GPIO.LOW)    
     time.sleep(1)
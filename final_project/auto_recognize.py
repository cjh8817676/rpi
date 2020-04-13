from lcd_library import my_lcd as lcd
from openalpr import Alpr
import re
import numpy as np
import cv2
import sys
import time

def recognize_and_indicate(picture_path):
    alpr = Alpr("us", "/usr/local/src/openalpr/src/config/openalpr.conf", "/usr/local/src/openalpr/runtime_data")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    
    alpr.set_top_n(20)
    alpr.set_default_region("md")

    results = alpr.recognize_file(picture_path)
    i = 0

    for plate in results['results']:
        i += 1
        #print("Plate #%d" % i)
        #print("   %12s %12s" % ("Plate", "Confidence"))
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"
            break
        break
            #print("  %s %12s%12f " % (prefix, candidate['plate'], candidate['confidence']))

    the_plate = candidate['plate']
    # Call when completely done to release memory
    lcd.init()              # Basic HW system setup - port directions on the expander and reset the display
    lcd.clearDisplay(0)     # Complete deletion of the display

    lcd.initTextMode()     # Switch to text mode

    lcd.printStringTextMode("Lisence Number :",0,0)   # Display the text in the text mode at specified coordinates
    lcd.printStringTextMode(the_plate,0,1)
    time.sleep(2)
    lcd.clearDisplay(0)     # Complete deletion of the display
    return the_plate

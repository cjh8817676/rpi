# -- coding:UTF-8 --<code>
import cv2
import time
def make_photo():
    """使用opencv拍照"""
    """默認攝像頭"""
    cap = cv2.VideoCapture(0)  
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("capture", frame)
            time.sleep(3)
            """ q關閉攝像頭並存檔"""
            if cv2.waitKey(1) & 0xFF == ord('q'):
                file_name = "xieyang.jpeg"
                cv2.imwrite(file_name, frame)
                break
        else:
            break
 
    cap.release()
    cv2.destroyAllWindows()


 
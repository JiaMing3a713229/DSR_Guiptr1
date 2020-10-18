import cv2
import numpy as np
import time
from pyModbusTCP.client import ModbusClient
cap = cv2.VideoCapture(0)
time.sleep(2)
SERVER_HOST = "192.168.1.1"
SERVER_U_ID = 2
a = np.array(65536)
c = ModbusClient(auto_open=True)


c.host(SERVER_HOST)
c.unit_id(SERVER_U_ID)
c.open()


'''width，height縮放大小'''
def get_picture(width,heigth):


    rat,frame=cap.read()
    frame = cv2.resize(frame, (width, heigth))
    frame = cv2.flip(frame, 1)

    #cv2.imwrite('D:/Desktop/result/imperson.jpg',frame)
    print("get picture")

    return frame
'''增強圖片對比度'''
'''利用線性方程式增強'''
def improve_brightness(img):

    rows, cols, channels = img.shape
    dst = img.copy()
    a = 1
    b = 30
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                dst[i,j,c] = np.clip(a*img[i,j,c] + b, 0, 255)
    return dst

def roiarea(frame):

    return frame[top:bottom,left:right]

def replaceroi(frame,roi):

    frame[top:bottom,left:right]=roi

    return frame



if __name__ == '__main__':
    #紅色
    #color = ((156, 43, 46), (180, 255, 255))
    #黃色
    color = ((26, 43, 46), (34, 255, 255))

    lower = np.array(color[0], dtype='uint8')
    upper = np.array(color[1], dtype='uint8')




    frame=get_picture(400,300)
    #frame=cv2.imread('D:/Desktop/result/test10.jpg')


    #frame=improve_brightness(frame)

    #frame = cv2.resize(frame, (400, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    '''高斯模糊'''
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)

    '''hsv 二值化'''
    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow('inrange',mask)

    #cv2.imwrite("D:/Desktop/result/red.jpg", mask)
    #cv2.imshow('inrange', mask)

    kernel = np.ones((5, 5), np.uint8)
    '''二值化侵蝕'''
    mask = cv2.erode(mask, kernel, iterations=2)
    #cv2.imshow('erode', mask)

    kernel = np.ones((5, 5), np.uint8)
    '''二值化膨脹'''
    mask = cv2.dilate(mask, kernel, iterations=2)

    cv2.imshow('mask',mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    '''如果輪廓大於0則進行動作'''
    if len(contours) > 0:
        '''取最大輪廓'''
        cnt = max(contours, key=cv2.contourArea)
        '''如果最大輪廓大於300則進行動作'''
        if cv2.contourArea(cnt) > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            x1, y1, x2, y2 = x, y, x + w , y + h

            #dst=frame.copy()
            dst=mask.copy()
            img = cv2.rectangle(frame, (x1-35, y1-35), (x2+20, y2+20), (0, 0, 255), 2)
            #cv2.putText(frame, "red color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
            cv2.putText(frame, "Yellow color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
            #cv2.drawContours(frame, cnt, -1, (0, 0, 255), 2)

            RECT = ((x1-35,y1-35),(x2+20,y2+20))

            (left,top),(right,bottom)=RECT
            '''取得重點區域'''
            roi = roiarea(dst)
            #roi = cv2.resize(roi,(400,300))
            #gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            '''關掉試試'''
            #ret, binary = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY)
            #binary = cv2.bitwise_not(binary)
            #cv2.imshow('binary',binary)
            #edged = cv2.Canny(binary, 50, 150)

            #edged = cv2.dilate(edged, None, iterations=1)
            '''10/18'''
            #contours1, hierarchy1 = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours1, hierarchy1 = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            approx_result = cv2.approxPolyDP(contours1[0], 30, True)
            cv2.drawContours(roi, contours1, -1, (0, 255, 0), 3)
            cv2.drawContours(roi, [approx_result], -1, (0, 255, 0), 3)


            length = (len(approx_result))
            print(length)
            result=length
            print(result)
            if length == 6:
                cv2.putText(frame, "Hexagon", (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
                print('Hexagon')
                rc = c.write_single_register(0x1100,6)

                #動作
                print(length)
            elif length == 4:
                cv2.putText(frame, "Rectangle", (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
                print('Rectangle')
                rc = c.write_single_register(0x1100, 4)
                print(length)

            elif length == 3:
                cv2.putText(frame, "Triangle", (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
                print('Triangle')
                rc = c.write_single_register(0x1100, 3)
                print(length)

            cv2.imshow('roi',roi)

    #rc = c.read_holding_registers(0x1100, 1)
    cv2.imshow("frame", frame)
    cv2.imwrite("D:/Desktop/result/red.jpg", mask)






    cv2.waitKey(0)
    cv2.destroyAllWindows()
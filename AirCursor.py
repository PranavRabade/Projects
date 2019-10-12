import numpy as np
import cv2
import win32api
from array import array
import pyautogui
 
face_cascade = cv2.CascadeClassifier('D:\Tools\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

xi,yi=win32api.GetCursorPos()

xvalue_lclick=np.array((xi,)*55,'i')
yvalue_lclick=np.array((yi,)*55,'i')

xvalue_rclick=np.array((xi,)*80,'i')
yvalue_rclick=np.array((yi,)*80,'i')
i=0
n=0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        xpos=(int(x+w/2)*3)%1365
        ypos=(int(y+h/2)*4)%767
        win32api.SetCursorPos((xpos,ypos))
		
        xvalue_lclick[i]=xpos
        yvalue_lclick[i]=ypos
        xvalue_rclick[n]=xpos
        yvalue_rclick[n]=ypos
        
        i=(i+1)%55
        n=(n+1)%80
        
        xflag_lclick=1
        yflag_lclick=1
        xflag_rclick=1
        yflag_rclick=1
        for m in range(0,80):
            if xvalue_rclick[m]-xpos>30 or xvalue_rclick[m]-xpos<-30:
                xflag_rclick=0
            if yvalue_rclick[m]-ypos>30 or yvalue_rclick[m]-ypos<-30:
                yflag_rclick=0
                
        if xflag_rclick and yflag_rclick:
            print("Right click invovked")
            pyautogui.rightClick(xpos,ypos)
            
        else:        
            for j in range(0,55):
                if xvalue_lclick[j]-xpos>30 or xvalue_lclick[j]-xpos<-30:
                    xflag_lclick=0
                if yvalue_lclick[j]-ypos>30 or yvalue_lclick[j]-ypos<-30:
                    yflag_lclick=0
        
            if xflag_lclick and yflag_lclick:
                print("click invoked")
                pyautogui.click(xpos,ypos)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

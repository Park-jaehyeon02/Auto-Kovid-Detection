import os
import cv2

pathDir = "./img_raw"
saveDir = "./img_process"

fileList = os.listdir(pathDir)

def setLabel(img,pts,label):
    (x,y,w,h) = cv2.boundingRect(pts)
    if w>5 and h>5:
        pt1 = (x,y)
        pt2 = (x+w,y+h)
        cv2.rectangle(img,pt1,pt2,(0,255,0),2)

for i in range(len(fileList)):
    imgPath = pathDir + '/' + fileList[i]
    img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
    # img = cv2.resize(img,(300,300))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        approx = cv2.approxPolyDP(cont,cv2.arcLength(cont,True)*0.02,True)
        vtc = len(approx)
        if vtc==4:
            setLabel(img,cont,"Rec")
    cv2.imshow('dst', dst)
    cv2.imshow('org', img)
    cv2.waitKey(0)


cv2.destroyAllWindows()

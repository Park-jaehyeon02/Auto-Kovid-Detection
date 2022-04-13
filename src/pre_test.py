import cv2 

def setLabel(img,pts,label):
    (x,y,w,h)=cv2.boundingRect(pts)
    if w>10 and h>10:
        pt1 = (x,y)
        pt2=(x+w,y+h)
        cv2.rectangle(img,pt1,pt2,(0,255,0),2)
        cv2.putText(img,label,(pt1[0],pt1[1]-3),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))

img = cv2.imread("test.jpg") 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, dst = cv2.threshold (gray, 150, 255, cv2.THRESH_BINARY) 
contour ,_=cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for cont in contour:
    approx = cv2.approxPolyDP(cont,cv2.arcLength(cont,True)*0.02,True)
    vtc = len(approx)

    if vtc ==4:
        setLabel(img,cont,"Rec")

cv2.imshow("original", img) 
cv2.imshow("binary", dst) 
cv2.waitKey(0)
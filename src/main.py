import cv2
import copy

upper_red = (10, 255, 255)
lower_red = (-20, 30, 30)


def mask(img):
    x, y, w, h = cv2.selectROI('img', img, False)
    if w and h:
        roi = img[y:y + h, x:x + w]
        roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        roi_mask = cv2.inRange(roi_hsv, lower_red, upper_red)
        roi_res = cv2.bitwise_and(roi, roi, mask=roi_mask)
        return roi_res


def onchange(pos):
    try:
        global roi
        roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    except:
        pass

    else:
        roi_mask = cv2.inRange(roi_hsv, (-20, cv2.getTrackbarPos("saturation", "cropped"), cv2.getTrackbarPos("value", "cropped")), upper_red)
        roi_res = cv2.bitwise_and(roi, roi, mask=roi_mask)
        roi_res = cv2.resize(roi_res, (300, 300))

        cv2.imshow('cropped', roi_res)


# import img file
img = cv2.imread('test.jpg')

# Except img import err
if img is None:
    print('Image Load Failed!')

# Copy img (Deep copy)
dst = copy.deepcopy(img)
cv2.namedWindow("cropped")

# create trackbar
cv2.createTrackbar("saturation", "cropped", 0, 255, onchange)
cv2.createTrackbar("value", "cropped", 0, 255, onchange)

# default bar pos setting
cv2.setTrackbarPos("saturation", "cropped", 30)
cv2.setTrackbarPos("value", "cropped", 30)

roi = mask(img)

roi_res = cv2.resize(roi, (300, 300))
cv2.imshow('cropped', roi_res)
cv2.moveWindow('cropped', 0, 0)

cv2.waitKey()
cv2.destroyAllWindows()

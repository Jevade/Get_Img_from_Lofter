# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/6/4 11:11'
#import library - MUST use cv2 if using opencv_traincascade
import cv2

# rectangle color and stroke
color = (0,0,255)       # reverse of RGB (B,G,R) - weird
strokeWeight = 1        # thickness of outline

# set window name
windowName = "Object Detection"


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=10, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


cascade_fn = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_fn)

# load an image to search for faces
img = cv2.imread("/Users/liu/Downloads/download/3.jpg")

# load detection file (various files for different views and uses)
img_copy = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
rects = detect(gray, cascade)

print(rects)
# display until escape key is hit
while True:
    # get a list of rectangles
    for x,y, width,height in rects:
        cv2.rectangle(img_copy, (x,y), (x+width, y+height), color, strokeWeight)
    # display!
    cv2.imshow(windowName, img_copy)
    # escape key (ASCII 27) closes window
    if cv2.waitKey(20) == 27:
        break

# if esc key is hit, quit!
exit()
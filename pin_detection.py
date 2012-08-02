#!/usr/bin/env python
import os
import cv2
import cv2.cv as cv

"1343772283-HAAR-ALL-GAB-0.5-10000_5000"
"1343751055-HAAR-GAB-0.45-20000_10000"

cascade_fn = "cascades/1343845877-HAAR-ALL-GAB-0.5-3000_1500/cascade.xml"
in_image_fn  = "images/positives/pins-cropped.png"
out_image_fn = "images/detected.jpg"
cascade = cv2.CascadeClassifier(cascade_fn)

if os.path.exists(in_image_fn) & os.path.exists(cascade_fn):
    img = cv2.imread(in_image_fn)
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    gray = cv2.equalizeHist(gray)
    rectangles = cascade.detectMultiScale(img, scaleFactor=1.001, minNeighbors=1,
        flags=0|cv.CV_HAAR_SCALE_IMAGE,
        minSize=(60, 60), maxSize=(160, 160))

    print(rectangles)
    print(len(rectangles))

    for x, y, width, height in rectangles:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)
    cv2.imwrite(out_image_fn, img)
else:
    print("File not found")

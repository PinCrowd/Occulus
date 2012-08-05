#!/usr/bin/env python
import os
import cv2
import cv2.cv as cv


cascade_fn = "bowling-pins.xml"
in_image_fn  = "cropped.png"
out_image_fn = "images/detected.jpg"
cascade = cv2.CascadeClassifier(cascade_fn)

if os.path.exists(in_image_fn) & os.path.exists(cascade_fn):
    img = cv2.imread(in_image_fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    cv2.equalizeHist(gray, gray)

    rectangles = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1,
        flags=cv.CV_HAAR_SCALE_IMAGE|cv.CV_HAAR_DO_CANNY_PRUNING,
        minSize=(50, 50), maxSize=(130,130))

    print(rectangles)
    print(len(rectangles))

    for x, y, width, height in rectangles:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)
    cv2.imwrite(out_image_fn, img)
else:
    print("File not found")

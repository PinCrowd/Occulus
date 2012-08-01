#!/usr/bin/env python
import os
import numpy as np
import cv2
import cv2.cv as cv


cascade_fn = "lbpcascades/lbpcascade_frontalface.xml"
in_image_fn  = ""
out_image_fn = ""
cascade = cv2.CascadeClassifier(cascade_fn)
if os.path.exists(in_image_fn) & os.path.exists(cascade_fn):
    img = cv2.imread(in_image_fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rectangles = cascade.detectMultiScale(img, scaleFactor=1.001, minNeighbors=1,
        flags=0,
        minSize=(80, 80), maxSize=(160, 160))
    for x, y, width, height in rectangles:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)
    cv2.imwrite(out_image_fn, img)
else:
    print("File not found")

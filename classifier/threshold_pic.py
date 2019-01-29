#!/usr/bin/env python3
import cv2,sys

img = cv2.imread(sys.argv[1], 0)
img = cv2.medianBlur(img, 5)

threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
			cv2.THRESH_BINARY,11,2)

cv2.imwrite("threshold-" + sys.argv[1], threshold)

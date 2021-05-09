#! /usr/bin/env python3
import cv2
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame1 = camera.read()
    ret, frame2 = camera.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _ , thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Hemanth Camera',frame1)
    cv2.imshow('Hemanth Camera',frame2)

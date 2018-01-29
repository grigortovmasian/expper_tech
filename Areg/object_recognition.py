#!/usr/bin/python

import os
import cv2
import cv2.face
import numpy as np
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera

from head_movement import head_movement


class object_detection(object):
    def is_non_zero_file(self, path):  
        print(os.path.getsize(path))
        return os.path.isfile(path) and os.path.getsize(path) > 512

class face_detection(object_detection):

    def __init__(self, cp = "haarcascade_frontalface_default.xml"):
        self._cascadePath = cp
        self._cascade = cv2.CascadeClassifier(self._cascadePath)
        self._head_movement_top_down = head_movement(16, 2.0*1.7, 10.6/1.7)
        self._head_movement_left_right = head_movement(18, 2.0, 10.6)

    def __get_max_rect(self, up):
        X = int(0); Y = int(0); W = int(0); H = int(0)
        for(x, y, w, h) in up:
            if w > W:
                X = x; Y = y; W = w; H = h
        return {'X': X, 'Y': Y, 'W': W, 'H': H}

    def __in_area(self, width, rc):
        print (width)
        print (rc)
        return abs(((width - rc['W']) / width) * 100) < 80

    def __get_step(self, rc, width, height):
        if abs(width / 2 - rc['X'] + rc['W'] / 2) < 50:
            self._head_movement.MoveHead(True, 0.01)
            return "Up"
        if width - rc['X'] < width / 2:
            return "rights and up"
        return "left and up"

    def detect_runtime_and_move(self):
        camera = PiCamera()
        camera.resolution = (320, 240)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(320, 240))
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                im = frame.array
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                height, width = im.shape[:2]
                up = self._cascade.detectMultiScale(gray, 1.1, 8)
                rc = self.__get_max_rect(up)
                if self.__in_area(width, rc):
                    print("In Area")
                elif rc['W'] > 0:
                    print(self.__get_step(rc, width, height))
                cv2.rectangle(im, (rc['X'], rc['Y']), (rc['X'] + rc['W'], rc['Y'] + rc['H']), (0, 0, 255), 2)
                cv2.imshow('im', im) 
                cv2.waitKey(5)
                key = cv2.waitKey(1) & 0xFF
                rawCapture.truncate(0)
                if key == ord("q"):
                         break




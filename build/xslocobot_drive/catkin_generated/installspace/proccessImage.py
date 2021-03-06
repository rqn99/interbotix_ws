#!/usr/bin/env python3

# script that will pilot different functions on our robot 
import rospy
from sensor_msgs.msg import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cv_bridge import CvBridge

class colorImageGet:

    # constructor initializes object with empty maskImg field
    def __init__(self):
        self.maskImg = []
        self.maskGet = False
        self.data = []
        rospy.init_node('colorImageGet', anonymous=False)
        print('Color Image object initialized')

        

    #function responsbile for initializing subscriber node to pull sensor_msg
    def subscribeToColor(self,color):

        print('Subscribe to image_raw topic')
        
        # self.sub = rospy.Subscriber('/locobot/camera/color/image_raw', Image, self.colorCallBack)
        self.data = rospy.wait_for_message('/locobot/camera/color/image_raw', Image)
        self.colorCallBack(color)

    #call back that generates mask
    def colorCallBack(self,color):
        rospy.loginfo('CALLINGBACK')
        bridge = CvBridge()
        # load ros image to open cv type
        cv_image = bridge.imgmsg_to_cv2(self.data, desired_encoding='passthrough')
        HSV_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        maskColor = color

        # mask b [0,30] g[30,60] y[60,100] r[110+]
        if maskColor == 'r':
            lb=np.array([110,10,50])
            ub=np.array([180,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'y':
            lb=np.array([60,10,50])
            ub=np.array([100,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'g':
            lb=np.array([30,10,50])
            ub=np.array([60,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'b':
            lb=np.array([0,10,50])
            ub=np.array([30,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)

        #apply
        mask_img =np.uint8(cv2.bitwise_and(HSV_img,HSV_img, mask= mask))
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_HSV2BGR)
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
        [ret,thresh] = cv2.threshold(mask_img,5,255,cv2.THRESH_BINARY)
        
        self.maskImg = thresh
        print('showimg')
        cv2.imshow('window1',self.maskImg)
        cv2.waitKey()
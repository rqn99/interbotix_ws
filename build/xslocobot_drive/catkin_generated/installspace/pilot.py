#!/usr/bin/env python3

# script that will pilot different functions on our robot 
import rospy
from sensor_msgs.msg import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cv_bridge import CvBridge

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

# from goToPoint import odomGet
# from proccessImage import colorImageGet


## ---responsible for making masks--- ##
class colorImageGet:

    # constructor initializes object with empty maskImg field
    def __init__(self):
        self.maskImg = []
        self.maskGet = False
        self.data = []
        # rospy.init_node('colorImageGet', anonymous=False)
        print('Color Image object initialized')

        

    #function responsbile for initializing subscriber node to pull sensor_msg
    def subscribeToColor(self,color):

        print('Subscribe to image_raw topic')
        
        # self.sub = rospy.Subscriber('/locobot/camera/color/image_raw', Image, self.colorCallBack)
        self.data = rospy.wait_for_message('/locobot/camera/color/image_raw', Image)
        self.colorCallBack(color)
        

    #call back that generates mask
    def colorCallBack(self,color):
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
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB)
        # [ret,thresh] = cv2.threshold(mask_img,5,255,cv2.THRESH_BINARY)
        
        self.maskImg = mask_img
        print('showimg')


        cv2.imshow('window1',self.maskImg)
        cv2.waitKey()


## --- responsible for driving robot -- ##
class odomGet:

    #constructor
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.zpos = 0
        self.roll = 0
        self.pitch = 0
        
        self.sub = None
        self.pub = None

        self.linVel = 0.5
        self.angVel = 1
        

        # initialize node
        # rospy.init_node('PositionMeasurement', anonymous=False)
        self.r = rospy.Rate(10)
        self.pub = rospy.Publisher('/locobot/mobile_base/commands/velocity', Twist, queue_size=1)
        self.sub = rospy.wait_for_message('/locobot/odom', Odometry)
        self.odomCallback(self.sub)

        # what to call on shutdown
        rospy.on_shutdown(self.shutdown)


    # subscribes to get odom messages
    # publishes to velocity topic
    def subscribeToOdom(self):
        print('Subscribed')
        self.sub = rospy.Subscriber('/locobot/odom', Odometry, self.odomCallback)
        
        # self.sub = rospy.wait_for_message('/locobot/odom', Odometry)
        # self.odomCallback(self.sub)

    
    # call back to get data from odom msgs
    def odomCallback(self,msg):
        self.xpos = msg.pose.pose.position.x
        self.ypos = msg.pose.pose.position.y 

        rot_q = msg.pose.pose.orientation
        self.roll, self.pitch, self.theta = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])


    # function called to get to goal x y
    def goToGoal(self,x,y):
        
        speed = Twist() 
        turning = True
        inc_x = (x - self.xpos)
        inc_y = (y - self.ypos)


        thresh = 0.1

        # keep moving while not at goal
        while abs(inc_x) > thresh or abs(inc_y) > thresh:
            
            inc_x = (x - self.xpos)
            inc_y = (y - self.ypos)
            goalAngle = atan2(inc_y,inc_x)


            inc_theta = goalAngle - self.theta
            mod_theta = (inc_theta+(2*np.pi)) % (2*np.pi)
    
            

            # check our orientation and rotate to goal point
            if abs(inc_theta) > 0.1:
                # speed.linear.x = 0.0
                if mod_theta < np.pi and turning:
                    speed.angular.z = self.angVel
                    print('LEFT')
                    turning = False
                elif turning:
                    speed.angular.z = -self.angVel
                    print('RIGHT')
                    turning = False
            # else go to goal
            else:
                print('FORWARD')
                speed.linear.x = self.linVel
                speed.angular.z = 0.0
                turning = True
            
            self.pub.publish(speed)
            self.r.sleep()
        #stop moving
        self.pub.publish(Twist())

    def rotateToPoint(self,x,y):
        turning = True
        rotate = Twist()
        rotate.angular.z = 1
        inc_x = (x - self.xpos)
        inc_y = (y - self.ypos)
        goalAngle = atan2(inc_y,inc_x)
        inc_theta = goalAngle - self.theta
        while abs(inc_theta) > 0.1:
            
            inc_x = (x - self.xpos)
            inc_y = (y - self.ypos)

            goalAngle = atan2(inc_y,inc_x)
            inc_theta = goalAngle - self.theta
            mod_theta = (inc_theta+(2*np.pi)) % (2*np.pi)
    

            
            if mod_theta < np.pi and turning:
                rotate.angular.z = self.angVel
                print('LEFT')
                turning = False
            elif turning:
                rotate.angular.z = -self.angVel
                print('RIGHT')
                turning = False
            self.pub.publish(rotate)
            self.r.sleep()
        
        self.pub.publish(Twist())

    
    def shutdown(self):
        self.pub.publish(Twist())
        print('Interrupt command recieved')


# <--- OUT OF CLASS --> #


# def findContours(threshImg):
#     contours, _= cv2.findContours(threshImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#     cnt = contours[0]
#     M = cv2.moments(cnt)

#     x_cam = int(M['m10']/M['m00'])
#     y_cam = int(M['m01']/M['m00'])
#     print(x_cam)
#     print(y_cam)
#     print(threshImg.shape)
    

    

def main():
    # initialize master node for all objects
    rospy.init_node('PilotNode',anonymous=False)
    # go to desired point
    print('going to point')
    myOdom = odomGet()
    myOdom.subscribeToOdom()
    myOdom.goToGoal(1,1)
    myOdom.rotateToPoint(2,1)


   



if __name__ == '__main__':
    main()
    
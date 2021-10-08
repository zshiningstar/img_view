#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge

def img_pub():

     rospy.init_node('img_pub', anonymous=True)
     mid = rospy.get_param('camera_id','1')
     is_view_incv = rospy.get_param('is_view_incv','false')
     pub = rospy.Publisher('/image', Image, queue_size=10)
     
     rate = rospy.Rate(30)
     
     bridge = CvBridge()
     Video = cv2.VideoCapture(int(mid))
     
     while not rospy.is_shutdown():
     
         ret, img = Video.read()
         if is_view_incv:
             cv2.imshow("img_pub", img)
         cv2.waitKey(3)
         pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
         rate.sleep()

if __name__ == '__main__':
     try:
         img_pub()
     except rospy.ROSInterruptException:
         pass
         


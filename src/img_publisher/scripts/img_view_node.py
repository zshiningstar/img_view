#!/usr/bin/env python

import rospy
import cv2
import sys

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImgPub:
	def __init__(self):
		self.bridge = CvBridge()
		self.camera_id = rospy.get_param('camera_id', '0')
		self.is_view_incv = rospy.get_param('is_view_incv', 'False')

def init():
	rospy.init_node('img_pub_node', anonymous = True)
	return True

def run():
	img_pub = ImgPub()
	m_pub = rospy.Publisher('/image', Image, queue_size = 10)
	Video = cv2.VideoCapture(int(img_pub.camera_id))
	rate = rospy.Rate(30)
	while not rospy.is_shutdown():
		ret, img = Video.read()
		if img_pub.is_view_incv:
			cv2.imshow("img_view", img)
		cv2.waitKey(4)
		m_pub.publish(img_pub.bridge.cv2_to_imgmsg(img, "bgr8"))
		rate.sleep()

def main(args):
	if init():
		run()
		
if __name__ == '__main__':
	main(sys.argv)


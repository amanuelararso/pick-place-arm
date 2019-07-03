#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Int32
from time import sleep

def go_place(msg):
	if msg.data=='Place':
		pub_gripper.publish('place')	
		sleep(2)	
		pub_done.publish('Place_Done')
		sleep(25)

if __name__=="__main__":
	rospy.init_node('place')
	rate=rospy.Rate(2)

	pub_done=rospy.Publisher('currently', String, queue_size=1)
	pub_gripper = rospy.Publisher('grip', String, queue_size=1)
	while not rospy.is_shutdown():
		sub=rospy.Subscriber('goal', String, go_place)
		rate.sleep()


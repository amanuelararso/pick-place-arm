#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from time import sleep

def go_pick(msg):
	if msg.data=='Pick':
		pub_gripper.publish('pick')
		sleep(2)
		pub_done.publish('Pick_Done')
		sleep(25)

if __name__=="__main__":
	rospy.init_node('pick')
	rate=rospy.Rate(2)

	pub_done=rospy.Publisher('currently', String, queue_size=1)
	pub_gripper = rospy.Publisher('grip', String, queue_size=1)
	
	while not rospy.is_shutdown():	
		sub=rospy.Subscriber('goal', String, go_pick)
		rate.sleep()




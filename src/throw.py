#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float32, Int32
from time import sleep
if __name__=="__main__":
	rospy.init_node('throw')
	rate=rospy.Rate(2)
	pub_theta1 = rospy.Publisher('theta1', Float32, queue_size=1)
	pub_theta2 = rospy.Publisher('theta2', Float32, queue_size=1)
	pub_gripper = rospy.Publisher('grip', Int32, queue_size=1)
	
	sleep(1)
	
 	pub_theta1.publish(0)
 	sleep(1)
 	pub_theta2.publish(170)
 	sleep(1)
 	pub_gripper.publish(30)
 	sleep(1)
	
	pub_theta2.publish(140)
	sleep(1)
	pub_gripper.publish(80)
	sleep(1)	
		
	pub_theta2.publish(170)
	sleep(1)	
	pub_theta1.publish(60)
	sleep(1)
	pub_gripper.publish(30)
	sleep(1)
		

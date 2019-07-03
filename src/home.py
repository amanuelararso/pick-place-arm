#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float32
from time import sleep
 
def go_home(msg):
	if msg.data=='Home':
		pub_theta1.publish(0.0)		
		pub_theta2.publish(160.0)
		
		sleep(2)
		pub_done.publish('Home_Done')
		#pub_done.unregister()
		sleep(115)

if __name__=="__main__":
	rospy.init_node('home')
	rate=rospy.Rate(2)

	pub_theta1 = rospy.Publisher('theta1', Float32, queue_size=1)
	pub_theta2 = rospy.Publisher('theta2', Float32, queue_size=1)
	pub_done=rospy.Publisher('currently', String, queue_size=1)
	while not rospy.is_shutdown():
		sub=rospy.Subscriber('goal', String, go_home)
		rate.sleep()

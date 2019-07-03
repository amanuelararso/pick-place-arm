#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float32
from time import sleep
import sys

def command(msg):

	if msg.data=='Home_Done':
		while msg.data=='Home_Done':
		 	print 'The Robot is in Home Position' 
			sleep(2)
			rospy.signal_shutdown("shutdown")
		sleep(1000)
			
	elif msg.data=='S_Cylinder_Done':
		while msg.data=='S_Cylinder_Done':
			pub.publish('Pick') # sending Pick to /goal topic			
			sleep(10)		
		
	elif msg.data=='Pick_Done':		
		while msg.data=='Pick_Done':	
			pub.publish('Water') 	# sending Water to /goal topic			
			sleep(10)

	elif msg.data== 'Water_Done':		
		while msg.data=='Water_Done':
			pub.publish('E_Cylinder') # sending Cylinder2 to /goal topic			
			sleep(10)

	elif msg.data=='E_Cylinder_Done':		
		while msg.data=='E_Cylinder_Done':
			pub.publish('Place') 	# sending Place to /goal topic
			sleep(10)

	elif msg.data=='Place_Done':		
		while msg.data=='Place_Done':
			pub.publish('Home') 	# sending Home to /goal topic
			sleep(10)

if __name__=="__main__":
	rospy.init_node('contol', disable_signals=True)
	rate=rospy.Rate(2)

	pub=rospy.Publisher('goal', String, queue_size=1)
	pub_theta1 = rospy.Publisher('theta1', Float32, queue_size=1)
	pub_theta2 = rospy.Publisher('theta2', Float32, queue_size=1)
	pub_gripper = rospy.Publisher('grip', String, queue_size=1)
	

	pub_theta1.publish(0.0)
	pub_theta2.publish(170.0)
	pub_gripper.publish('open')
	start=raw_input('Enter start to start the robot: ')
	if start=='start':
		pub.publish('S_Cylinder')
	
	while not rospy.is_shutdown():
		sub=rospy.Subscriber('currently', String, command)
		rate.sleep()


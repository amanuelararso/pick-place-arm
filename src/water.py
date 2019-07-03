#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float32, Int32
from time import sleep
from thesisproject.srv import IK

def go_to_water(msg):
	# cylinder position
	x0_2=18.0
	y0_2=15.5
	z0_2=24.5

	if msg.data=='Water':
		rospy.wait_for_service('ik_solver')
                service=rospy.ServiceProxy('ik_solver', IK)
		theta=service(x0_2,y0_2,z0_2)
                #since the elbow joint angle doesnot start from 0, it has to be mapped for the hardware compatibility 
		theta.T2=150+theta.T2+20
		pub_theta1.publish(theta.T1)
		pub_theta2.publish(theta.T2)
		sleep(5) # 2 sec for execution and 3 sec for staying at this position 		
		pub_done.publish('Water_Done')
		#pub_done.unregister()
		sleep(25)

if __name__=="__main__":
	rospy.init_node('water')
	rate=rospy.Rate(2)
	pub_theta1 = rospy.Publisher('theta1', Float32, queue_size=1)
	pub_theta2 = rospy.Publisher('theta2', Float32, queue_size=1)
	pub_done=rospy.Publisher('currently', String, queue_size=1)
	
	while not rospy.is_shutdown():
		sub=rospy.Subscriber('goal', String, go_to_water)

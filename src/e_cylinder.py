#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float32, Int32
from thesisproject.srv import IK
from time import sleep
def go_to_cylinder(msg):
	
	# cylinder position
	x0_2=21.0
	y0_2=0.0
	z0_2=12.0
	
	if msg.data=='E_Cylinder':
		rospy.wait_for_service('ik_solver')
		service=rospy.ServiceProxy('ik_solver', IK)
		theta=service(x0_2,y0_2,z0_2) 
		#since the elbow joint angle doesnot start from 0, it has to be mapped for the hardware compatibility	
		theta.T2=150+theta.T2+10
		pub_theta1.publish(theta.T1)
		pub_theta2.publish(theta.T2)
		sleep(2)
		pub_done.publish('E_Cylinder_Done')
		#pub_done.unregister
		sleep(25)

if __name__=="__main__":
	rospy.init_node('e_cylinder')
	rate=rospy.Rate(2)
	pub_theta1 = rospy.Publisher('theta1', Float32, queue_size=1)
	pub_theta2 = rospy.Publisher('theta2', Float32, queue_size=1)
	pub_gripper = rospy.Publisher('grip', String, queue_size=1)
	pub_done=rospy.Publisher('currently', String, queue_size=1)
	
	while not rospy.is_shutdown():
		sub=rospy.Subscriber('goal', String, go_to_cylinder)
		rate.sleep()	

#! /usr/bin/env python

import rospy
from std_msgs.msg import String, Float32, Int32
from thesisproject.srv import IK
from time import sleep
import sys

def go_to_cylinder(msg):
   	
  	 # cylinder position
   	x0_2=18.0
   	y0_2=0.0
   	z0_2=12.0

   	if msg.data=='S_Cylinder':
	   	rospy.wait_for_service('ik_solver')
		service=rospy.ServiceProxy('ik_solver', IK)
		theta=service(x0_2,y0_2,z0_2) 
		pub_gripper.publish('open') # open the gripper
		sleep(1)
		#since the elbow joint angle does not start from 0, it has to be mapped for the hardware compatibility 
		theta.T2=150+theta.T2+10
		pub_theta1.publish(theta.T1)
		
		pub_theta2.publish(theta.T2)
		sleep(2)
		 # waiting it to execute and finish 
		pub_done.publish('S_Cylinder_Done')
		#pub_done.unregister()
		sleep(3)
		rospy.signal_shutdown("shutdown")

if __name__=="__main__":
	
	rospy.init_node('s_cylinder', disable_signals=True)
	rate=rospy.Rate(2)

	pub_theta1 = rospy.Publisher('theta1', Float32, queue_size=1)
	pub_theta2 = rospy.Publisher('theta2', Float32, queue_size=1)
	pub_gripper = rospy.Publisher('grip', String, queue_size=1)
	pub_done=rospy.Publisher('currently', String, queue_size=1)
	
	while not rospy.is_shutdown():
		sub=rospy.Subscriber('goal', String, go_to_cylinder)
		rate.sleep()

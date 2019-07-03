#! /usr/bin/env python

import rospy
import math
from thesisproject.srv import IK


#this is a server for ik solving
#this node is called as a node wants an inverse kinematics
def ik_solver(req):
	T1=T2=0.0
	a1=26.4 
	a2=23.8

	T1=math.degrees(math.atan(req.y0_2/req.x0_2))
	T2=math.degrees(math.atan((req.z0_2-a1)/(math.sqrt((a2*a2)-(req.z0_2-a1*a1)))))

	t=[T1,T2]

	return t

def ik_solver_server():
	rospy.init_node('ik_solver_server')

	s=rospy.Service('ik_solver', IK, ik_solver)

	rospy.spin()

if __name__=="__main__":
	ik_solver_server()


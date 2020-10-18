#!/usr/bin/env python
# the above line tells the computer which interpreter to use

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import PoseArray

def pose_callback(msg):
	pos[0] = msg.poses[0].position.x
	pos[1] = msg.poses[0].position.y
	pos[2] = msg.poses[0].position.z


if __name__ == '__main__':

	# initializing the node
	rospy.init_node('parker',anonymous=False)

	pos = [0,0,0]
	error = 0.2
	target = 3
	whycon_sub = rospy.Subscriber('/whycon/poses',PoseArray,pose_callback)

	rightFrontWheel = rospy.Publisher('/foxbot2/right_front_wheel_controller/command',Float64,queue_size=10)
	rightBackWheel = rospy.Publisher('/foxbot2/right_back_wheel_controller/command',Float64,queue_size=10)
	leftFrontWheel = rospy.Publisher('/foxbot2/left_front_wheel_controller/command',Float64,queue_size=10)
	leftBackWheel = rospy.Publisher('/foxbot2/left_back_wheel_controller/command',Float64,queue_size=10)

	r = rospy.Rate(30)
	while not rospy.is_shutdown():
		rightFrontWheel.publish(5.0)
		rightBackWheel.publish(5.0)
		leftFrontWheel.publish(5.0)
		leftBackWheel.publish(5.0)
		if pos[0]>target-error and pos[0]<target+error:
			rightFrontWheel.publish(0.0)
			rightBackWheel.publish(0.0)
			leftFrontWheel.publish(0.0)
			leftBackWheel.publish(0.0)
			break




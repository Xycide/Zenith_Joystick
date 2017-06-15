#!/usr/bin/python
# coding: utf-8

import rospy
import tf.transformations
import Joy
from geometry_msgs.msg import Twist
#reverse: address 128 motor 2 and address 129 motor 2
#function to scale values in one range to values in another range -  proportional scaling
def pscale(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def callback(msg):
	if(msg.axes[5] <= 0.97):
		linear = msg.axes[5]
	elif(msg.axes[2] <= 0.97):
		linear = msg.axes[2]
	
	angular = msg.axes[0]

	if(angular < 0):
		#right is negative
		v1 = linear - angular
        	v2 = linear
	elif(angular > 0):
		#left is positive
		v1 = linear
		v2 = linear - angular

	if(v1 > 127) {
		temp = v1 - 127
		v2 = v2 + temp
		v1 = 127
	}
	if(v1 < -127)
		temp = 


def listener():

    rospy.init_node('TriggerJoystick') #anonymous=true would allow us to run multiple of these motor interpreters at once

    rospy.Subscriber("zenith/cmd_vel", Twist, callback,queue_size = 2)
    #rospy.Subscriber("cmd_vel",Twist,callback,queue_size = 2)
    rospy.spin() #keeps python from exiting until node is stopped

if __name__ == '__main__':
    listener()

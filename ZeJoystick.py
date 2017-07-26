#!/usr/bin/python
# coding: utf-8

import rospy
import tf.transformations
from sensor_msgs import Joy
from geometry_msgs.msg import Twist
#reverse: address 128 motor 2 and address 129 motor 2
#function to scale values in one range to values in another range -  proportional scaling
def pscale(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def callback(msg):

    pub = rospy.Publisher('zenith/cmd_vel', Twist, queue_size = 1)


    tVals = Twist()
    tVals.linear.x = 0
    tVals.angular.z = 0
    if(msg.axes[5] <= 0.97):
		tVals.linear.x = msg.axes[5]
    elif(msg.axes[2] <= 0.97):
        tVals.linear.x = msg.axes[2]

	tVals.angular.z = msg.axes[0]

    pub.publish(tVals)


def listener():

    rospy.init_node('TriggerJoystick') #anonymous=true would allow us to run multiple of these motor interpreters at once

    rospy.Subscriber("/joy", Joy, callback, queue_size = 2)
    #rospy.Subscriber("cmd_vel",Twist,callback,queue_size = 2)
    rospy.spin() #keeps python from exiting until node is stopped


if __name__ == '__main__':
    listener()

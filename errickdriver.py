#!/usr/bin/python
# coding: utf-8

import rospy
import serial
import tf.transformations
import Joy
from geometry_msgs.msg
#reverse: address 128 motor 2 and address 129 motor 2
address1 = 129
address2 = 128
#function to scale values in one range to values in another range -  proportional scaling
def pscale(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def motor1speed(address,speed):
    port = serial.Serial('/dev/ttyUSB0')
    if(speed > 127):
        speed = 127
    if(speed < 0):
        speed = 0
    port.isOpen()
    command1 = 6
    command2 = 7
    checksum1 = (address + command1 + speed) & 127
    checksum2 = (address + command2 + pscale(speed,0,127,127,0)) & 127
    #print("Left Speed: " + str(speed))
    port.write("".join(chr(i) for i in [address, 14, 10, (address + 24) & 127]))
    port.write("".join(chr(i) for i in [address, command1, speed, checksum1]))
    port.write("".join(chr(i) for i in [address, command2, pscale(speed,0,127,127,0), checksum2]))

def callback(msg):


def listener():

    rospy.init_node('sabertooth_driver') #anonymous=true would allow us to run multiple of these motor interpreters at once

    rospy.Subscriber("zenith/cmd_vel", Twist, callback,queue_size = 2)
    #rospy.Subscriber("cmd_vel",Twist,callback,queue_size = 2)
    rospy.spin() #keeps python from exiting until node is stopped

if __name__ == '__main__':
    listener()

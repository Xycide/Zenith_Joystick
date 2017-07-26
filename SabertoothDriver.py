from geometry_msgs.msg import Twist
import pyserial
import rospy

def speaker():

    if(angular < 0):
		#right is negative
		v1 = linear - angular
    	v2 = linear
	elif(angular > 0):
		#left is positive
		v1 = linear
		v2 = linear - angular

	if(v1 > 127):
		temp = v1 - 127
        if(v2 + temp <= 127):
            v2 = v2 + temp
        else:
            v2 = 127
		v1 = 127

	if(v1 < -127):
		temp = v1 + 127
        if (v2 + temp >= -127):
            v2 = v2 + temp
        else:
            v2 = -127
        v1 = -127

    if (v2 > 127):
        temp = v2 - 127
        if (v1 + temp <= 127):
            v1 = v1 + temp
        else:
            v1 = 127
        v2 = 127

    if (v2 < -127):
        temp = v2 + 127
        if(v1 >= -127):
            v1 = v1 + temp
        else:
            v1 = -127
        v2 = -127





def listener():

    rospy.init_node('TriggerJoystick') #anonymous=true would allow us to run multiple of these motor interpreters at once

    rospy.Subscriber("zenith/cmd_vel", Twist, callback,queue_size = 2)
    #rospy.Subscriber("cmd_vel",Twist,callback,queue_size = 2)
    rospy.spin() #keeps python from exiting until node is stopped

if __name__ == '__main__':
    listener()

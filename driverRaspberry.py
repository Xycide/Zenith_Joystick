import rospy
import serial
import time
port = serial.Serial("/dev/ttyUSB0", baudrate = 115200)

command = ""

from sensor_msgs.msg import Joy

leftArr = [':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
rightArr = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c']

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

	scaledv1 = int(pscale(v1,-1.0,1.0,0,20))
        scaledv2 = int(pscale(v2,-1.0,1.0,0,20))

	print(v1)
	print(v2)
	print(scaledv1)
	print(scaledv2)
	print(leftArr[scaledv1])
	print(rightArr[scaledv2])
	
	command = "0"
	command += leftArr[scaledv1]
	command += rightArr[scaledv2]
	command += "!"
	print(command)

	print(" ")
	port.isOpen()
 0):
                
'''def callback(msg):
	S = 3
	v1 = msg.linear.x - msg.angular.z * S
	v2 = msg.linear.x + msg.angular.z * S
	scaledv1 = pscale(v1,-1.8,1.8,0,19)
	scaledv2 = pscale(v2,-1.8,1.8,0,19)
	print(v1)
	print(v2)
	print(scaledv1)
	print(scaledv2)
	print(leftArr[int(scaledv1)])
	print(rightArr[int(scaledv2)])
	command = "0"
	command += leftArr[int(scaledv1)]
	command += rightArr[int(scaledv2)]
	command += "!"
	print(command)
	print(" ")
	port.isOpen()
	port.write(command)
	sleep(.05)'''
def millis():
	return int(round(time.time()*1000))
def listener():
	dt = 200
	tn = 0
	ts = 0
	rospy.init_node('driver')
	rospy.Subscriber("joy", Joy, callback,queue_size = 1)
	#rospy.Subscriber("joy", Joy, callback,queue_size = 1)
        tn = millis()
       	ts = millis()
        count = 0
        flag = 0
	#FIX THIS |
	#         V
	while(1):
	        tn = millis()
                if(tn - ts > dt):
                    	print command
                       	port.isOpen()
                       	port.write(command)
                       	ts = millis()
                       	if(not flag):
                              	count = count + 1
                       	else:
                               	count = count - 1
	                if(count == 20 or count == 0):
        	                flag = (flag+1)%2
		rospy.spin()

if __name__ == '__main__':
	listener()

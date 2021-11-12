#!/usr/bin/env python
# license removed for brevity
from re import I
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from std_msgs.msg import UInt8
from geometry_msgs.msg import Twist
import math
import time



def talker():
    commands = {
        'takeoff' : [None, '/tello/takeoff', Empty],
        'land' : [None, '/tello/land',Empty],
        'emergency' : [None, '/tello/emergency', Empty],
        'fast_mode' : [None, '/tello/fast_mode', Empty],
        'flattrim' : [None, '/tello/flattrimm', Empty],
        'flip' : [None, '/tello/flip', UInt8],
        'palm_land' : [None, '/tello/palm_land', Empty],
        'throw_takeoff' : [None, '/tello/throw_takeoff', Empty],
        'position' : [None, '/tello/cmd_vel', Twist]

    }

    rospy.init_node('controler', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cm = raw_input('INPUT COMMAND : ')

        for i in commands:
            if cm == i: # Empty Type
                topic = commands[cm][1]
                type = commands[cm][2]
                pub = rospy.Publisher(topic, type, queue_size=10)
                pub.publish()
                break

            elif 'flip' in cm:  #flip
                cm_list = cm.split()
                pub = rospy.Publisher('/tello/flip', UInt8, queue_size=10)
                pub.publish(int(cm_list[1]) )
                break

            elif any(chr.isdigit() for chr in cm): # other
                cm_list = cm.split()
                type = cm_list[0]   # linear or angular
                dire = cm_list[1]   # direction
                scale = float(cm_list[2])  # scale

                twist = Twist()

                if cm_list[0] == 'l':   # linear
                    velo = 50.0 * (scale/abs(scale))
                    t = scale/velo

                    if cm_list[1] == 'x':
                        twist.linear.x = velo
                    elif cm_list[1] == 'y':
                        twist.linear.y = velo
                    elif cm_list[1] == 'z':
                        twist.linear.z = velo
                    pub = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=10)
                    pub.publish(twist)
                    time.sleep(t)
                    twist.linear.x = twist.linear.y = twist.linear.z = 0.0
                    pub.publish(twist)
                    break

        
                elif cm_list[0] == 'a':   # angular
                    velo = 2/math.pi * (scale/abs(scale))
                    t = (scale/180*math.pi)/velo

                    if cm_list[1] == 'x':
                        twist.angular.x = velo
                    elif cm_list[1] == 'y':
                        twist.angular.y = velo
                    elif cm_list[1] == 'z':
                        twist.angular.z = velo
                    pub = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=10)
                    pub.publish(twist)
                    time.sleep(t)
                    twist.angular.x = twist.angular.y = twist.angular.z = 0.0
                    pub.publish(twist)
                    break
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
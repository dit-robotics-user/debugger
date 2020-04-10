#!/usr/bin/env python
import rospy
from std_msgs.msg import *

def txST1_callback(data):
    rospy.loginfo("txST1: ", data.data)

def txST2_callback(data):
    rospy.loginfo("txST2: ", data.data)

def rxST1_callback(data):
    rospy.loginfo("rxST1", data.data)

def rxST2_callback(data):
    rospy.loginfo("rxST2", data.data)

def success_rate1_callback(data):
    rospy.loginfo("success_rate", data.data)

def success_rate2_callback(data):
    rospy.loginfo("success_rate2", data.data)


def listener():

    rospy.init_node('debugger', anonymous=True)

    txST1_sub = rospy.Subscriber('/txST1', Int32MultiArray, txST1_callback)
    rxST1_sub = rospy.Subscriber('/rxST1', Int32MultiArray, rxST1_callback)
    rate1_sub = rospy.Subscriber('/success_rate', Int32, success_rate1_callback)

    txST2_sub = rospy.Subscriber('/txST2', Int32MultiArray, txST1_callback)
    rxST2_sub = rospy.Subscriber('/rxST2', Int32MultiArray, rxST1_callback)
    rate2_sub = rospy.Subscriber('/success_rate_2', Int32, success_rate1_callback)

    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

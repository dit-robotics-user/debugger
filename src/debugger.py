#!/usr/bin/env python
import rospy
from std_msgs.msg import *
import time

txST1_str = ""
txST2_str = ""
rxST1_str = ""
rxST2_str = ""
rate1_str = ""
rate2_str = ""
pi2ST1_rate_str = ""
pi2ST2_rate_str = ""

def txST1_callback(data):
    global txST1_str
    txST1_str = "txST1: " + str(data.data)

def txST2_callback(data):
    global txST2_str
    txST2_str = "txST2: " + str(data.data)

def rxST1_callback(data):
    global rxST1_str
    rxST1_str = "rxST1: " + str(data.data)

def rxST2_callback(data):
    global rxST2_str
    rxST2_str = "rxST2: " + str(data.data)

def success_rate1_callback(data):
    global rate1_str
    rate1_str = "ST to Pi rate1: " + str(data.data)

def success_rate2_callback(data):
    global rate2_str
    rate2_str = "ST to Pi rate2: " + str(data.data)

def pi2ST1_rate_callback(data):
    global pi2ST1_rate_str
    pi2ST1_rate_str = "Pi to ST rate1: " + str(data.data)

def pi2ST2_rate_callback(data):
    global pi2ST2_rate_str
    pi2ST2_rate_str = "Pi to ST rate2: " + str(data.data)

txST1_sub = rospy.Subscriber('/txST1', Int32MultiArray, txST1_callback)
rxST1_sub = rospy.Subscriber('/rxST1', Int32MultiArray, rxST1_callback)
rate1_sub = rospy.Subscriber('/success_rate', Int32, success_rate1_callback)
pi2ST1_sub = rospy.Subscriber('/pi2ST1_rate', Int32, pi2ST1_rate_callback)

txST2_sub = rospy.Subscriber('/txST2', Int32MultiArray, txST2_callback)
rxST2_sub = rospy.Subscriber('/rxST2', Int32MultiArray, rxST2_callback)
rate2_sub = rospy.Subscriber('/success_rate2', Int32, success_rate2_callback)
pi2ST2_sub = rospy.Subscriber('/pi2ST2_rate', Int32, pi2ST2_rate_callback)
    
def listener():

    rospy.init_node('debugger', anonymous=True)
    global txST1_str
    global txST2_str
    global rxST1_str
    global rxST2_str
    global rate1_str
    global rate2_str
    global pi2ST1_rate_str
    global pi2ST2_rate_str
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        starttime = time.time()
        print(txST1_str)
        print(rxST1_str)
        print(rate1_str)
        print(pi2ST1_rate_str)
        print(txST2_str)
        print(rxST2_str)
        print(rate2_str)
        print(pi2ST2_rate_str)
        rate.sleep()
        nowtime = time.time()
        print("the loop takes %.2f seconds\n" % (nowtime-starttime))


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

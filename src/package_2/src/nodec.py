#!/usr/bin/env python

# Imports we need for python code
import rospy

# you don't need these, it's here just to show you that you can also import
# message libraries already provided by ROS (granted they are in the package.xml and CMake)
import geometry_msgs
from geometry_msgs.msg import Accel # this is preferrred

import std_msgs

# Import custom messages (from <package_containing_message> import <message_name>)
from package_1.msg import Custom

class NodeC:
    '''
    Node C is a subsriber node.

    It reads the messages coming from Node A and Node B, and simply outputs the values of both messages
    '''
    def __init__(self):
        # Again, setting and grabbing all the params we need
        # Needed for subscribers
        custom_message_topic_name = rospy.get_param('custom_message_topic_name', 
            '/default_custom_message_topic_name')
        accel_topic_name = rospy.get_param('accel_topic_name', '/default_accel_topic_name')
       
        self.queue_size = 10

        # Initialize any ROS constructs
        # Subscribes to Node A's publisher
        self.custom_message_subscriber = rospy.Subscriber(custom_message_topic_name, Custom, 
            self.custom_message_callback, queue_size=self.queue_size)
        # Subscribes to Node B's publisher
        self.accel_publisher = rospy.Subscriber(accel_topic_name, Accel, self.accel_callback, 
            queue_size = self.queue_size)

        rospy.loginfo("initialization complete")

        return

    # This function will run everytime Node C gets a message from Node A
    def custom_message_callback(self, msg): 
        # When Node C gets the custom message, its contents are found in the 'msg' object
        rospy.loginfo("Received from A (%s, %s, %s) and message: %s", msg.coordinate.x, 
            msg.coordinate.y, msg.coordinate.z, msg.message)

        return

    # This function will run everytime Node C gets a message from Node B
    def accel_callback(self, msg):
        # When Node C gets the custom message, its contents are found in the 'msg' object
        rospy.loginfo("Received from B l accel(%s, %s, %s) and a accel (%s, %s, %s)", 
            msg.linear.x, msg.linear.y, msg.linear.z, msg.angular.x, msg.angular.y, msg.angular.z)

        return

if __name__ == '__main__':
    # Initialize Node C
    rospy.init_node('node_c')

    # Spawn class and let it do its thing
    try:
        na =  NodeC()
        rospy.spin()

    except rospy.ROSInterruptException: pass
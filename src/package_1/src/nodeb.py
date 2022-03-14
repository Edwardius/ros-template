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

class NodeB:
    '''
    Node B is both a subscriber and publisher node.

    It reads the messages coming from Node A and publishes a message of its own using
    one of ROS's included messages from geometry msgs (Accel). This is to show you that
    a node can be both a Publisher AND Subscriber, the sky is the limit!

    Another thing to keep in mind is that Node B publishes in response to Node A.
    This is because Node B publishes on every call of the Subscriber callback.
    '''
    def __init__(self):
        # Again, setting and grabbing all the params we need
        # Needed for subscriber
        custom_message_topic_name = rospy.get_param('custom_message_topic_name', 
            '/default_custom_message_topic_name')
        # Needed for publisher
        accel_topic_name = rospy.get_param('accel_topic_name', '/default_accel_topic_name')
        self.x = float(rospy.get_param('~x', '2.0'))
        self.y = float(rospy.get_param('~y', '2.0'))
        self.z = float(rospy.get_param('~z', '2.0'))

        self.queue_size = 10

        rospy.loginfo("from params got (%s, %s, %s) and %s", self.x, self.y, self.z,
            accel_topic_name)

        # Initialize any ROS constructs
        self.accel_publisher = rospy.Publisher(accel_topic_name, Accel, queue_size = self.queue_size)
        self.custom_message_subscriber = rospy.Subscriber(custom_message_topic_name, Custom, 
            self.custom_message_callback, queue_size=self.queue_size)

        rospy.loginfo("initialization complete")

        return

    # This function will run everytime Node B gets a message from Node A
    def custom_message_callback(self, msg): 
        # When Node B gets the custom message, its contents are found in the 'msg' object
        rospy.loginfo("Received (%s, %s, %s) and message: %s", msg.coordinate.x, 
            msg.coordinate.y, msg.coordinate.z, msg.message)
            
        # initialize message variables
        accel_message = Accel()

        # fill message and publish in response to Node A
        # Linear Accel is filled by the values we sent from Node A
        accel_message.linear.x = msg.coordinate.x
        accel_message.linear.y = msg.coordinate.y
        accel_message.linear.z = msg.coordinate.z
        # Angular Accel is filled by the values fed from Node B's Params
        accel_message.angular.x = self.x
        accel_message.angular.y = self.y
        accel_message.angular.z = self.z

        rospy.loginfo("publishing...")
        self.accel_publisher.publish(accel_message)

        return

if __name__ == '__main__':
    # Initialize Node B
    rospy.init_node('node_b')

    # Spawn class and let it do its thing
    try:
        na =  NodeB()
        rospy.spin()

    except rospy.ROSInterruptException: pass
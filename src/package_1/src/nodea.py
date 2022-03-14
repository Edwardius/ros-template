#!/usr/bin/env python

# All Python code should follow PEP 8, but this is a design team so who cares...
# Generally Speaking:
#   - package_name
#   - ClassName
#   - method_name
#   - field_name
#   - _private_something
#   - self.__really_private_fielda
#   - _global
# http://wiki.ros.org/PyStyleGuide

# Imports we need for python code
import rospy

# you don't need these, it's here just to show you that you can also import
# message libraries already provided by ROS (granted they are in the package.xml and CMake)
import geometry_msgs
import std_msgs

# Import custom messages (from <package_containing_message> import <message_name>)
from package_1.msg import Custom

class NodeA:
    ''' 
    Node A is a publisher node. 

    It manifests a message and sends it into the 
    ROS system via a ROSTopic. There, other nodes can subscribe to the topic and
    read the messages sent by Node A.
    '''
    def __init__(self):
        # Grab any parameters we need for this node 
        # Can either come from the launchfile or not important enough so just set them
        # http://wiki.ros.org/Parameter%20Server
        custom_message_topic_name = rospy.get_param('custom_message_topic_name', 
            '/default_custom_message_topic_name')
        self.x = float(rospy.get_param('~x', '1.0'))
        self.y = float(rospy.get_param('~y', '1.0'))
        self.z = float(rospy.get_param('~z', '1.0'))

        self.message = "Eddy is a great teacher c:"

        self.queue_size = 10
        self.period = 3

        # Logging is good for debugging and to let others know what's wrong with your code
        # http://wiki.ros.org/rospy/Overview/Logging
        rospy.loginfo("from params got (%s, %s, %s) and %s", self.x, self.y, self.z,
            custom_message_topic_name)

        # Initialize any ROS constructs
        # http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
        self.custom_message_publisher = rospy.Publisher(custom_message_topic_name, Custom, queue_size = self.queue_size)

        rospy.loginfo("initialization complete")
        # Begin publishing
        self.publish_custom_message()

        return

    def publish_custom_message(self):
        # initialize message variables
        custom_message = Custom()

        # Node A will continue to publish the same message every 3 seconds
        # until you shutdown the node
        while not rospy.is_shutdown():
            # Fill the header of the message
            # http://docs.ros.org/en/lunar/api/std_msgs/html/msg/Header.html
            # you may be instructed to fill these out differently
            custom_message.header.stamp = rospy.get_rostime() 
            custom_message.header.frame_id = 'original message from Node A'

            # Fill the rest of the message
            custom_message.coordinate.x = self.x
            custom_message.coordinate.y = self.y
            custom_message.coordinate.z = self.z
            custom_message.message = self.message

            # Publish
            rospy.loginfo("publishing...")
            self.custom_message_publisher.publish(custom_message)
            
            # Sleep for a specified amount of time before publishing again
            rospy.sleep(self.period)

        rospy.loginfo("stopping...")
        return

if __name__ == '__main__':
    # Initialize Node A
    rospy.init_node('node_a')

    # Spawn class and let it do its thing
    try:
        na =  NodeA()
    except rospy.ROSInterruptException: pass
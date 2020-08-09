#! /usr/bin/env python
import rospy
import tf
import geometry_msgs.msg


if __name__ == "__main__":

    rospy.init_node("trans_listener")

    listener = tf.TransformListener()
    listener.waitForTransform("RightShoulderRoll_link","RightShoulderPitch_link", rospy.Time(), rospy.Duration(4.0))



    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:

            (translation, rotation) = listener.lookupTransform(
                "RightShoulderRoll_link","RightShoulderPitch_link", rospy.Time(0))
            print("rotation right shoulder pitch to right shoulder roll:", rotation, "\n")
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rate.sleep()
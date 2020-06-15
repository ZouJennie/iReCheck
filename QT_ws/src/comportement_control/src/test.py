import rospy
from std_msgs.msg import String

# create a publisher
rospy.init_node('test', anonymous=True)
speechSay_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)

# publish a text message to TTS (non-blocking)
speechSay_pub.publish("Hello! I am QT!")

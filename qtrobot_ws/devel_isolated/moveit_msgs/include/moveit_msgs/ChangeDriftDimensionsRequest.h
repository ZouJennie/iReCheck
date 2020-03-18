// Generated by gencpp from file moveit_msgs/ChangeDriftDimensionsRequest.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_CHANGEDRIFTDIMENSIONSREQUEST_H
#define MOVEIT_MSGS_MESSAGE_CHANGEDRIFTDIMENSIONSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Transform.h>

namespace moveit_msgs
{
template <class ContainerAllocator>
struct ChangeDriftDimensionsRequest_
{
  typedef ChangeDriftDimensionsRequest_<ContainerAllocator> Type;

  ChangeDriftDimensionsRequest_()
    : drift_x_translation(false)
    , drift_y_translation(false)
    , drift_z_translation(false)
    , drift_x_rotation(false)
    , drift_y_rotation(false)
    , drift_z_rotation(false)
    , transform_jog_frame_to_drift_frame()  {
    }
  ChangeDriftDimensionsRequest_(const ContainerAllocator& _alloc)
    : drift_x_translation(false)
    , drift_y_translation(false)
    , drift_z_translation(false)
    , drift_x_rotation(false)
    , drift_y_rotation(false)
    , drift_z_rotation(false)
    , transform_jog_frame_to_drift_frame(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _drift_x_translation_type;
  _drift_x_translation_type drift_x_translation;

   typedef uint8_t _drift_y_translation_type;
  _drift_y_translation_type drift_y_translation;

   typedef uint8_t _drift_z_translation_type;
  _drift_z_translation_type drift_z_translation;

   typedef uint8_t _drift_x_rotation_type;
  _drift_x_rotation_type drift_x_rotation;

   typedef uint8_t _drift_y_rotation_type;
  _drift_y_rotation_type drift_y_rotation;

   typedef uint8_t _drift_z_rotation_type;
  _drift_z_rotation_type drift_z_rotation;

   typedef  ::geometry_msgs::Transform_<ContainerAllocator>  _transform_jog_frame_to_drift_frame_type;
  _transform_jog_frame_to_drift_frame_type transform_jog_frame_to_drift_frame;





  typedef boost::shared_ptr< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ChangeDriftDimensionsRequest_

typedef ::moveit_msgs::ChangeDriftDimensionsRequest_<std::allocator<void> > ChangeDriftDimensionsRequest;

typedef boost::shared_ptr< ::moveit_msgs::ChangeDriftDimensionsRequest > ChangeDriftDimensionsRequestPtr;
typedef boost::shared_ptr< ::moveit_msgs::ChangeDriftDimensionsRequest const> ChangeDriftDimensionsRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace moveit_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'shape_msgs': ['/opt/ros/kinetic/share/shape_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'moveit_msgs': ['/home/jennie/irecheck/iReCheck/qtrobot_ws/devel_isolated/moveit_msgs/share/moveit_msgs/msg', '/home/jennie/irecheck/iReCheck/qtrobot_ws/src/moveit_msgs/msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'object_recognition_msgs': ['/opt/ros/kinetic/share/object_recognition_msgs/cmake/../msg'], 'octomap_msgs': ['/opt/ros/kinetic/share/octomap_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4a5ce44f94cdee672e699df89b1ebaf1";
  }

  static const char* value(const ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4a5ce44f94cdee67ULL;
  static const uint64_t static_value2 = 0x2e699df89b1ebaf1ULL;
};

template<class ContainerAllocator>
struct DataType< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "moveit_msgs/ChangeDriftDimensionsRequest";
  }

  static const char* value(const ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
\n\
bool drift_x_translation\n\
bool drift_y_translation\n\
bool drift_z_translation\n\
bool drift_x_rotation\n\
bool drift_y_rotation\n\
bool drift_z_rotation\n\
\n\
\n\
\n\
geometry_msgs/Transform transform_jog_frame_to_drift_frame\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Transform\n\
# This represents the transform between two coordinate frames in free space.\n\
\n\
Vector3 translation\n\
Quaternion rotation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.drift_x_translation);
      stream.next(m.drift_y_translation);
      stream.next(m.drift_z_translation);
      stream.next(m.drift_x_rotation);
      stream.next(m.drift_y_rotation);
      stream.next(m.drift_z_rotation);
      stream.next(m.transform_jog_frame_to_drift_frame);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ChangeDriftDimensionsRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::moveit_msgs::ChangeDriftDimensionsRequest_<ContainerAllocator>& v)
  {
    s << indent << "drift_x_translation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.drift_x_translation);
    s << indent << "drift_y_translation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.drift_y_translation);
    s << indent << "drift_z_translation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.drift_z_translation);
    s << indent << "drift_x_rotation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.drift_x_rotation);
    s << indent << "drift_y_rotation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.drift_y_rotation);
    s << indent << "drift_z_rotation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.drift_z_rotation);
    s << indent << "transform_jog_frame_to_drift_frame: ";
    s << std::endl;
    Printer< ::geometry_msgs::Transform_<ContainerAllocator> >::stream(s, indent + "  ", v.transform_jog_frame_to_drift_frame);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_CHANGEDRIFTDIMENSIONSREQUEST_H

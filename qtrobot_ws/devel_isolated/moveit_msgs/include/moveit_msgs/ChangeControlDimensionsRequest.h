// Generated by gencpp from file moveit_msgs/ChangeControlDimensionsRequest.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_CHANGECONTROLDIMENSIONSREQUEST_H
#define MOVEIT_MSGS_MESSAGE_CHANGECONTROLDIMENSIONSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace moveit_msgs
{
template <class ContainerAllocator>
struct ChangeControlDimensionsRequest_
{
  typedef ChangeControlDimensionsRequest_<ContainerAllocator> Type;

  ChangeControlDimensionsRequest_()
    : control_x_translation(false)
    , control_y_translation(false)
    , control_z_translation(false)
    , control_x_rotation(false)
    , control_y_rotation(false)
    , control_z_rotation(false)  {
    }
  ChangeControlDimensionsRequest_(const ContainerAllocator& _alloc)
    : control_x_translation(false)
    , control_y_translation(false)
    , control_z_translation(false)
    , control_x_rotation(false)
    , control_y_rotation(false)
    , control_z_rotation(false)  {
  (void)_alloc;
    }



   typedef uint8_t _control_x_translation_type;
  _control_x_translation_type control_x_translation;

   typedef uint8_t _control_y_translation_type;
  _control_y_translation_type control_y_translation;

   typedef uint8_t _control_z_translation_type;
  _control_z_translation_type control_z_translation;

   typedef uint8_t _control_x_rotation_type;
  _control_x_rotation_type control_x_rotation;

   typedef uint8_t _control_y_rotation_type;
  _control_y_rotation_type control_y_rotation;

   typedef uint8_t _control_z_rotation_type;
  _control_z_rotation_type control_z_rotation;





  typedef boost::shared_ptr< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ChangeControlDimensionsRequest_

typedef ::moveit_msgs::ChangeControlDimensionsRequest_<std::allocator<void> > ChangeControlDimensionsRequest;

typedef boost::shared_ptr< ::moveit_msgs::ChangeControlDimensionsRequest > ChangeControlDimensionsRequestPtr;
typedef boost::shared_ptr< ::moveit_msgs::ChangeControlDimensionsRequest const> ChangeControlDimensionsRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "64c0dd6d519e78f5ce2626b06dab34c1";
  }

  static const char* value(const ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x64c0dd6d519e78f5ULL;
  static const uint64_t static_value2 = 0xce2626b06dab34c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "moveit_msgs/ChangeControlDimensionsRequest";
  }

  static const char* value(const ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
bool control_x_translation\n\
bool control_y_translation\n\
bool control_z_translation\n\
bool control_x_rotation\n\
bool control_y_rotation\n\
bool control_z_rotation\n\
";
  }

  static const char* value(const ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.control_x_translation);
      stream.next(m.control_y_translation);
      stream.next(m.control_z_translation);
      stream.next(m.control_x_rotation);
      stream.next(m.control_y_rotation);
      stream.next(m.control_z_rotation);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ChangeControlDimensionsRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::moveit_msgs::ChangeControlDimensionsRequest_<ContainerAllocator>& v)
  {
    s << indent << "control_x_translation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_x_translation);
    s << indent << "control_y_translation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_y_translation);
    s << indent << "control_z_translation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_z_translation);
    s << indent << "control_x_rotation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_x_rotation);
    s << indent << "control_y_rotation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_y_rotation);
    s << indent << "control_z_rotation: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.control_z_rotation);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_CHANGECONTROLDIMENSIONSREQUEST_H

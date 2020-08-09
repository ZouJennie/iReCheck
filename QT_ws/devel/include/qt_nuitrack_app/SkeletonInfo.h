// Generated by gencpp from file qt_nuitrack_app/SkeletonInfo.msg
// DO NOT EDIT!


#ifndef QT_NUITRACK_APP_MESSAGE_SKELETONINFO_H
#define QT_NUITRACK_APP_MESSAGE_SKELETONINFO_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <qt_nuitrack_app/JointInfo.h>

namespace qt_nuitrack_app
{
template <class ContainerAllocator>
struct SkeletonInfo_
{
  typedef SkeletonInfo_<ContainerAllocator> Type;

  SkeletonInfo_()
    : id(0)
    , joints()  {
    }
  SkeletonInfo_(const ContainerAllocator& _alloc)
    : id(0)
    , joints(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef std::vector< ::qt_nuitrack_app::JointInfo_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::qt_nuitrack_app::JointInfo_<ContainerAllocator> >::other >  _joints_type;
  _joints_type joints;





  typedef boost::shared_ptr< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> const> ConstPtr;

}; // struct SkeletonInfo_

typedef ::qt_nuitrack_app::SkeletonInfo_<std::allocator<void> > SkeletonInfo;

typedef boost::shared_ptr< ::qt_nuitrack_app::SkeletonInfo > SkeletonInfoPtr;
typedef boost::shared_ptr< ::qt_nuitrack_app::SkeletonInfo const> SkeletonInfoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace qt_nuitrack_app

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'qt_nuitrack_app': ['/home/jennie/irecheck/iReCheck/QT_ws/src/qt_nuitrack_app/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ac75876d5ead18b4ad4603a6b5b71a97";
  }

  static const char* value(const ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xac75876d5ead18b4ULL;
  static const uint64_t static_value2 = 0xad4603a6b5b71a97ULL;
};

template<class ContainerAllocator>
struct DataType< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "qt_nuitrack_app/SkeletonInfo";
  }

  static const char* value(const ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#std_msgs/Header header\n\
int32 id\n\
JointInfo[] joints \n\
\n\
================================================================================\n\
MSG: qt_nuitrack_app/JointInfo\n\
#std_msgs/Header header\n\
uint8 type\n\
float32 confidence\n\
float32[] real\n\
float32[] projection\n\
float32[] orientation\n\
";
  }

  static const char* value(const ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.joints);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SkeletonInfo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::qt_nuitrack_app::SkeletonInfo_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "joints[]" << std::endl;
    for (size_t i = 0; i < v.joints.size(); ++i)
    {
      s << indent << "  joints[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::qt_nuitrack_app::JointInfo_<ContainerAllocator> >::stream(s, indent + "    ", v.joints[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // QT_NUITRACK_APP_MESSAGE_SKELETONINFO_H

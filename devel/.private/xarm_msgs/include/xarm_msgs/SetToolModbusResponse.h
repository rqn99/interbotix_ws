// Generated by gencpp from file xarm_msgs/SetToolModbusResponse.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_SETTOOLMODBUSRESPONSE_H
#define XARM_MSGS_MESSAGE_SETTOOLMODBUSRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace xarm_msgs
{
template <class ContainerAllocator>
struct SetToolModbusResponse_
{
  typedef SetToolModbusResponse_<ContainerAllocator> Type;

  SetToolModbusResponse_()
    : ret(0)
    , respond_data()  {
    }
  SetToolModbusResponse_(const ContainerAllocator& _alloc)
    : ret(0)
    , respond_data(_alloc)  {
  (void)_alloc;
    }



   typedef int16_t _ret_type;
  _ret_type ret;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _respond_data_type;
  _respond_data_type respond_data;





  typedef boost::shared_ptr< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SetToolModbusResponse_

typedef ::xarm_msgs::SetToolModbusResponse_<std::allocator<void> > SetToolModbusResponse;

typedef boost::shared_ptr< ::xarm_msgs::SetToolModbusResponse > SetToolModbusResponsePtr;
typedef boost::shared_ptr< ::xarm_msgs::SetToolModbusResponse const> SetToolModbusResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator1> & lhs, const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ret == rhs.ret &&
    lhs.respond_data == rhs.respond_data;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator1> & lhs, const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xarm_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c427c0a32ae08ea52c839bcc2cb24d84";
  }

  static const char* value(const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc427c0a32ae08ea5ULL;
  static const uint64_t static_value2 = 0x2c839bcc2cb24d84ULL;
};

template<class ContainerAllocator>
struct DataType< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xarm_msgs/SetToolModbusResponse";
  }

  static const char* value(const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"int16 ret\n"
"uint8[] respond_data\n"
"\n"
;
  }

  static const char* value(const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ret);
      stream.next(m.respond_data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetToolModbusResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xarm_msgs::SetToolModbusResponse_<ContainerAllocator>& v)
  {
    s << indent << "ret: ";
    Printer<int16_t>::stream(s, indent + "  ", v.ret);
    s << indent << "respond_data[]" << std::endl;
    for (size_t i = 0; i < v.respond_data.size(); ++i)
    {
      s << indent << "  respond_data[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.respond_data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // XARM_MSGS_MESSAGE_SETTOOLMODBUSRESPONSE_H

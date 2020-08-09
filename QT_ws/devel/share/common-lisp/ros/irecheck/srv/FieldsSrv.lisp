; Auto-generated. Do not edit!


(cl:in-package irecheck-srv)


;//! \htmlinclude FieldsSrv-request.msg.html

(cl:defclass <FieldsSrv-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass FieldsSrv-request (<FieldsSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FieldsSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FieldsSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name irecheck-srv:<FieldsSrv-request> is deprecated: use irecheck-srv:FieldsSrv-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FieldsSrv-request>) ostream)
  "Serializes a message object of type '<FieldsSrv-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FieldsSrv-request>) istream)
  "Deserializes a message object of type '<FieldsSrv-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FieldsSrv-request>)))
  "Returns string type for a service object of type '<FieldsSrv-request>"
  "irecheck/FieldsSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FieldsSrv-request)))
  "Returns string type for a service object of type 'FieldsSrv-request"
  "irecheck/FieldsSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FieldsSrv-request>)))
  "Returns md5sum for a message object of type '<FieldsSrv-request>"
  "43c0132e6d5bd924f115049e9614e3d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FieldsSrv-request)))
  "Returns md5sum for a message object of type 'FieldsSrv-request"
  "43c0132e6d5bd924f115049e9614e3d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FieldsSrv-request>)))
  "Returns full string definition for message of type '<FieldsSrv-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FieldsSrv-request)))
  "Returns full string definition for message of type 'FieldsSrv-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FieldsSrv-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FieldsSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'FieldsSrv-request
))
;//! \htmlinclude FieldsSrv-response.msg.html

(cl:defclass <FieldsSrv-response> (roslisp-msg-protocol:ros-message)
  ((fields
    :reader fields
    :initarg :fields
    :type cl:string
    :initform ""))
)

(cl:defclass FieldsSrv-response (<FieldsSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FieldsSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FieldsSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name irecheck-srv:<FieldsSrv-response> is deprecated: use irecheck-srv:FieldsSrv-response instead.")))

(cl:ensure-generic-function 'fields-val :lambda-list '(m))
(cl:defmethod fields-val ((m <FieldsSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader irecheck-srv:fields-val is deprecated.  Use irecheck-srv:fields instead.")
  (fields m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FieldsSrv-response>) ostream)
  "Serializes a message object of type '<FieldsSrv-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'fields))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'fields))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FieldsSrv-response>) istream)
  "Deserializes a message object of type '<FieldsSrv-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fields) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'fields) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FieldsSrv-response>)))
  "Returns string type for a service object of type '<FieldsSrv-response>"
  "irecheck/FieldsSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FieldsSrv-response)))
  "Returns string type for a service object of type 'FieldsSrv-response"
  "irecheck/FieldsSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FieldsSrv-response>)))
  "Returns md5sum for a message object of type '<FieldsSrv-response>"
  "43c0132e6d5bd924f115049e9614e3d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FieldsSrv-response)))
  "Returns md5sum for a message object of type 'FieldsSrv-response"
  "43c0132e6d5bd924f115049e9614e3d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FieldsSrv-response>)))
  "Returns full string definition for message of type '<FieldsSrv-response>"
  (cl:format cl:nil "string fields~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FieldsSrv-response)))
  "Returns full string definition for message of type 'FieldsSrv-response"
  (cl:format cl:nil "string fields~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FieldsSrv-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'fields))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FieldsSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'FieldsSrv-response
    (cl:cons ':fields (fields msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'FieldsSrv)))
  'FieldsSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'FieldsSrv)))
  'FieldsSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FieldsSrv)))
  "Returns string type for a service object of type '<FieldsSrv>"
  "irecheck/FieldsSrv")
; Auto-generated. Do not edit!


(cl:in-package comportement_control-msg)


;//! \htmlinclude GestureCommand.msg.html

(cl:defclass <GestureCommand> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass GestureCommand (<GestureCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GestureCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GestureCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name comportement_control-msg:<GestureCommand> is deprecated: use comportement_control-msg:GestureCommand instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <GestureCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader comportement_control-msg:name-val is deprecated.  Use comportement_control-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <GestureCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader comportement_control-msg:speed-val is deprecated.  Use comportement_control-msg:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GestureCommand>) ostream)
  "Serializes a message object of type '<GestureCommand>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GestureCommand>) istream)
  "Deserializes a message object of type '<GestureCommand>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GestureCommand>)))
  "Returns string type for a message object of type '<GestureCommand>"
  "comportement_control/GestureCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GestureCommand)))
  "Returns string type for a message object of type 'GestureCommand"
  "comportement_control/GestureCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GestureCommand>)))
  "Returns md5sum for a message object of type '<GestureCommand>"
  "731354329381c2f16be8e48fe990ad74")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GestureCommand)))
  "Returns md5sum for a message object of type 'GestureCommand"
  "731354329381c2f16be8e48fe990ad74")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GestureCommand>)))
  "Returns full string definition for message of type '<GestureCommand>"
  (cl:format cl:nil "string name~%float32 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GestureCommand)))
  "Returns full string definition for message of type 'GestureCommand"
  (cl:format cl:nil "string name~%float32 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GestureCommand>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GestureCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'GestureCommand
    (cl:cons ':name (name msg))
    (cl:cons ':speed (speed msg))
))

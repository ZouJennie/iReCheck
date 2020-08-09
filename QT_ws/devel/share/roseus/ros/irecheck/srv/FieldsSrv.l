;; Auto-generated. Do not edit!


(when (boundp 'irecheck::FieldsSrv)
  (if (not (find-package "IRECHECK"))
    (make-package "IRECHECK"))
  (shadow 'FieldsSrv (find-package "IRECHECK")))
(unless (find-package "IRECHECK::FIELDSSRV")
  (make-package "IRECHECK::FIELDSSRV"))
(unless (find-package "IRECHECK::FIELDSSRVREQUEST")
  (make-package "IRECHECK::FIELDSSRVREQUEST"))
(unless (find-package "IRECHECK::FIELDSSRVRESPONSE")
  (make-package "IRECHECK::FIELDSSRVRESPONSE"))

(in-package "ROS")





(defclass irecheck::FieldsSrvRequest
  :super ros::object
  :slots ())

(defmethod irecheck::FieldsSrvRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass irecheck::FieldsSrvResponse
  :super ros::object
  :slots (_fields ))

(defmethod irecheck::FieldsSrvResponse
  (:init
   (&key
    ((:fields __fields) "")
    )
   (send-super :init)
   (setq _fields (string __fields))
   self)
  (:fields
   (&optional __fields)
   (if __fields (setq _fields __fields)) _fields)
  (:serialization-length
   ()
   (+
    ;; string _fields
    4 (length _fields)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _fields
       (write-long (length _fields) s) (princ _fields s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _fields
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _fields (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass irecheck::FieldsSrv
  :super ros::object
  :slots ())

(setf (get irecheck::FieldsSrv :md5sum-) "43c0132e6d5bd924f115049e9614e3d9")
(setf (get irecheck::FieldsSrv :datatype-) "irecheck/FieldsSrv")
(setf (get irecheck::FieldsSrv :request) irecheck::FieldsSrvRequest)
(setf (get irecheck::FieldsSrv :response) irecheck::FieldsSrvResponse)

(defmethod irecheck::FieldsSrvRequest
  (:response () (instance irecheck::FieldsSrvResponse :init)))

(setf (get irecheck::FieldsSrvRequest :md5sum-) "43c0132e6d5bd924f115049e9614e3d9")
(setf (get irecheck::FieldsSrvRequest :datatype-) "irecheck/FieldsSrvRequest")
(setf (get irecheck::FieldsSrvRequest :definition-)
      "---
string fields

")

(setf (get irecheck::FieldsSrvResponse :md5sum-) "43c0132e6d5bd924f115049e9614e3d9")
(setf (get irecheck::FieldsSrvResponse :datatype-) "irecheck/FieldsSrvResponse")
(setf (get irecheck::FieldsSrvResponse :definition-)
      "---
string fields

")



(provide :irecheck/FieldsSrv "43c0132e6d5bd924f115049e9614e3d9")



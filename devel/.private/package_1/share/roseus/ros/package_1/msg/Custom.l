;; Auto-generated. Do not edit!


(when (boundp 'package_1::Custom)
  (if (not (find-package "PACKAGE_1"))
    (make-package "PACKAGE_1"))
  (shadow 'Custom (find-package "PACKAGE_1")))
(unless (find-package "PACKAGE_1::CUSTOM")
  (make-package "PACKAGE_1::CUSTOM"))

(in-package "ROS")
;;//! \htmlinclude Custom.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass package_1::Custom
  :super ros::object
  :slots (_header _message _coordinate ))

(defmethod package_1::Custom
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:message __message) "")
    ((:coordinate __coordinate) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _message (string __message))
   (setq _coordinate __coordinate)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:coordinate
   (&rest __coordinate)
   (if (keywordp (car __coordinate))
       (send* _coordinate __coordinate)
     (progn
       (if __coordinate (setq _coordinate (car __coordinate)))
       _coordinate)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string _message
    4 (length _message)
    ;; geometry_msgs/Point _coordinate
    (send _coordinate :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;; geometry_msgs/Point _coordinate
       (send _coordinate :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Point _coordinate
     (send _coordinate :deserialize buf ptr-) (incf ptr- (send _coordinate :serialization-length))
   ;;
   self)
  )

(setf (get package_1::Custom :md5sum-) "df4cbcc180f9e5f7082067ab54c916f7")
(setf (get package_1::Custom :datatype-) "package_1/Custom")
(setf (get package_1::Custom :definition-)
      "Header header
string message
geometry_msgs/Point coordinate
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :package_1/Custom "df4cbcc180f9e5f7082067ab54c916f7")



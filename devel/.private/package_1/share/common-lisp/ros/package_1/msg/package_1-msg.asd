
(cl:in-package :asdf)

(defsystem "package_1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Custom" :depends-on ("_package_Custom"))
    (:file "_package_Custom" :depends-on ("_package"))
  ))
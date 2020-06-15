
(cl:in-package :asdf)

(defsystem "comportement_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GestureCommand" :depends-on ("_package_GestureCommand"))
    (:file "_package_GestureCommand" :depends-on ("_package"))
  ))
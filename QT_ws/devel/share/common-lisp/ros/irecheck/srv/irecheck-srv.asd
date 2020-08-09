
(cl:in-package :asdf)

(defsystem "irecheck-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FieldsSrv" :depends-on ("_package_FieldsSrv"))
    (:file "_package_FieldsSrv" :depends-on ("_package"))
  ))
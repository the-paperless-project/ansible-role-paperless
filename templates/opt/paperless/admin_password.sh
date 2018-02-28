#!/usr/bin/expect

set timeout -1;
spawn {{ paperless_virtualenv }}/bin/python /opt/paperless/source/src/manage.py changepassword {{ paperless_admin_user }};
expect {
    "Password:" { exp_send "{{ paperless_admin_password }}\r" ; exp_continue }
    "Password (again):" { exp_send "{{ paperless_admin_password }}\r" ; exp_continue }
    eof
}

#!/usr/bin/expect

set timeout -1;
spawn /opt/paperless/.env/bin/python /opt/paperless/source/src/manage.py changepassword {{ paperless_user }};
expect {
    "Password:" { exp_send "{{ paperless_password }}\r" ; exp_continue }
    "Password (again):" { exp_send "{{ paperless_password }}\r" ; exp_continue }
    eof
}

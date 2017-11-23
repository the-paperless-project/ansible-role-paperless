ovv.paperless
=============

[![Build Status](https://travis-ci.org/ovv/ansible-role-paperless.svg?branch=master)](https://travis-ci.org/ovv/ansible-role-paperless)

Ansible role to install and configure [paperless](https://github.com/danielquinn/paperless).

Requirements
------------

A python3 and nginx installation are required. We recommend using [pyslackers.python](https://github.com/pyslackers/ansible-role-python)
and [pyslackers.nginx](https://github.com/pyslackers/ansible-role-nginx).

Installation
------------

To install this roles clone it into your roles directory.

```bash
$ git clone https://github.com/ovv/ansible-role-paperless.git ovv.paperless
```

If your playbook already reside inside a git repository you can clone it by using git submodules.

```bash
$ git submodule add -b master https://github.com/ovv/ansible-role-paperless.git ovv.paperless
```

Role Variables
--------------


Dependencies
------------

None

Example Playbook
----------------

```yml
- hosts: paperless
  tags:
    - paperless
  roles:
    - pyslackers.python
    - ovv.paperless
    - pyslackers.nginx
  vars:
    paperless_user: 
    paperless_password: 
    paperless_email:
    paperless_encrypt_passphrase:
    paperless_secret_key:
    
    # pyslackers.python
    virtualenvs:
      paperless:
        path: /opt/paperless/.env
        version: 3.6.3
    
    # pyslackers.nginx
    nginx_sites:
      paperless:
        directory: /opt/paperless
        locations:
          static:
            location: /static
            custom: |
              autoindex on;
              alias /opt/paperless/static;
          root:
            location: /
            proxy_pass: http://127.0.0.1:8000
```

License
-------

MIT

Author Information
------------------

None

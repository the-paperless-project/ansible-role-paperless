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

* `paperless_admin_user`: Paperless admin user.
* `paperless_admin_email`: Paperless admin email.
* `paperless_admin_password`: Paperless admin password.
* `paperless_encrypt_passphrase`: Paperless encryption passphrase.
* `paperless_secret_key`: Paperless secret key.


* `paperless_consumption_dir`: Consumption directory for paperless (default to `/opt/paperless/consumption`).
* `paperless_consumption_dir_group`: Group of the consumption directory (default to `paperless`).
* `paperless_consumption_dir_users`: List of users to add to the `paperless_consumption_dir_group` (default to `[]`).


* `paperless_allowed_host`: List of hosts allowed to connect (default to `[127.0.0.1]`).
* `paperless_ocr_language`: Default ocr language (default to `eng`).
* `paperless_tz`: Timezone (default to `Etc/UTC`).
* `paperless_list_per_page`: Number of item per page (default to `100`).
* `paperless_custom_packages`: Custom packages to install, like some tesseract languages (default to `[]`).


* `paperless_backup`: Export paperless documents and fetch them to `paperless_backup_directory` (default to `False`).
* `paperless_restore`: Upload and import documents from the `paperless_backup_directory` (default to `False`).
* `paperless_backup_directory`: Directory on the computer launching the ansible where to store documents backup.

Other variable and their defaults are located in [defaults](defaults/main.yml).

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
    paperless_admin_user: admin
    paperless_admin_password: password
    paperless_admin_email: paperless@example.com
    paperless_encrypt_passphrase: passphrase
    paperless_secret_key: supersecretkey

    # pyslackers.python
    virtualenvs:
      paperless:
        path: /opt/paperless/.env
        version: 3.6.4

    # pyslackers.nginx
    nginx_sites:
      paperless:
        directory: /opt/paperless
        locations:
          - location: /static
            custom: |
              autoindex on;
              alias /opt/paperless/static;
          - location: /
            proxy_pass: http://127.0.0.1:8000
```

License
-------

MIT

f5_check_server_certs
==============

Checks if any certificates are expiring within a particular expiration period. The role produces a report which is then emailed to an admin.

Requirements
------------

Install the following Python libraries in order to use this role

* f5-sdk
* bigsuds

Role Variables
--------------

* ``f5_cert_expiration_period``: Number of days before certificate expires
* ``f5_hostname``: f5 server name
* ``f5_username``: f5 username with privileges to add or remove pool members
* ``f5_password``: f5 password for user with add/remove pool member privileges
* ``mailserver``: mail server name
* ``mail_port``: mail server port
* ``mail_username``: mail server user name
* ``mail_password``: mail server user password
* ``mail_receipient``: mail destination email
* ``mail_sender``: mail sender email

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: localhost
  connection: local
  gather_facts: no
  pre_tasks:
    - name: give F5 hostname as a extra var on a Ansible Tower survey
      assert:
        that: f5_hostname is defined
        msg: "f5_hostname is not provided"
  vars:
    # get Username/Password from Ansible Tower SSH Credential
    f5_username: "{{ ansible_password }}"
    f5_password: "{{ ansible_user }}"
  roles:
    - role: f5_check_server_certs

```

License
-------
MIT


Author Information
------------------

Red Hat Consulting

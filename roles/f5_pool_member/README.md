f5_pool_member
==============

Adds or Removes a Pool Member. Assumes the F5 pool already exists.

Requirements
------------

Install the following Python libraries in order to use this role

* f5-sdk
* bigsuds

Role Variables
--------------

* ``pool_name``: Name of the pool to manipulate
* ``pool_member``: IP or hostname of pool member to add or remove`
* ``pool_action``: can be either  add or delete. Default action is 'add'
* ``f5_hostname``: f5 server name
* ``f5_username``: f5 username with privileges to add or remove pool members
* ``f5_password``: f5 password for user with add/remove pool member privileges

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
    - name: give F5 hostname as a extra var on a Ansible Tower survey form
      assert:
        that: f5_hostname is defined
        msg: "f5_hostname is not provided"
    - name: give pool member as an extra var on the Ansible Tower survey form
      assert:
        that: pool_member is defined
        msg: "pool_member is not provided"
    - name: give pool  name as an extra var on the Ansible Tower survey form
      assert:
        that: pool_name is defined
        msg: "pool_name is not provided"
  vars:
    # get Username/Password from Ansible Tower SSH Credential
    f5_username: "{{ ansible_password }}"
    f5_password: "{{ ansible_user }}"

  roles:
    - role: f5_pool_member

```

License
-------
MIT


Author Information
------------------

Red Hat Consulting - Initial setup

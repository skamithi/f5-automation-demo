f5_virtual_server
==============

Create a F5 Virtual Server.
   - Create a monitor
   - Creates the pool nodes
   - create a pool
   - assign node as pool members
   - create a virtual server binding SSL certs and Irules if necessary.


Requirements
------------

Install the following Python libraries in order to use this role

* f5-sdk
* bigsuds

Role Variables
--------------

* ``f5_hostname``: f5 server name
* ``f5_username``: f5 username with privileges to add or remove pool members
* ``f5_password``: f5 password for user with add/remove pool member privileges
* ``monitor_send_string``: http string to send to the node behind the f5
* ``monitor_receive_string``: http string to expect from the node behind the f5
* ``pool_members``: List of hostnames that will become pool members
* ``pool_name``: F5 pool name
* ``vserver_address``:  vserver address
* ``vserver_port``: vserver port
* ``vserver_name``: vserver name
* ``vserver_profiles``: list virtual server profiles. Example: ['http', 'clientssl']
* ``vserver_default_persistent_profil``e: Define default persistence profile
* ``vserver_fallback_persistent_profile``: Define fallack persistence profile

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
    - name: ensure that user inputs are made available to this playbook before execution
      assert:
      that: "{{ item }} is defined "
      msg: "{{ item }} is not provided"
    with_items:
      - monitor_send_string
      - monitor_receive_string
      - pool_name
      - vserver_name
      - vserver_port
      - vserver_profiles
      - vserver_default_persistent_profile
      - vserver_fallback_persistent_profile
      - pool_members
      - f5_hostname

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

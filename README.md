# Ansible Installation

### How to setup Ansible on your GNU/Linux system
```
$ cd $HOME
$ mkdir fosscafe
$ cd fosscafe
$ git clone https://github.com/ansible/ansible.git
$ cd ansible
$ git submodule update --init
$ . hacking/env-setup

$ bin/ansible --version

ansible 2.4.0 (devel 737c27121b) last updated 2017/09/01 22:22:13 (GMT +550)
  config file = None
  configured module search path = ['/home/saifi/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/saifi/src/src-ansible/ansible/lib/ansible
  executable location = bin/ansible
  python version = 3.6.2 (default, Jul 20 2017, 03:52:27) [GCC 7.1.1 20170630]


$
```
### On Windows system

Please follow these steps:
* install vagrant or virtualbox or hyper-v
* install a Linux distro of your choice (we recommend Arch Linux, Alpine Linux or Gentoo Linux)
* Follow the steps outlined in section above titled 'Ansible on GNU/Linux' system


### Support
Please send mail to fosscafe@googlegroups.com


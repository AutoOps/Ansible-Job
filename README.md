Ansible-Job
------------------------
本次试验配置环境为：
------------------------
控制节点：
主机名：controller
网卡名：eno16777984
IPv4: 172.16.50.66/24
------------------------
计算节点：
主机名：
compute1
网卡名：eno16777984
IPv4: 172.16.50.67/24

compute2
网卡名：eno16777984
IPv4: 172.16.50.68/24

compute3
网卡名：eno16777984
IPv4: 172.16.50.69/24
------------------------
------------------------
1.修改主机名
控制节点:controller
计算节点:
compute1
compute2
compute3
------------------------
2.全部节点都做/etc/hosts 硬解析
# controller
172.16.50.66	controller
# compute1
172.16.50.67	compute1
# compute2
172.16.50.68	compute2
# compute3
172.16.50.69	compute3

------------------------
3.免密钥登录
  a.从控制节点登录所有计算节点免密钥
  b.从控制节点登录控制节点也要免密钥
------------------------
4.密码设置
  为了本次试验，统一设定密码为：
  aaaaaa
  其中具体可根据自己的需求自行设置
------------------------
5.目录介绍

openstack-01-liberty/
├── action_plugins
├── group_vars
│   ├── all
│   ├── compute_servers
│   └── controller_servers
├── library
│   ├── keystone_endpoint.py
│   └── keystone_service.py
├── roles
│   ├── dashboard
│   │   ├── files
│   │   │   └── local_settings
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── dhcp_agent
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── glance
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── api.yml
│   │       ├── config.yml
│   │       ├── db.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── keystone
│   │   ├── files
│   │   │   └── wsgi-keystone.conf
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── api.yml
│   │       ├── config.yml
│   │       ├── db.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── l3_agent
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── linuxbridge_agent
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── mariadb
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── metadata_agent
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── mongodb
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── neutron_compute
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── neutron_server
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── api.yml
│   │       ├── config.yml
│   │       ├── db.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── nova_compute
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── nova_server
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── api.yml
│   │       ├── config.yml
│   │       ├── db.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── ntp
│   │   ├── files
│   │   │   └── chrony.conf
│   │   └── tasks
│   │       ├── change_ntp_cfg_n.yml
│   │       ├── change_ntp_cfg.yml
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── rabbitmq
│   │   └── tasks
│   │       ├── config.yml
│   │       ├── install.yml
│   │       ├── main_old_bak.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── restart_nova_service
│   │   └── tasks
│   │       ├── main.yml
│   │       └── start.yml
│   ├── system
│   │   ├── files
│   │   │   └── local_repo
│   │   └── tasks
│   │       ├── init-config.yml
│   │       ├── init-service.yml
│   │       └── main.yml
│   └── zabbix
│       ├── files
│       └── tasks
│           ├── config.yml
│           ├── install.yml
│           ├── main.yml
│           └── start.yml
└── site.yml
------------------------
------------------------
------------------------
------------------------
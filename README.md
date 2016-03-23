Ansible-Job
------------------------
本次试验配置环境为：
------------------------
控制节点：
主机名：controller
网卡名：en32
IPv4: 172.16.50.53/24

计算节点：
主机名：compute1
网卡名：en32
IPv4: 172.16.50.54/24
------------------------
------------------------
1.修改主机名
控制节点:controller
计算节点:compute1
------------------------
2.全部节点都做/etc/hosts 硬解析
# controller
172.16.50.53	controller
# compute1
172.16.50.54	compute1
------------------------
3.免密钥登录
  a.从控制节点登录所有计算节点免密钥
  b.从控制节点登录控制节点也要免密钥
------------------------
4.密码设置
  为了本次试验，统一设定密码为：
  MyPassWord*2016
  其中具体可根据自己的需求自行设置
------------------------
5.目录介绍

├── group_vars
│   ├── all
│   ├── compute_servers
│   ├── controller_servers
│   └── password
├── inventory
├── library
│   ├── keystone_endpoint.py
│   └── keystone_service.py
├── roles
│   ├── agent
│   │   ├── files
│   │   └── tasks
│   │       └── main.yml
│   ├── dashboard
│   │   ├── files
│   │   │   └── local_settings
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       └── main.yml
│   ├── glance
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── glance-api.yml
│   │       ├── glance-db.yml
│   │       ├── glance-install.yml
│   │       └── main.yml
│   ├── keystone
│   │   ├── files
│   │   │   └── wsgi-keystone.conf
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── httpd.yml
│   │       ├── keystone-api.yml
│   │       ├── keystone-db.yml
│   │       ├── keystone-install.yml
│   │       └── main.yml
│   ├── mariadb
│   │   └── tasks
│   │       └── main.yml
│   ├── mongodb
│   │   └── tasks
│   │       └── main
│   ├── neutron-compute
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── bridge-agent.yml
│   │       ├── main.yml
│   │       ├── neutron-install.yml
│   │       ├── neutron-nova.yml
│   │       └── service-enable.yml
│   ├── neutron-server
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── bridge-agent.yml
│   │       ├── dhcp-agent.yml
│   │       ├── l3-agent.yml
│   │       ├── main.yml
│   │       ├── metadata-agent.yml
│   │       ├── ml2.yml
│   │       ├── neutron-db.yml
│   │       ├── neutron-install.yml
│   │       ├── neutron-nova.yml
│   │       └── service-enable.yml
│   ├── nova-compute
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── main.yml
│   │       ├── nova-com.yml
│   │       └── ntp-com.yml
│   ├── nova-server
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── main.yml
│   │       ├── nova-api.yml
│   │       ├── nova-db.yml
│   │       └── nova-install.yml
│   ├── ntp
│   │   ├── files
│   │   │   └── chrony.conf
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── change_ntp_cfg_n.yml
│   │       ├── change_ntp_cfg.yml
│   │       ├── install_ntp.yml
│   │       └── main.yml
│   ├── rabbitmq
│   │   └── tasks
│   │       ├── main-bak.yml
│   │       └── main.yml
│   └── system
│       ├── files
│       │   └── local_repo
│       └── tasks
│           ├── init-config.yml
│           ├── init-service.yml
│           └── main.yml
└── site.yml
------------------------
------------------------
------------------------
------------------------
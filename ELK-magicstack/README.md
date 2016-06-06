├── group_vars
│   └── all
├── inventory
│   └── hosts
├── README.md
├── roles
│   ├── elasticsearch
│   │   ├── files
│   │   │   └── elasticsearch-2.3.3.rpm
│   │   └── tasks
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── init_sys
│   │   └── tasks
│   │       ├── install.yml
│   │       └── main.yml
│   ├── kafka
│   │   ├── files
│   │   │   ├── kafka
│   │   │   ├── kafka_2.10-0.9.0.1.tgz
│   │   │   └── zookeeper
│   │   ├── tasks
│   │   │   ├── install.yml
│   │   │   ├── kafka_conf.yml
│   │   │   ├── main.yml
│   │   │   └── start.yml
│   │   └── templates
│   │       └── server_properties.j2
│   ├── kibana
│   │   ├── files
│   │   │   └── kibana-4.5.1-1.x86_64.rpm
│   │   └── tasks
│   │       ├── install.yml
│   │       ├── main.yml
│   │       └── start.yml
│   ├── logstash
│   │   ├── files
│   │   │   ├── conf
│   │   │   │   ├── input_1000_logs.conf
│   │   │   │   └── output_1000_kafka.conf
│   │   │   └── logstash-2.2.2-1.noarch.rpm
│   │   ├── handlers
│   │   │   └── main.yml
│   │   └── tasks
│   │       ├── install.yml
│   │       ├── logstash_conf.yml
│   │       ├── main.yml
│   │       └── start.yml
│   └── logstash_index
│       ├── files
│       │   ├── conf
│       │   │   ├── input_1000_kafka.conf
│       │   │   └── output_1000_es.conf
│       │   └── logstash-2.2.2-1.noarch.rpm
│       ├── handlers
│       │   └── main.yml
│       └── tasks
│           ├── install.yml
│           ├── logstash_index.yml
│           ├── main.yml
│           └── start.yml
└── site.yml

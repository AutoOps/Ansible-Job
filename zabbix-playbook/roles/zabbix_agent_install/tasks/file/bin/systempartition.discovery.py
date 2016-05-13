#!/usr/bin/env python
import os
import json
t=os.popen(""" df -h |grep -v tmpfs |awk '{print $6}' |grep -v Mount  """)
ports = []
for port in  t.readlines():
        data = port.strip('\n')
        ports += [{'{#PARTITIONNAME}':data}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))

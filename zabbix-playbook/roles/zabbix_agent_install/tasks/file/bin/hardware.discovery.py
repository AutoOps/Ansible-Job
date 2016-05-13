#!/usr/bin/env python
import os
import json
t=os.popen(""" ipmitool -I open sdr |egrep '^Power|FAN*'|grep -v ns |awk '{print $1}'  """)
ports = []
for port in  t.readlines():
        data = port.strip('\n')
        ports += [{'{#HARDWARENAME}':data}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))

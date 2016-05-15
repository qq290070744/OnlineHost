#!/usr/bin/env python
#-*- coding:utf-8 -*-
#检查在线主机脚本
import re,subprocess

with open("t.txt","w",encoding="utf-8") as f:
    for i in range(20,25):
        #ip=os.popen("ping -n 1 192.168.72.%s"%i).read().strip()
        ip=subprocess.Popen("ping -n 1 192.168.72.%s"%i,stdout=subprocess.PIPE,shell=True).stdout.read()
        f.write("%s\n"%ip)
with open("t.txt",encoding="utf-8") as f_r,open("ip.txt","w",encoding="utf-8") as f_w:
    for i in f_r:
        if "TTL" in i:
            m = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i)#正则匹配IP
            f_w.write("%s\n"%m.group())



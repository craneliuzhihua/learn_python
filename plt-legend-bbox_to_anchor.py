#!/usr/bin/env python
#---coding:UTF-8---
#本脚本用来输出网页计费新框架的各个接口最近其他的访问量的图形
#目前输出的是图例在图片右侧，详细效见图片plt-legend-bbox_to_anchor.png
#本脚本用到的源数据见文件Last7_total.csv
#version:1.0.0
#release:2017/02/15
#author:lzh phone:15811869179

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename="/home/craneliu/python/wabps_img/Last7_total.csv"

with open(filename) as f:
     readers=csv.reader(f)

     dates=[]
     apSyncQueryReq_req_nums=[]
     IntegratedSubscribeReq_req_nums=[]

     for reader in readers:
         date=datetime.strptime(reader[0],'%Y-%m-%d')
         apSyncQueryReq_req_num=int(reader[1])
         IntegratedSubscribeReq_req_num=int(reader[2])

         dates.append(date)
         apSyncQueryReq_req_nums.append(apSyncQueryReq_req_num)
         IntegratedSubscribeReq_req_nums.append(IntegratedSubscribeReq_req_num)
         
fig=plt.figure(dpi=128, figsize=(20,6),facecolor='yellow',edgecolor='green')
plt.plot(dates,apSyncQueryReq_req_nums,c='red',alpha=0.5,label='apSyncQueryReq')
plt.plot(dates,IntegratedSubscribeReq_req_nums,c='blue',alpha=0.5,label='IntegratedSubscribeReq')
plt.legend(bbox_to_anchor=(1,.102), loc=10,ncol=1, mode="expand", borderaxespad=0.,fontsize=6)

title="Wabps's Access Of Different Interfaces"
plt.title(title,fontsize=10)
plt.xlabel('Aceess of last 7 days',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Numbers of access",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
    

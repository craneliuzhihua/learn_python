#!/usr/bin/env python
#---coding:UTF-8---
#本脚本用来输出网页计费新框架的各个接口最近其他的访问量的图形
#version:1.0.0
#release:2017/02/15
#author:lzh phone:15811869179
#本脚本用到的源数据文件是Last7_total.csv，输出的图片为plt-legend-bbox_to_anchor.png

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename="/home/craneliu/python/wabps_img/Last7_total.csv"

with open(filename) as f:
     readers=csv.reader(f)

     dates=[]
     apSyncQueryReq_nums=[]
     IntegratedSubscribeReq_nums=[]
     UnSubscribeServiceReq_nums=[]
     AppServQueryReq_nums = []
     AppUnSubscribeReq_nums = []
     UnSubscribeWabpServiceReq_nums = []
     WabpBillApplyReq_nums = []
     WabpPreQueryReq_nums = []
     WabpBillConfirmReq_nums = []
     ServiceWebTransfer2APReq_nums = []
     VertifyUserState2APReq_nums = []

     for reader in readers:
         date=datetime.strptime(reader[0],'%Y-%m-%d')
         apSyncQueryReq_num=int(reader[1])
         IntegratedSubscribeReq_num=int(reader[2])
         UnSubscribeServiceReq_num = int(reader[3])
         AppServQueryReq_num = int(reader[4])
         AppUnSubscribeReq_num = int(reader[5])
         UnSubscribeWabpServiceReq_num = int(reader[6])
         WabpBillApplyReq_num = int(reader[7])
         WabpPreQueryReq_num = int(reader[8])
         WabpBillConfirmReq_num = int(reader[9])
         ServiceWebTransfer2APReq_num = int(reader[10])
         VertifyUserState2APReq_num = int(reader[11])

         dates.append(date)
         apSyncQueryReq_nums.append(apSyncQueryReq_num)
         IntegratedSubscribeReq_nums.append(IntegratedSubscribeReq_num)
         UnSubscribeServiceReq_nums.append(UnSubscribeServiceReq_num)
         AppServQueryReq_nums.append(AppServQueryReq_num)
         AppUnSubscribeReq_nums.append(AppUnSubscribeReq_num)
         UnSubscribeWabpServiceReq_nums.append(UnSubscribeWabpServiceReq_num)
         WabpBillApplyReq_nums.append(WabpBillApplyReq_num)
         WabpPreQueryReq_nums.append(WabpPreQueryReq_num)
         WabpBillConfirmReq_nums.append(WabpBillConfirmReq_num)
         ServiceWebTransfer2APReq_nums.append(ServiceWebTransfer2APReq_num)
         VertifyUserState2APReq_nums.append(VertifyUserState2APReq_num)


#定义图片的各种参数（如背景颜色等）
fig=plt.figure(dpi=128, figsize=(20,6),facecolor='yellow',edgecolor='green')
#在图片上画各种接口的访问图形
plt.plot(dates,apSyncQueryReq_nums,'-o',c='blue',alpha=0.5,label='apSyncQueryReq')
plt.plot(dates,IntegratedSubscribeReq_nums,'-D',c='green',alpha=0.5,label='IntegratedSubscribeReq')
plt.plot(dates,UnSubscribeServiceReq_nums,'-h',c='red',alpha=0.5,label='UnSubscribeServiceReq')
plt.plot(dates,AppServQueryReq_nums,'-x',c='red',alpha=0.5,label='AppServQueryReq')
plt.plot(dates,AppUnSubscribeReq_nums,'-8',c='red',alpha=0.5,label='AppUnSubscribeReq')
plt.plot(dates,UnSubscribeWabpServiceReq_nums,'-s',c='red',alpha=0.5,label='UnSubscribeWabpServiceReq')
plt.plot(dates,WabpBillApplyReq_nums,'-*',c='black',alpha=0.5,label='WabpBillApplyReq')
plt.plot(dates,WabpPreQueryReq_nums,'-d',c='red',alpha=0.5,label='WabpPreQueryReq')
plt.plot(dates,WabpBillConfirmReq_nums,'-p',c='blue',alpha=0.5,label='WabpBillConfirmReq')
plt.plot(dates,ServiceWebTransfer2APReq_nums,'-<',c='green',alpha=0.5,label='ServiceWebTransfer2APReq')
plt.plot(dates,VertifyUserState2APReq_nums,'->',c='red',alpha=0.5,label='VertifyUserState2APReq')

plt.legend(bbox_to_anchor=(1,.102), loc=10,ncol=1, mode="expand", borderaxespad=0.,fontsize=6)

title="Wabps's Access Of Different Interfaces"
plt.title(title,fontsize=10)
plt.xlabel('Aceess of last 7 days',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Numbers of access",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
    

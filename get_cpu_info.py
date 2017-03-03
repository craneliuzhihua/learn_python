#本脚本用来获取/proc/cpuinfo文件的cpu信息
#!/usr/bin/env python
#---coding:UTF-8---
#release:2017/03/03
from collections import OrderedDict

def get_cpu_info():
  process_number=0
  CPU_LIST_INFOS={}
  CPU_INFO_DETAILS={}
  with open("/tmp/cpuinfo")as f:
     for line in f:
        if line.strip()=='':
            CPU_LIST_INFOS[process_number]=CPU_INFO_DETAILS
            process_number=process_number+1
            CPU_INFO_DETAILS={}
           
        else:
           CPU_INFO_DETAILS[line.split(':')[0]]=line.split(':')[1]

     for number,cpu_list_info in CPU_LIST_INFOS.items():
        print("process %s:\n") %(number)
        for module_name,cpu_info in cpu_list_info.items():
            print("%s:%s") %(module_name,cpu_info)            

if __name__=='__main__':
   get_cpu_info()
   print("hello2")

#Author craneliu
#本脚本实现通过输入参数来决定脚本的输出内容
#--version 输出版本信息
#--help 输出帮助信息
#输入文件明，输出文件内容
import sys

#定义读取文件的方法
def open_file(filename):
    f=open(filename)
    lines=f.readlines()
# 第一种读取文件的方法（一次读取所有行）
    for line in lines:
        print(line)
    f.close()
'''
第二种读取文件内容的方法（逐行读取）
 while line:
        print(line)
        line=f.readline()
    f.close()
'''


if len(sys.argv)<2 :
    print("Sorry ! You didn't specify any words....Please specify your words !")
else:
    if sys.argv[1].startswith('--'):
        if sys.argv[1]=="--version":
            print("Python version:3.5")
        elif sys.argv[1]=="--help":
            print('''
            This program prints files to the standard output. 
            Any number of files can be specified. 
            Options include: 
              --version : Prints the version number 
              --help    : Display this help''')
        else:
            print("Sorry ! Wrong arguments! Please specify '--help' to get you help")
    else:
        open_file(sys.argv[1])

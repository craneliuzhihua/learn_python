#Author craneliu
#本脚本实现用户登录程序
#（1）如果用户输入三次密码均错误，用户将会被锁
#（2）如果用户连续两次输入不同的用户名，会被强制重新登录

import getpass
user_info={}          #保存用户信息
user_locked=[]        #记录被锁定的用户信息

#打开用户信息的文件
with open('user_info.txt') as opened_file:
    lines=opened_file.readlines()
    for line in lines:
        line = line.strip('\n')
        split_list=line.split(':')
        user_info[split_list[0]]=split_list[1]

#读入被锁定的用户信息
with open('user_locked.txt') as opened_file:
    lines=opened_file.readlines()
    for line in lines:
        line = line.strip('\n')
        user_locked.append(line)

tmp_user=[]                                   #保存本次登录的用户名，用于对比连续输入的用户名称是否相同
fail_count=0
while fail_count<3:                           #使用循环实现登录验证，用户输入错误三次即锁定用户
    input_user=input("Please input your name :")
    input_passwd=getpass.getpass("Please input your password :")

#利用if检查用户是否被锁定
    if input_user in user_locked:
        print("Sorry ! Your account is locked ! You're not permitted to login......")
        break
    else:
        if not tmp_user:
            tmp_user.append(input_user)
        if input_user==tmp_user[0]:
            if input_passwd == user_info[input_user]:
                print("Welcome to login ,{_username} !".format(_username=input_user))
                break
            else:
                fail_count += 1
                print("Sorry ! Logined failed {count} times! Check your name or password.....".format(count=fail_count))
                if fail_count == 3:
                    print(
                        "Sorry ! Your account will be locked ! You're not permitted to login......Please wait for next login !")
                    with open("user_locked.txt", 'a') as locked_file:
                        locked_file.write("\n")
                        locked_file.write(input_user)
                        break

        else:
            print("Sorry! Your input username is different from your last time !Please exit and login again !")

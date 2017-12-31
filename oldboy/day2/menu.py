#Author craneliu
#本脚本实现三级菜单的功能“省-市-区”
#（1）从最高级别的菜单可以逐步进入下一级菜单
#（2）在每个级别菜单可以返回上一级菜单，以及退出整个程序
pronvince_lists=["广东","广西","湖南","湖北","海南","江西","福建"]
pronvince_city_dicts={
"广东":["广州市","深圳市","佛山市","江门市","东莞市","珠海市"],
"广西":["南宁市","柳州市","桂林市","梧州市","北海市","玉林市"],
"湖南":["长沙市","株洲市","湘潭市","衡阳市","邵阳市","岳阳市"],
"湖北":["武汉市","黄石市","十堰市","宜昌市","襄阳市","鄂州市"],
"海南":["海口市","三亚市","三沙市","儋州市","洋浦经济开发区","五指山市"],
"江西":["南昌市","九江市","上饶市","抚州市","宜春市","吉安市"],
"福建":["福州市","厦门市","漳州市","泉州市","三明市","莆田市"]

}
city_area_dicts={
"长沙市":["长沙区1","长沙区2","长沙区3"],
"广州市":["越秀区","荔湾区","白云区"],
"南宁市":["南宁区1","南宁区2","南宁区3"],
"南昌市":["南昌区1","南昌区2","南昌区3"],
"福州市":["福州区1","福州区2","福州区3"],
"武汉市":["武汉区1","武汉区2","武汉区3"],
"海口市":["海口区1","海口区2","海口区3"],
}

cycle_flag=True
while cycle_flag:
    show_menu=input("Would you like to display this menu ? Y/N:")
    if show_menu=='Y' or show_menu=="y":
        print("Welcome ! We will show you the pronvince list as below.")
        while cycle_flag:
            for index, item in enumerate(pronvince_lists):
                print(index, item)
            pronvine_choice = input(  ####进入市菜单
                ">>>>>>What's your choice ?\n"
                ">>>>>>Input nmber for a pronvince's city\n"
                ">>>>>>Q(uit) for exitting the programm\n"
                ">>>>>>R(eturn) for backup to  the top menu\n"
                ">>>>>>Your choice ?:"
            )
            if pronvine_choice == 'q' or pronvine_choice == 'Q':
                print("OK ! This programm will exit right now .....")
                cycle_flag = False
            elif pronvine_choice.isdigit():
                pronvine_choice = int(pronvine_choice)
                if pronvine_choice >= 0 and pronvine_choice < len(pronvince_lists):
                    while cycle_flag:
                        for index, item in enumerate(pronvince_city_dicts[pronvince_lists[pronvine_choice]]):
                            print(index, item)
                        city_choice = input(  ####进入区菜单
                            ">>>>>>What's your choice ?\n"
                            ">>>>>>Input nmber for a city's area\n"
                            ">>>>>>Q(uit) for exitting the programm\n"
                            ">>>>>>R(eturn) for backup to  the pronvine menu\n"
                            ">>>>>>Your choice ?:"
                        )
                        if city_choice == 'Q' or city_choice == 'q':
                            print("OK ! This programm will exit right now .....")
                            cycle_flag = False
                        elif city_choice == 'R' or city_choice == 'r':
                            break
                        elif city_choice.isdigit():
                            city_choice = int(city_choice)
                            while cycle_flag:
                                for index,item in enumerate(city_area_dicts[pronvince_city_dicts[pronvince_lists[pronvine_choice]][city_choice]]):
                                    print(index,item)
                                area_choice=input(">>>>>>What's your choce ?\n"
                                                  ">>>>>>Q(uit) for exitting the programm\n"
                                                  ">>>>>>R(eturn) for backup to  the city menu\n"
                                                  ">>>>>>Your choice ?:"
                                                  )
                                if area_choice=='q' or area_choice=='Q':
                                    cycle_flag = False
                                elif area_choice=='R' or area_choice=='r':
                                    break
                                else:
                                    print("Sorry ! Invalid choice!Try again ,please !")
                        else:
                            print("Sorry ! Invalid choice!Try again ,please !")
                else:
                    print("Sorry ! Invalid choice!Try again ,please !")
            elif pronvine_choice == 'R' or pronvine_choice == 'r':
                break
            else:
                print("Sorry ! Invalid choice!Try again ,please !")


    elif show_menu=='N' or show_menu=='n':
        print("OK ! This programm will exit right now .....")
        break
    else:
        print("Sorry ! invalid option.......")

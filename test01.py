#roc code
'''
编写登陆接口
输入用户名密码
认证成功后显示登陆页面
输错三次后锁定
'''
num=0
while num<3:
    name=input("输入账号")
    password=input("输入密码")
    user_storehouse={
        "skirt":"123",
        "kilt":"123",
        "dress":"123",
        "watch":"123",
    }
    for i in user_storehouse:
        if name==i and password==user_storehouse[i]:
            print("登陆成功")
        else:
            break

    print("输入失败")
    num=num+1
    print("num=%d"%num)



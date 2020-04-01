# 不定长参数
def info(arg1,*args): #元组
    print(arg1)
    for arg in args:
        print(arg)
    print("-------------")

def info2(arg1,**args): #字典
    print(arg1)
    print(args)
    print("************")

info(10)
info(10,8,9)
info2(10,a=8, b=9)
print("###########")

def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=3))   #如果单独出现星号 * 后的参数必须用关键字传入


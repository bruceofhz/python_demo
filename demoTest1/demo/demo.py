#!/usr/bin/env python
def foo():
    str="function"
    print(str);

def foo1(num):
    print('num' ,num);

def foo2(name ,age):
    print('name' ,name);
    print('age' ,age);

if __name__=="__main__":
    foo2('yuhui' ,30)
    foo1(6)
    foo()
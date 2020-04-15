sum = lambda t1, t2, t3: t1 + t2 + t3
print(sum(2, 3, 5))

list1 = ['google', 'runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print(list1[0])
del list1[0]
print('list1[0]=', list1[0])

print('list2[1:5]=', list2[1:5])
print('#############')
print('组合：' + str(list1 + list2))
print('重复：' + str(list1 * 3))
print('#############')

print('元素是否存在于列表中:' + str(1997 in list1))
for i in list1:
    print(i)





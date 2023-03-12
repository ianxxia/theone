'''
列表有序 可变的元素集合 列表中的元素不受数据类型
限制
字符串的元素属于一个整体 且不可变

列表是有序可变的而且内部元素是独立的

'''


list = [1,2,3,4,5]
print(list)
print(id(list))

list.append('aaa')
print(list)
print(id(list))
##### id没有变化 证明可变

liststr=['a','b','v']
listfloat=[6.3,5.5,7.4,['python']]
listcomplex=[True,{'name':'hh'}]

listrang=range(0,9)

list1 = [1,2,3,4,5]
res = [num ** 2 for num in list1]

print(res)


name1=['chen','xian','lan','tie']

name2=['python','c#','cpp','c']
#######增加方法
#使用+ * 拼接
list = name1 + name2
print(list)
list = name1 * 3
print(list)



# append
name1.append(123)
print(name1)

listappend = name2.append('hjhjhjh')
print(listappend)###输出None


#extend()  追加元素 int不可迭代 只能输入序列
name1.extend('aaa')
print(name1) #输出['chen', 'xian', 'lan', 'tie', 123, 'a', 'a', 'a']
name1.extend(name2)
print(name1)
#整形非迭代不能使用extend


# insert (索引，元素)
name3=[1,2,3,4]
name3.insert(2,1.5)
print(name3)



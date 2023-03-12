#
#
# class Cat:
#     def __init__(self,num):
#         self.num = num
#
#     def __getitem__(self, item):
#         self.num += 1
#         if self.num >= 10:
#             raise StopIteration()
#         return self.num
#
#
# c = Cat(2)
# for i in c:
#     print(i)
import collections.abc

# isinstance(c,collections.abc.Iterator)#__iter__(),__next__
# isinstance(c,collections.abc.Iterable)



# class Cat:
#     def __init__(self,num):
#         self.num = num
#
#     def __iter__(self):
#         return iter(self.num)#变成可迭代对象
#
# list1=[1,2,3,4,5,6]
# c = Cat(list1)
# for i in c:
#     print(i)

class Cat:
    def __init__(self,num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.num +=1
        if self.num >=10:
            raise StopIteration('遍历结束')
        return self.num

c =Cat(2)
# for i in c:
#     print(i)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
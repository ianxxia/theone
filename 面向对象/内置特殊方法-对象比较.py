
class Num:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __eq__(self, other):
        print(self,'eq里面')
        print(other)
        return self.num1 == other.num1

    def __ne__(self,other):#不等于
        return self.num1 != other.num1

    def __gt__(self,other):#不等于
        return self.num1 > other.num1

    def __ge__(self,other):#不等于
        return self.num1 >= other.num1

    def __lt__(self,other):#不等于
        return self.num1 < other.num1

    def __le__(self,other):#不等于
        return self.num1 <= other.num1




n1 = Num(15,20)#self 代表n1
n2 = Num(15,25)#other 为n2
print(n1)
print(n2)
print(n1 == n2,'外面print')
print(n1 > n2,'外面print')
print(n1 >= n2,'外面print')
print(n1 < n2,'外面print')
print(n1 <= n2,'外面print')

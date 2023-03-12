#统计一个类被实例化多少次


class cat:
    __num =0

    def __init__(self):
        cat.__num += 1



    def __del__(self):
        cat.__num -=1


    @staticmethod
    def total(cls):

        return cls.__num

c = cat()
c1 = cat()
c2 = cat()
print(cat.total())

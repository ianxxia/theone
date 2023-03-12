#一个类拥有多种形态

class person:
    def __init__(self):
        pass
    def run(self):
        print('run')

class man(person):
    def run(self):
        print('run man')

class woman(person):
    def run(self):
        print('run woman')


def func(obj):
    obj.run()

m = man()
wm = woman()
func(m)
func(wm)


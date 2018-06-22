def test(self):
    print('hello')
class dynClass:
    def __int__(self):
        print("from class")


obj = dynClass()
setattr(obj,'myMethod',test)
obj.myMethod()
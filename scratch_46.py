def laptop():
    print("I will read ebooks on Laptop")

def book():
    print("I will read printed Book")

class student:
    def __init__(self,grade):
        self.grade = grade

    def incGrade(self):
        self.grade += 1
        if(self.grade) > 11:
            setattr(self,'Right','laptop')



obj1 = student(1)
obj2 = student(2)


for gr in range(1,13):
    obj2.Right()
    obj2.incGrade()
if obj2.grade>11:
    obj2.Right()



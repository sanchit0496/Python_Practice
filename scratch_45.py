def laptop():
    print("Laptop")

class student:
    def __init__(self,grade):
        self.grade = grade

    def inGrade(self):
        self.grade += 1
        if(self.grade) > 11:
            setattr(self,'Right','laptop')


obj1 = student(1)
obj2 = student(2)


for gr in range(1,12):
    obj2.inGrade()
if obj2.grade>11:
    obj2.Right()



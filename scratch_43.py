class student:
    """My student class"""
    noOfStudent = 0
    classTeacher = 'Anand Paradkar'

    @staticmethod
    def showClassTeacher():
        return(student.classTeacher)

    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        self.grade = grade = ''
        noOfStudent =+ 1

    def clgrade(self):
        if self.marks>80:
            self.grade = "A"
        elif self.marks>=70:
            self.grade = "B"
        elif self.marks>=60:
            self.grade = "C"
        elif self.marks>=50:
            self.grade = "D"
        else:
            self.grade = "E"
        return self.grade


s1=student(111, "Prema", 84)
#class using getattr method
v = getattr(s1,'name')
print(v)

#class using setattr method
x = setattr(s1,'name','Adi')
print(s1.name)

#class using hasattr method

if hasattr(s1, 'height'):
    print('yes')
else:
    print('nopes')

if hasattr(s1, 'name'):
    print('yes')
else:
    print('nopes')



# class using hasattr method
delattr(s1, 'name')
print(s1.name)

if hasattr(s1, 'name'):
    print('yes')
else:
    print('nopes')


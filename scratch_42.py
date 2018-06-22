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
        #self.__maxmarks = 100 #private runs only in the class and nowhere else
        self.__maxmarks = 100


        noOfStudent =+ 1

    def clgrade(self):
        print(self.__maxmarks)
        if self.marks>=80:
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
s2=student(112, "Hello", 69)
s3=student(113, "World", 59)
s4=student(114, "Hey", 49)
s5=student(115, "There", 39)

print("Roll No.", s1.rollno, "Name", s1.name, "Marks", s1.marks, "Grade", s1.clgrade())
print("Roll No.", s2.rollno, "Name", s2.name, "Marks", s2.marks, "Grade", s2.clgrade())
print("Roll No.", s3.rollno, "Name", s3.name, "Marks", s3.marks, "Grade", s3.clgrade())
print("Roll No.", s4.rollno, "Name", s4.name, "Marks", s4.marks, "Grade", s4.clgrade())
print("Roll No.", s5.rollno, "Name", s5.name, "Marks", s5.marks, "Grade", s5.clgrade())


print(student.showClassTeacher())
print(s1.__dict__)
print(student.__name__)
print(s1.__class__.__name__)
print(s1.__module__)
print(student.__doc__)
print(student.__bases__)
#print(s1.maxmarks)
print(s1.maxmarks)
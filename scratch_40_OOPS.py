class Shirt:
    def __init__(self,color,material):
        self.color=color
        self.material=material
        self.state='Clean'
    def makeDirty(self):
        self.state='Dirty'
    def cleanIt(self):
        self.state='Clean'


s1=Shirt('Red','Cotton')
s2=Shirt('Blue','Silk')
s3=Shirt('Yellow','Khaki')
s4=Shirt('Green','Denim')



print(s1.color, " " , s1.material, " " ,s1.state)

s1.makeDirty()
print(s1.color, " " , s1.material, " " ,s1.state)


print(s2.color, " " , s2.material, " " ,s2.state)

s1.makeDirty()
print(s2.color, " " , s2.material, " " ,s2.state)


print(s3.color, " " , s3.material, " " ,s3.state)

s1.makeDirty()
print(s3.color, " " , s3.material, " " ,s3.state)

print(s4.color, " " , s4.material, " " ,s4.state)

s1.makeDirty()
print(s4.color, " " , s4.material, " " ,s4.state)

print(type(s1), " ", id(s1))
print(type(s2), " ", id(s2))

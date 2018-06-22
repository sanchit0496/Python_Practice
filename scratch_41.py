class point:
    def __init__(self, x=0, y=0):
        self.x,self.y = x,y
    def __str__(self):
        string = "("+str(self.x)+","+str(self.y)+")"
        return string

    def __del__(self):
        print("Delete")

pt1 = point(3,4)
pt2 = point(8,9)
pt3 = pt2


print(pt1)
print(pt2)
print(pt3)

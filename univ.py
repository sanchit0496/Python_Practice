p = float(input('Enter Marks '))
c = float(input('Enter Marks '))
m = float(input('Enter Marks '))

g = (((p+c+m)/300)*100)

if  g >= 80:
    print ("First Div")
elif g > 60 and g < 80:
        print ("Second Div")
elif g > 40 and g < 60:
        print ("Third Div")

print("Marks")


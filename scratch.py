n = int(input('Enter Number '))
p = 2
while(n%p == 1):
    p = p + 1
    print("The number is prime")
    break
else:
    print("The number is not prime")


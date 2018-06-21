seta = {'a','b','c','d'}
setb = {'c','d','e','f'}

print(seta - setb)
print(setb - seta)
print(seta | setb)
print(setb | seta)
print(seta & setb)
print(seta ^ setb)

if 'a' in (seta - setb):
    print('Hello')
else:
    print('Hey')
basket={'Apple','Orange','Apple','Banana','Orange','Mango'}
a=set('Apple')
print(a)

basket.add('Strawberry')
print(basket)

a=set()
print(a)

if 'Mango' in basket:
    print('Hello')
else:
    print('Hey')


if 'pear' in basket:
    print('Hello')
else:
    print('Hey')


if 'pear' not in basket:
    print('Hello1')
if 'pear' in basket:
    print('Hey1')

if 'Strawberry' in basket:
    print('Hey1')
if 'pear' in basket:
    print('Hello')

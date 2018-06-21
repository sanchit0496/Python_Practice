D={101:"Apple",102:"Ball",103:"Cat",104:"Dog"}
for k,v in D.items():
    print('Key=', k , 'Value=', v)

#.get() will only work for the keys and not for the values
print(D.get(101))
print(D.get(102))
print(D.get(103))
print(D.get(104))

D[101]="Aeroplane"
print(D)

D[105]="Elephant"
print(D)

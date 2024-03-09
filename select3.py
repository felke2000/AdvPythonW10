import numpy as np

lista1=list(np.random.randint(1,10,200))
lista2=list(np.random.randint(1,10,200))

print(lista1)
print(lista2)

lista1.append(9/3)
lista2.append(3)

print(lista1)
print(lista2)

for i in range(len(lista1)):
    if lista1[i]==lista2[i]:
        print("what was wanted",i,lista1[i])
        break














"""
import numpy as np

lista1=list(np.random.randint(1,100,20))
lista2=list(np.random.randint(50,150,20))

print(lista1)
print(lista2)

lista1.append(6/5)
lista2.append(1.2)

print(lista1)
print(lista2)
"""
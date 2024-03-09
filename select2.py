#what does this program doing
import numpy as np

lista = np.random.randint(1,100,20)
print(lista)

other =[]

for i in range(len(lista)):
    other.append(lista[i]+lista[i+1])
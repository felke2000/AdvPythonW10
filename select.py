import numpy

lista = numpy.random.randint(1,100,20)
print(lista)

other=[]
for elem in lista:
    if elem%2==1:
        other.append(elem)

print(elem)





i=0
k=0
while i<9:
    i=i+1
    if i%4==0:
        i=i-1
    k+=1
    print("step ",k," i=",i)
    if k==6:
        break
print(i)
import sys
def add(x,y):
    summ = x+y
    return summ

if __name__=="__main__":
    print("This is the name of the program:",sys.argv[0])
    print("Number of elements excluding the name of the program:", (len(sys.argv) - 1))
    print("Argument List:", str(sys.argv))

    z = add(sys.argv[1],sys.argv[2])
    print(z)
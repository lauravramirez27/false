def fibonacci():
    n1= 0
    n2= 1
    can=20
    
    array =[n1, n2]

    for i in range(can):
        cantidad =len(array)
        s1=array[cantidad-1]
        s2=array[cantidad-2]
        total=s1+s2
        array.append(total)
    print("Fibonacci: ",array)
    n=int(input("ingrese el numero que desea ver del fibonacci: "))
    ver =array[n]
    print(ver)
fibonacci()


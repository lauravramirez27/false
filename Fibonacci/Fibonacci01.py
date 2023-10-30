def fibonacci():
    n1= 0
    n2= 1
    can=20
    
    array =[n1, n2]
    x=0
    for i in range(can):
        cantidad =len(array)
        s1=array[cantidad-1]
        s2=array[cantidad-2]
        total=s1+s2
        array.append(total)
    print("Fibonacci: ",array)
    n=int(input("ingrese el numero que desea ver del fibonacci: "))
    ver=array[n]
    print(ver)
    e=int(input("ingrese el numero, para ver si es del fibonacci: "))
    for i in range(len(array)):
        if array[i]!=e:
            x=0
        else:
            x=1
            break
    if x==0:
        print(e," no es numero de fibonacci")
    else:
        print(e," es numero de fibonacci")
    m=int(input("Ingrese m (la cantidad de numeros que quiere ver del fibonacci):"))
    nuevo=[]
    for i in range(m):
        nuevo.append(array[i])
    print("los primeros ",m," numeros de fibonacci son: " ,nuevo)
    
             
fibonacci()


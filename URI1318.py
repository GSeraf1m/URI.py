entrada=raw_input().split()
n=int(entrada[0])
m=int(entrada[1])
while n!=0 and m!=0:
    array=[0]*10000
    cont=0
    entradas=raw_input().split()
    for i in xrange(m):
        array[int(entradas[i])]+=1
        if array[int(entradas[i])]==2:
            cont+=1
    print cont
    entrada=raw_input().split()
    n=int(entrada[0])
    m=int(entrada[1])

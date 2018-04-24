a=input()
for index in xrange(a):
    cont=0
    n=input()
    entradas=raw_input().split()
    tiros=[]
    for i in xrange(n):
        tiros.append(int(entradas[i]))
    entrada=raw_input()
    pulos=entrada
    for i in xrange(n):
        if pulos[i]=='J' and tiros[i]>2:
            cont+=1
        elif pulos[i]=='S' and tiros[i]<3:
            cont+=1
    print cont

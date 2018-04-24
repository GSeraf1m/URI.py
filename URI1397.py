n=input()
while(n!=0):
    acont,bcont=0,0
    for i in xrange(0,n,1):
        entradas = raw_input().split()
        a=int(entradas[0])
        b=int(entradas[1])
        if a>b:
            acont+=1
        elif b>a:
            bcont+=1
    print acont,bcont
    n=input()

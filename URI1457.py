a=input()
for index in xrange(a):
    entrada=raw_input().split("!")
    n=int(entrada[0])
    k=len(entrada)-1
    valor=n
    for i in xrange(1,n-1,1):
        x=n-(i*k)
        if x>0:
            valor*=n-(i*k)
    print valor

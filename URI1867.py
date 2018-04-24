entradas=raw_input().split()
a,b=entradas[0],entradas[1]
while(a!='0' or b!='0'):
    while(len(a)>1):
        soma=0
        for i in xrange(len(a)):
            soma+=int(a[i])
        a=str(soma)
    while(len(b)>1):
        soma=0
        for i in xrange(len(b)):
            soma+=int(b[i])
        b=str(soma)
    if a>b:
        print 1
    elif b>a:
        print 2
    else:
        print 0
    entradas=raw_input().split()
    a,b=entradas[0],entradas[1]

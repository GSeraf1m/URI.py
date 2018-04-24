n=input()
for index in xrange(n):
    a=input()
    esferas=a
    for i in xrange(1,a+1):
        cont=0
        for ind in xrange(1,a+1):
            if i%ind==0:
                cont+=1
        if cont%2!=0:
            esferas-=1
    print esferas

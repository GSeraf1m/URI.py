a=input()
for index in xrange(a):
    entrada=raw_input().split()
    x,y=int(entrada[0]),int(entrada[1])
    soma=0
    if x<y:
        for i in xrange(x+1,y,1):
            if i%2!=0:
                soma+=i
    else:
        for i in xrange(y+1,x,1):
            if i%2!=0:
                soma+=i
    print soma

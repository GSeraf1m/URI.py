a=input()
for i in xrange(a):
    entradas=raw_input().split()
    x,y=int(entradas[0]),int(entradas[1])
    x=x/3
    y=y/3
    print x*y

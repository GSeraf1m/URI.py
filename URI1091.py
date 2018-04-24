a=input()
while(a!=0):
    entrada=raw_input().split()
    x=int(entrada[0])
    y=int(entrada[1])
    for i in xrange(a):
        entrada=raw_input().split()
        x1=int(entrada[0])
        y1=int(entrada[1])
        if x1==x or y1==y:
            print "divisa"
        elif x1>x and y1>y:
            print "NE"
        elif x1>x and y1<y:
            print "SE"
        elif y1>y and x1<x:
            print "NO"
        else:
            print "SO"
    a=input()

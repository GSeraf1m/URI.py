n=input()
for i in xrange(n):
    entrada=raw_input().split()
    x,y=int(entrada[0]),int(entrada[1])
    rafael=((3*x)**2)+y**2
    beto=(2*(x**2))+((5*y)**2)
    carlos=(-100*x)+y**3
    if carlos>beto and carlos>rafael:
        print "Carlos ganhou"
    elif beto>rafael:
        print "Beto ganhou"
    else:
        print "Rafael ganhou"

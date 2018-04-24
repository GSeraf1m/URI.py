a=input()
cont=0
for i in xrange(0,1000):
    print "N[%d] = %d"%(i,cont)
    cont+=1
    if a==cont:
        cont=0

i,j=1,7
for x in xrange(1,16,1):
    print "I=%d J=%d"%(i,j)
    j-=1
    if(x%3==0):
        i+=2
        j=7
    

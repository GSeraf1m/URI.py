a=[0]*100
for i in xrange(len(a)):
    a[i]=input()
for i in xrange(len(a)):
    if a[i]<=10:
        print "A[%d] = %1.1f"%(i,a[i])

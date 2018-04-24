a=input()
n1=0
n2=1
print n1,n2,
for i in xrange(2,a):
    n3=n1+n2
    print n3,
    n1=n2
    n2=n3

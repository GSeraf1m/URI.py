n=input()
for i in xrange(n):
    entrada=raw_input().split()
    a,b=int(entrada[0]),int(entrada[1])
    area=(a*b)/2
    print area,"cm2"

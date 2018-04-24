entrada=raw_input().split()
a,b,c=int(entrada[0]),int(entrada[1]),int(entrada[2])
while(a!=0 and b!=0 and c!=0):
    cubo=(a*b*c)
    print "%1.0f"%int(cubo**(1./3))
    entrada=raw_input().split()
    a,b,c=int(entrada[0]),int(entrada[1]),int(entrada[2])

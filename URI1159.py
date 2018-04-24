a=input()
while(a!=0):
    soma=0
    if a%2==0:
        for i in xrange(a,a+9,2):
            soma+=i
    else:
        a+=1
        for i in xrange(a,a+9,2):
           soma+=i
    print soma
    a=input()

a=input()
while(a!=0):
    b=a
    while(a!=1):
        if(a%2==0):
            a/=2
        else:
            a*=3
            a+=1
        if(a>b):
            b=a
    print b
    b=0
    a=input()

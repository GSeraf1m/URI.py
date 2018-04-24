a=input()
for i in xrange(0,a,1):
    cont=0
    x=input()
    while(x>1):
        x-=(x/2)
        cont+=1
    print cont,"dias"

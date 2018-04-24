a=input()
while(True):
    x=[]
    tam = 0
    for i in xrange(a):
        x.append(' '.join(raw_input().split()))
        tam = max(tam, len(x[i]))
    for i in xrange(a):
        print x[i].rjust(tam)
    a=input()
    if (a!=0):
        print ""
    else:
        break;

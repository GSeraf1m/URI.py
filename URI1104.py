entrada=raw_input().split()
a,b=int(entrada[0]),int(entrada[1])
while(a!=0 and b!=0):
    alice=[0]*100001
    beatriz=[0]*100001
    al,be=0,0
    entrada=raw_input().split()
    for i in xrange(a):
        alice[int(entrada[i])]+=1
    entrada=raw_input().split()
    for i in xrange(b):
        beatriz[int(entrada[i])]+=1
    for i in xrange(100001):
        if alice[i]!=0 and beatriz[i]==0:
            al+=1
        elif alice[i]==0 and beatriz[i]!=0:
            be+=1
    if be>al:
        print al
    else:
        print be
    entrada=raw_input().split()
    a,b=int(entrada[0]),int(entrada[1])

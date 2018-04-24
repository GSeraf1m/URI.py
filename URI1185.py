letra=raw_input()
a=[]
soma=0.0
for i in xrange(12):
    a.append([])
    for index in xrange(12):
        a[i].append(input())
        if(index<11-i):
            soma+=a[i][index]
if(letra=="S"):
    print "%1.1f"%soma
else:
    print "%1.1f"%(soma/66.0)        

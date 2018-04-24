n=input()
for index in xrange(n):
    entrada=raw_input().split()
    p1,p2,cont=entrada[0],entrada[1],0
    for i in xrange(len(p2)):
        if(ord(p2[i])>ord(p1[i])):
            cont+=ord(p2[i])-ord(p1[i])
        elif(ord(p2[i])<ord(p1[i])):
            cont+=26-ord(p1[i])+ord(p2[i])
    print cont

entrada=raw_input().split()
while(int(entrada[0])!=0 and int(entrada[1])!=0 and int(entrada[2])!=0 and int(entrada[3])!=0):
    x1,y1,x2,y2=int(entrada[0]),int(entrada[1]),int(entrada[2]),int(entrada[3])
    cont=0
    if x1==x2 and y1==y2:
        cont=0
    elif x1==x2 or y2==y1:
        cont=1
    elif ((x1-x2)**2)==((y1-y2)**2):
        cont=1
    else:
        cont=2
    print cont
    entrada=raw_input().split()

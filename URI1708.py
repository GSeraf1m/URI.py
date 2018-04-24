entrada=raw_input().split()
a,b=int(entrada[0]),int(entrada[1])
cont=1
b=b-a
while(a>0):
    a-=b
    cont+=1
print cont

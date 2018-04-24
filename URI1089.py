n=input()
while(n!=0):
    picos=0
    entrada=raw_input().split()
    for i in xrange(1,n-1):
        if int(entrada[i+1])>int(entrada[i]) and int(entrada[i])<int(entrada[i-1]):
            picos+=1
        elif int(entrada[i+1])<int(entrada[i]) and int(entrada[i])>int(entrada[i-1]):
            picos+=1
    if int(entrada[0])>int(entrada[n-1]) and int(entrada[n-1])<int(entrada[n-2]):
        picos+=1
    if int(entrada[0])<int(entrada[n-1]) and int(entrada[n-1])>int(entrada[n-2]):
        picos+=1
    if int(entrada[1])<int(entrada[0]) and int(entrada[0])>int(entrada[n-1]):
        picos+=1
    if int(entrada[1])>int(entrada[0]) and int(entrada[0])<int(entrada[n-1]):
        picos+=1
    print picos
    n=input()

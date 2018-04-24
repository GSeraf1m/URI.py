n=input()
while(n!=0):
    for i in xrange(n):
        entrada=raw_input().split()
        a,b,c,d,e=int(entrada[0]),int(entrada[1]),int(entrada[2]),int(entrada[3]),int(entrada[4])
        if a<=127 and b>127 and c>127 and d>127 and e>127:
            print "A"
        elif a>127 and b<=127 and c>127 and d>127 and e>127:
            print "B"
        elif a>127 and b>127 and c<=127 and d>127 and e>127:
            print "C"
        elif a>127 and b>127 and c>127 and d<=127 and e>127:
            print "D"
        elif a>127 and b>127 and c>127 and d>127 and e<=127:
            print "E"
        else:
            print "*"
    n=input()

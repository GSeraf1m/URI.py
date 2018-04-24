from __future__ import print_function
try:
    while True:
        p=raw_input()
        for index in xrange(len(p)):
            for i in xrange(len(p)-index):
                if i==0 or index==len(p):
                    print (p[i].rjust(index+1), end= "")
                elif i==len(p)-index:
                    print (p[i],end= "\n")
                else:
                    print (" "+p[i],end= "")
            print ("")
        print("")
except EOFError:
    pass

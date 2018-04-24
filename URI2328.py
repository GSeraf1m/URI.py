n=input()
total=0
entrada=raw_input().split()
for i in xrange(n):
    total+=int(entrada[i])
print total-n

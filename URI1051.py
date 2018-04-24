a=input()
if 0<a and a<=2000:
    print"Isento"
elif 2000<a and a<=3000:
    b=a-2000
    c=b*0.08
    print"R$ %1.2f"%c
elif 3000<a and a<=4500:
    b=a-2000
    b1=b-1000
    d=1000*0.08
    e=b1*0.18
    print"R$ %1.2f"%(d+e)
else:
    b=a-2000
    b1=b-1000
    d=1000*0.08
    b2=b1-1500
    e=1500*0.18
    c=b2*0.28
    print"R$ %1.2f" %(c+d+e)

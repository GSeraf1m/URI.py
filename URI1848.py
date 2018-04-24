x=0
num=0
while(x<3):
    e=raw_input()
    if len(e)>0:
        if e!="caw caw":
            if e[0]=='*':
                num+=4
            if e[1]=='*':
                num+=2
            if e[2]=='*':
                num+=1
        else:
            x+=1
            print num
            num = 0

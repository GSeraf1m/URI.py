try:
    while True:
        caps=True
        SeNtEnCaDaNcAnTe=""
        x=""
        sentenca=raw_input()
        for i in xrange(len(sentenca)):
            if caps and sentenca[i]!=' ':
                x=sentenca[i]
                SeNtEnCaDaNcAnTe+=x.upper()
                caps=False
            elif (not caps) and sentenca[i]!=' ':
                x=sentenca[i]
                SeNtEnCaDaNcAnTe+=x.lower()
                caps=True
            else:
                SeNtEnCaDaNcAnTe+=sentenca[i]
        print SeNtEnCaDaNcAnTe
except EOFError:
    pass

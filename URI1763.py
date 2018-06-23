try:
    while True:
        a=raw_input()
        if a=="brasil" or a=="portugal":
            print "Feliz Natal!"
        elif a=="alemanha":
            print "Frohliche Weihnachten!"
        elif a=="austria":
            print "Frohe Weihnacht!"
        elif a=="coreia":
            print "Chuk Sung Tan!"
        elif a=="espanha" or a=="argentina" or a=="chile" or a=="mexico":
            print "Feliz Navidad!"
        elif a=="grecia":
            print "Kala Christougena!"
        elif a=="estados-unidos" or a=="inglaterra" or a=="australia" or a=="antardida" or a=="canada":
            print "Merry Christmas!"
        elif a=="suecia":
            print "God Jul!"
        elif a=="turquia":
            print "Mutlu Noeller!"
        elif a=="irlanda":
            print "Nollaig Shona Dhuit!"
        elif a=="belgica":
            print "Zalig Kerstfeest!"
        elif a=="italia" or a=="libia":
            print "Buon Natale!"
        elif a=="siria" or a=="marrocos":
            print "Milad Mubarak!"
        elif a=="japao":
            print "Merii Kurisumasu!"
        else:
            print "--- NOT FOUND ---"
except EOFError:
    pass

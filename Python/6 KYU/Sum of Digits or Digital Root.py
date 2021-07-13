def digital_root(n):
    # ...
    tes = str(n)
    a= 0
    for i in tes:
        a+=int(i)
    tes2 = str(a)
    if len(tes2)==1:
        return a
    b = 0
    if (len(tes2)!=1):
        for i in str(a):
            b+=int(i)
    tes3 = str(b)
    if len(tes3)==1:
        return b
    c = 0
    if (len(tes3)!=1):
        for i in str(b):
            c+=int(i)
        return c

def alphabet_position(text):
    tes = ''
    a = 0
    for i in text:
        if ord(i)>96 and ord(i)<123:
            a = ord(i) - 96
            tes += str(a)+' '
        elif ord(i)>64 and ord(i)<91:
            a = ord(i) - 64
            tes += str(a)+' '
    
    return tes[:len(tes)-1]

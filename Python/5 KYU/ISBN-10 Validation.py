def valid_ISBN10(isbn): 
    if len(isbn) < 10 or isbn.isalpha() or len(isbn) > 10:
        return False
    a = 0
    for i in range (0,len(isbn)):
        if isbn[i].isdecimal():
            a += int(isbn[i]) * (i+1)
        elif isbn[i] == "X" and i == 9:
            a += 10 * (i+1)
        else:
            return False
    # your code here
    if a % 11 == 0:
        return True
    else:
        return False

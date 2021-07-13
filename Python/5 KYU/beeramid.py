def beeramid(bonus, price):
    if bonus <= 0:
        return 0
    bills = 0
    i = 1
    a = 0
    while bills < bonus:
        a += i*i
        bills = a*price
        if bills > bonus:
            i -= 1
        elif bills == bonus:
            pass
        else:
            i += 1
    return i
        
    # your code

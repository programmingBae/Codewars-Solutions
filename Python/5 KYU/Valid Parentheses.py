def valid_parentheses(string):
    #your code here
    if len(string)==0:
        return True
    count_a = 0
    count_b = 0
    checker = True #works like a saclar
    for i in string:
        if i  == '(':
            count_a += 1
            checker = False
        elif i  == ')':
            count_b += 1
            if count_a==0:
                return False
            if count_a == count_b and checker==False:
                checker = True
            elif count_b>count_a and checker==True:
                return False
            
    if count_a == count_b and checker   :
        return True
    else:
        return False

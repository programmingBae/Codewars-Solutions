def guess_gifts(wishlist, presents): 
    # your code here
    array = []
    for i in presents: # sorry im just too lazy so that i named it i and j
        for j in wishlist:
            if j['size'] == i['size'] and j['clatters'] == i['clatters'] and j['weight'] == i['weight']:
                array.append(j['name'])
    return set(array)

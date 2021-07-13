def duplicate_encode(word):
    #your code here
    word = word.lower()
    tes = ''
    for i in range (0,len(word),1):
        if word.count(word[i]) == 1:
            tes += '('
        else:
            tes+=')'
    return tes

def anagrams(word, words):
    #your code here
    result = []
    match = sorted(word)
    for w in words:
        if match == sorted(w):
            result.append(w)
    return result

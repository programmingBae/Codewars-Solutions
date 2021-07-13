def first_non_repeating_letter(string):
    stringLower = string.lower()
    for i in range (len(string)):
        if stringLower.count(stringLower[i]) == 1:
            return string[i]
    return ""

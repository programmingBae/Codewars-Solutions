def solution(array_a, array_b):
    temp = 0
    for i in range (len(array_a)):
        temp+=(array_a[i]-array_b[i])**2
    return temp/len(array_a)

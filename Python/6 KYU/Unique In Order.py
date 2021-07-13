def unique_in_order(iterable):
    result = []
    tes = ''
    for i in iterable:
        if tes!=i:
            tes = i
            result.append(i)
    return result

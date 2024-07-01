def recursive(start=0, end=10):

    if start >= end:
        return end

    start += 1
    return recursive(start, end)


print(recursive())

def intersection(arrays):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for stuff in arrays:
        for things in stuff:
            if things not in cache:
                cache[things] = 1
            elif things in cache:
                cache[things] += 1
            if cache[things] == len(arrays):
                result.append(things)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))

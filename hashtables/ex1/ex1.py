def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    cache = {}
    for i in range(len(weights)):
        if limit - weights[i] in cache:
            return [i, cache[limit - weights[i]]]
        if weights[i] not in cache:
            cache[weights[i]] = i

    return None

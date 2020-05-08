#  Hint:  You may not need all of these  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    cache = {}
    for i in tickets:
        cache[i.source] = i.destination
    route = [None] * length
    cur_source = ''
    for i in range(length):
        route[i] = cache[cur_source]
        cur_source = cache[cur_source]


    return route

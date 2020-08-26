"""
function to count the frequency of each elements.
"""
def count_frequency(mylist):
    """Return count of each elements."""
    count = {}
    for i in [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]:
        count[i] = count.get(i, 0) + 1
    return count

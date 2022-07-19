"""
Exponential Time O(3**n)
"""

from itertools import chain,combinations


def subset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


print(list(subset(['a','b','c'])))
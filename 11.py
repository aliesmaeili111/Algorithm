"""
    Is isomorphic
    foo , bar => False
    foo , bee => True
"""

def is_isomorphic(s,t):
    if len(s) != len(t):
        return False
    
    dic = {}
    set_values = set()
    
    for i in range(len(s)):
        if s[i] not in dic:
            if t[i] in set_values:
                return False
            dic[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dic[s[i]] != t[i]:
                return False
    return True
    
print(is_isomorphic('foe','bee'))
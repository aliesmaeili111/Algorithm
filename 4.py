"""
Linear Time O(n)
"""

nums = [0,4,5,98,100,110,111,220,300,450,500,550,558,595,600,610]


def show(list1):
    max_nums = list1[0]
    for i in list1:
        if i > max_nums :
            max_nums = i 
            
    return max_nums

print(show(nums))
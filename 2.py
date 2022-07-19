"""
Constant Time O(1)

"""

nums = [4,5,98,121,45,5564]


def show(list1):
    if list1[0] % 2 ==0 :
        return 'Even'
    return 'Odd'

print(show(nums))
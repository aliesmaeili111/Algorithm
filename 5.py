"""
Polynomial Time O(n*n)
"""

nums = [100,110,1] # [100,1,110]


def bubble_sort(list1):
    length = len(list1)
    for i in range(length - 1): # i = 0 ,1
        swapped = False
        for j in range(length - 1 - i) : # j = 0 ,1 
            if list1[j] > list1[j+1]:
                swapped = True
                list1[j],list1[j+1] = list1[j+1] ,list1[j]
        if not swapped : 
            break
    return list1


print(bubble_sort(nums))
"""
Complexity
    Time     Space
"""

nums = [0,4,5,98,100,110,111,220,300,450,500,550,600,650,4555]

def show_element(list1,element):
    for i in list1:
        if i == element :
            return list1.index(i) + 1
        
print(show_element(nums,110))
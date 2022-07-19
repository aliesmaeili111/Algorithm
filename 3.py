"""
Logorithm Time O(log n)
"""

nums = [0,4,5,98,100,110,111,220,300,450,555,556,755,845,950,1000]

# binary search

def show_element(list1,element):
    
    first,last = 0,len(nums)-1 
    
    while first <= last:
        middle = (first+last) // 2
        if nums[middle] == element : 
            print(middle + 1)
            break
        elif nums[middle] > element :
            last = middle - 1 
        else:
            first = middle + 1  
    else:
        return "Not Found"
    
(show_element(nums,110))
        
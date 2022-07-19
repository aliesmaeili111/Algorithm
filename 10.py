"""
        Search insert
        [1,2,3,4],3 => 2
        [1,2,3,4],5 => 4
        [1,2,3,4],0 => 0
"""


def search_insert(array,val):
    low = 0
    high = len(array) - 1 # 3
    mid = high // 2 # 3//2 = 1
    
    while low <= high: # 1 < 3 True
        if val > array[mid]: # 3 >
            mid +=1 
            low = mid
        else:
            mid -= 1
            high = mid
    return low

print(search_insert([1,2,3,4],3))
# Attempting a recursive sorting function

def quick_sort(list):
    #defining the base cases
    if len(list) < 2:    #base case: empty list or with one element
        return list
    else:
        pivot  = list[0]    #choosing first element as pivot
        lower  = [val for val in list if val < pivot]
        higher = [val for val in list if val > pivot]
        return quick_sort(lower) + [pivot] + quick_sort(higher)




# Test cases:
cases = {1: [2,7,1,9,5,10], 2: [34,29,11,39,56,100,291,3], 3: [9,5,10,0]}

#looping through cases:

for num,test_list in cases.items():
    print(f"Case {num}:\n\tOriginal list: {test_list}\n\
        Sorted list: {quick_sort(test_list)}\n\n")
    

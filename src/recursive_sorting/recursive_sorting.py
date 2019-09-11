# TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO
    
#     return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort( arr ):
#     # TO-DO

#     return arr

'''
sample list 
a = [7,2,5,9]

 How this works. 

 1. Take in the list of data
 2. Find the middle of the list by dividing the list by 2
 3. Create a right and left list
 4. Via recursion, pass through the lists until they get down to their smallest component.  For instance, the left list
    would become a left and right list with the values 7 and 2. (Assuming you're using the list posted above).
 5. Then the values are checked for the right and left sublists
'''

def mergesort(list):
    if len(list)>1: # base case
        middle = len(list)//2
        left_list = list[:middle]
        right_list = list[middle:]
        mergesort(left_list)
        mergesort(right_list)
        x=0
        y=0
        z=0
        # this is the condition for merging
        while x < len(left_list) and y < len(right_list):
            if left_list[x] < right_list[y]:
                list[z] = left_list[x]
                x = x + 1
                z = z + 1
            else:
                list[z] = right_list[y]
                y = y+1
                z = z+1
        # this is to check for any values in the left or right sublists
        while x < len(left_list):
            list[z] = left_list[x]
            x = x + 1
            z = z + 1
        while y < len(right_list):
            list[z] = right_list[y]
            y = y + 1
            z = z + 1
            
a=[5,3,8,9,4,7,11]
mergesort(a)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

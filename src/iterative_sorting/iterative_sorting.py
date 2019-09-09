# TO-DO: Complete the selection_sort() function below 

'''
How this works

* sample array [5,2,6,0]

1. Pass the array into selection_sort
2. Iterate through the entire array using a for loop
3. Grab the minium value number (not the index). In this case, 0.
4. Locate where that is within the index.  In this case, 3
5. So...we have a value of 0 in the index 3 position
6. Now we swap the number 0 in the index 3 with the number 5 in the index 0
'''

def selection_sort(arr):
    for i in range(len(arr)):
        minimum_val = min(arr[i:])
        minimum_ind = arr.index(minimum_val)
        arr[i], arr[minimum_ind] = arr[minimum_ind], arr[i]
    return(arr)
    



# TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr
'''
How this works

* sample array [5,2,6,0]

1. Pass the array to bubble_sort.
2. (i) is the first of two loops.  We start at index 0, then go to the end of the array length
3. (j) is the second loop. Same process as above
4. (j) will check to see if the value of it's current number is larger than the number to the right of it
   If so, it will swap its index location and number with the number to the right
'''
def bubble_sort(arr):
    for i in range(0, len(arr) -1):
        for j in range(0, len(arr) -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
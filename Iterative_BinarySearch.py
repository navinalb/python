# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1
 
def navBinarySearch(arr,start,end,x):
    while start <= end:
        
        mid = start + (end-start) // 2
        print ("mid:", mid)
        print ("value at mid:" , arr[mid])
        
        #check if mid has x
        if arr[mid] == x:
            print ("inside 1st if loop")
            return mid
            
        elif arr[mid] < x:
            print ("inside elif")
            start = mid + 1
        else:
            print ("inside else")
            end = mid - 1
            
    return -1
    

arr = [2,4,6,8,12,23,34,54,56,76]
x = 54


# Function call
result = navBinarySearch(arr,0,len(arr)-1,x)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
    
    # Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

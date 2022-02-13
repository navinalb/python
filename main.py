# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1
 
def Myfirstfun(navarr, navlen, x):
     
    for i in range(1,navlen):
        if navarr[i]==x:
            return i
    return -1
    
navarr = [2,5,1,6,8,9,7,1]
navlen = len(navarr)
x = 8
 

# Function call
result = Myfirstfun(navarr, navlen, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
    
    # Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

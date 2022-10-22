if high >= low:
 
        mid = (high + low) // 2
 
     
            return binary_search(arr, low, mid - 1, x)
 
   
        else:
            return binary_search(arr, mid + 1, high, x)
 

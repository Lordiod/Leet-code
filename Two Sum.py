def sortyyyy(arr,n):
    count = 0
    
    for i in range(0,n):
        if arr[i] == 0:
            count += 1
            
    for i in range(0,count):
        arr[i] = 0
    
    for i in range(count,n):
        arr[i] = 1
        
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
n= len(arr)
sortyyyy(arr,n)
print(arr)
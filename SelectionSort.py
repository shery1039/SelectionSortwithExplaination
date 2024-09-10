def selection_Sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        mini_value=i
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                mini_value=j
                arr[i],arr[mini_value]=arr[mini_value],arr[i]
        
arr = [24, 41, 33, 42, 17]
result = selection_Sort(arr)
print(arr)  # [17, 24, 33, 41, 42]
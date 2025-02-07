def binary_serch(arr,target):
            low=0
            high=len(arr)-1
            while low<=high:
                 mid=(low+high)//2
            if arr[mid]==target:
                    return mid
            elif arr[mid]<target:
                    low=mid+1
            else:
                    high=mid-1
                    
                  
arr=[1,2,3,4,5]
target=4
index=binary_serch(arr,target)
if(index!=-1):
        print(target,"found at index",index) 
else:
        print(target,"not found")                   
                    

                    
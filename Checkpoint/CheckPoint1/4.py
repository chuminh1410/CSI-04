a=[1,2,5,7,15,22,41,55,65,73,82,91] # sorted array
def tim_kiem_nhi_phan(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = ((low+high)//2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid - 1
    return -1

x = 22
result = tim_kiem_nhi_phan(a,x)
print("Kết quả x ở vị trí: " + str(result))

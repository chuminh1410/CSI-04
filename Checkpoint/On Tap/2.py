a = [2,4,6,7,9,11]
x = 7
def tim_kiem_nhi_phan(a,x):
    low = 0
    high = len(a)-1
    while low<= high:
        mid = (low+high)//2
        if a[mid] == x:
            return mid 
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid-1

print(f'kết quả x ở vị trí : {tim_kiem_nhi_phan(a,x)}')
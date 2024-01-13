def bubble_sort(a):
    lenarr = len(a)

    for i in range(lenarr):
        for j in range(0, lenarr-i-1):
            if a[j] > a[j+1]:
                print(f"Swapping {a[j]} and {a[j+1]}")
                a[j], a[j+1] = a[j+1], a[j]

def binary_search(a,x):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = ((low+high)//2)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid+1
        else:
            high = mid - 1
    return -1

def tim_tuyen_tinh(a,x):
    for i in range(len(a)):
        if a[i] ==x:
            return i
    return -1

a=[0,9,1,5]
x = 9
bubble_sort(a)
print(a)
result = binary_search(a,x)
print(f"Số {x} được tìm ở vị trí (binary search) :{result}") 
result = tim_tuyen_tinh(a,x)
print(f"Số {x} được tìm ở vị trí (tuyến tính) :{result}")



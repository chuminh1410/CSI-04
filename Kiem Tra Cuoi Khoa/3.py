a = []
for i in range(0,6):
    b = int(input("Enter a number: "))
    a.append(b)
print(f'Dãy a là: {a}')

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(a)
print(a)

def binary_search(a,min_even):
    #gọi 2 phần chia đôi đó là low và high (thấp và cao)

    low = 0
    high = len(a)-1
    while low <= high:
        #chia đôi mảng cần tìm kiếm và vị trí ở giữa gọi là mid
        mid = ((low+high)//2)
        #nếu phần tử cần tìm ở vị trí giữa thì lấy luôn
        if a[mid] == min_even:
            return mid
        #còn không nếu bé hơn sẽ chỉ so sánh bên low còn lại thì sẽ là high
        elif a[mid] < min_even:
            low = mid+1
        else:
            high = mid - 1
    return -1

find = int(input("nhập số cần tìm của bạn : "))
result = binary_search(a,find)
print(f'số {find} được tìm thấy ở vị trí: {result}')

smallest_odd_num = min([num for num in a if num % 2 == 1])
print(f'số lẻ bé nhất trong dãy là: {smallest_odd_num}')
print(f'list trước khi xóa số lẻ bé nhất: {a}')
a.remove(smallest_odd_num)
print(f'list sau khi xóa số lẻ bé nhất: {a}')

value = int(input("Thêm 1 phần từ vào dãy: "))
index = int(input("Vị trí của phần tử ở dãy: "))
print(f'list trước khi thêm phần tử : {a}')
a.insert(index,value)
print(f'list sau khi thêm phần tử : {a}')




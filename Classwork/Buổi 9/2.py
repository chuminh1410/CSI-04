#Các thuật toán tìm kiếm: (tuyến tính, nhị phân)

#Tuần tự : Duyệt qua từng phần tử và so sánh giá trị cần tìm cho đến khi tìm thấy
def tim_tuyen_tinh(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Trả về i tức là vị trí đã tìm được 
    return -1  # Trả về -1 nếu không tìm thấy

# Ví dụ 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
result = tim_tuyen_tinh(arr, x)
print(f"Phần tử {x} được tìm thấy tại vị trí {result}.")


#Nhị phân : chỉ áp dụng cho dãy đã được sắp xếp. So sánh giá trị cần tìm với phần tử ở giữa dãy.Theo kết quả so sánh, tìm kiếm ở một nửa phù hợp của dãy.
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        #Nếu phần tử có tồn tại ở phần giữa của mảng
        if arr[mid] == x:
            return mid
        #Nếu phần tử nhỏ hơn mid, nó sẽ nằm ở phía bên trái của mảng gốc
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        #Nếu không, phần tử sẽ nằm bên phải
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        #Phần tử không tồn tại
        return -1

#Ví dụ:
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)
print(f"Phần tử {x} được tìm thấy tại vị trí {result}.")



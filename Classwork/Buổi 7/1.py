def bubble_sort(a):
    lenarr = len(a)

    # Đi qua từng phần tử trong list
    for i in range(lenarr):
        # So sánh dãy n[i] xong sẽ so sánh số n[i+1] cho đến hết độ dài của dãy n
        for j in range(0, lenarr-i-1):
            # Nếu số sau lớn hơn số trước, đổi chỗ cho nhau
            if a[j] > a[j+1]:
                # In ra thông báo về số đổi
                print(f"Swapping {a[j]} and {a[j+1]}")
                # Hoán đổi chỗ
                a[j], a[j+1] = a[j+1], a[j]

# Ví dụ
a=[1,5,4,7,0]

bubble_sort(a)

# In danh sách sắp xếp
print(a)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

#thuật toán này sẽ tìm phẩn tử bé nhất trong các lượt, lưu vào các vị trí từ 1 đến hết

my_list = [7,4,5,8]
selection_sort(my_list)
print(my_list)


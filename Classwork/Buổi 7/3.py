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


a = []

while True:
    b = int(input("Nhập số (nhập -1 để dừng): "))
    if b == -1:
        break
    a.append(b)


bubble_sort(a)

# In danh sách sắp xếp
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

even_num = [num for num in a if num % 2 == 0]
min_even = min(even_num)
result = binary_search(a,min_even)
print(f'số chẵn bé nhất được tìm thấy ở vị trí: {result}')
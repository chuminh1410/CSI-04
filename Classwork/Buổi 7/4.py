def bubble_sort(a):
    lenarr = len(a)

    # Đi qua từng phần tử trong list
    for i in range(lenarr):
        # So sánh dãy n[i] xong sẽ so sánh số n[i+1] cho đến hết độ dài của dãy n
        for j in range(0, lenarr-i-1):
            # Nếu số sau lớn hơn số trước, đổi chỗ cho nhau
            if a[j] < a[j+1]:
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

result = []

def tim_tuyen_tinh(a):
    for i in range(len(a)):
        if a[i] % 4 == 0 and a[i] >= 0:
            result.append(a[i])

    return result

result = tim_tuyen_tinh(a)
print(f"Số chia hết cho 4 và không âm được tìm ở vị trí (linear search): {result}")

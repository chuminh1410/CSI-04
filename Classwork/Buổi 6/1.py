def bubble_sort(a):
    lenarr = len(a)

    # Đi qua từng phần tử trong list
    for i in range(lenarr):
        # So sánh dãy n[i]
        for j in range(0, lenarr-i-1):
            # Nếu số sau lớn hơn số trước, đổi chỗ cho nhau
            if a[j] > a[j+1]:
                # In ra thông báo về số đổi
                print(f"Swapping {a[j]} and {a[j+1]}")
                # Hoán đổi chỗ
                a[j], a[j+1] = a[j+1], a[j]

# Ví dụ
a=[2,4,8,0]

bubble_sort(a)

# In danh sách sắp xếp
print(a)
# Arr có độ dài là 4
# 2,4,0,8
# 2,0,4,8
# 0,2,4,8


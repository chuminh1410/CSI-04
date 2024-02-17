a = []
while len(a) != 5 :
    b = int(input("Nhập 5 số nguyên: "))
    a.append(b)
print(f'Dãy gốc: {a}')

# tạo một mảng với độ dài 5 do người dùng nhập

# sử dụng bubble sort để sắp xếp theo thứ tự tăng dần

def bubble_sort(a):
    lenarr = len(a)
    for i in range(lenarr):
        for j in range(0, lenarr-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(f'dãy sau khi sắp xếp: {bubble_sort(a)}')

def tim_tuyen_tinh(a,x):
    for i in range(len(a)):
        if a[i]== x:
            return i
    return -1

x = 4
print(f'kết quả x ở vị trí : {tim_tuyen_tinh(a,x)}')
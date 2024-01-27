a=[4,12,5,8,70,6]
print(f'Mảng gốc {a}')
def find_smallest(a):
    smallest = 10000
    for i in range(len(a)):
        if a[i] < smallest:
            smallest = a[i]
    return smallest

print(f'Số bé nhất: {find_smallest(a)}')

def find_biggest(a):
    biggest = 0
    for i in range(len(a)):
        if a[i] > biggest:
            biggest = a[i]
    return biggest

print(f'Số lớn nhất: {find_biggest(a)}')

def bubble_sort(a):
    lenarr = len(a)
    for i in range(lenarr):
        for j in range(0, lenarr-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

bubble_sort(a)
print(f'Mảng sau sắp xếp: {a}')

def so_lon_k(a,k):
    if k <= len(a):
        return a[len(a)-k]
        
k = 2
print(f'Số lớn thứ {k} trong mảng là: {so_lon_k(a,k)}')

def add(a,place,item):
    return a[:place-1] + [item] + a[place-1:]

place = 4
item = 66
print(add(a,place,item))
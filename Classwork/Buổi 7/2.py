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

#a=[1,5,4,7,0]
#Lượt 1: so sánh 1 với 5 giữ nguyên, 5 với 4 thì đổi vị trí cho nhau [1,4,5,7,0], 5 so với 7 giữ nguyên, 7 so với 0 đổi vị trí [1,4,5,0,7]
#Lượt 2: so sánh 1 với 4 giữ nguyên, 4 với 5 giữ nguyên. 5 với 0 đổi vị trí [1,4,0,5,7], 0 với 5 giữ nguyên, 5 với 7 giữ nguyên
#Lượt 3: so sánh 1 với 4 giữ nguyên, 4 với 0 đổi vị trí [1,0,4,5,7], 4 với 5 giữ nguyên, 5 với 7 giữ nguyên
#Lượt 4: so sánh 1 với 0 đổi vị trí [0,1,4,5,7], 1 với 4 giữ nguyên, 4 với 5 giữ nguyên, 5 với 7 giữ nguyên
#sắp xếp đã hoàn thành

def binary_search(a,x):
    #gọi 2 phần chia đôi đó là low và high (thấp và cao)

    low = 0
    high = len(a)-1
    while low <= high:
        #chia đôi mảng cần tìm kiếm và vị trí ở giữa gọi là mid
        mid = ((low+high)//2)
        #nếu phần tử cần tìm ở vị trí giữa thì lấy luôn
        if a[mid] == x:
            return mid
        #còn không nếu bé hơn sẽ chỉ so sánh bên low còn lại thì sẽ là high
        elif a[mid] < x:
            low = mid+1
        else:
            high = mid - 1
    return -1
#a = [0, 1, 4, 5, 7]
#low = 0
#high = 4
#khi low < high:
#mid = low+high/2 = 2
#nếu vị trí cần tìm ở mid thì lấy luôn, còn không nếu bé hơn sẽ tìm từ 1 về low hoặc lớn hơn thì từ 3 đến hết high
#số cần tìm là 7
#vị trí 2 của array là 4, sẽ tìm bên lớn hơn
#so sánh với mid + 1 cho đến khi tìm đến 
#ngược lại nếu bé hơn thì so sánh với mid-1

def tim_tuyen_tinh(a,x):
    for i in range(len(a)):
        if a[i] ==x:
            return i
    return -1
#tìm tuyến tính sẽ so sánh từng phần tử trong dãy với số cần tìm

a=[1,5,4,7,0]
x = 7

result = tim_tuyen_tinh(a,x)
print(f"Số {x} được tìm ở vị trí (tuyến tính) : {result}")

#tìm nhị phân yêu cầu dãy phải được sắp xếp sẵn
bubble_sort(a)
print(a)
result = binary_search(a,x)
print(f"Số {x} được tìm ở vị trí (binary search) : {result}") 




#Các thuật toán sắp xếp: (nổi bọt, chèn, chọn, trộn)

#Nổi bọt: So sánh lần lượt các cặp phần tử liền kề và đổi chỗ chúng nếu chúng không theo thứ tự. nó sẽ lặp lại này cho đến khi mảng được sắp xếp.
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


#Chèn: Chèn phần tử mỗi lần vào đúng vị trí trong dãy đã sắp xếp.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # chọn phần tử hiện tại để so sánh và chèn vào đúng vị trí
        j = i - 1  # vị trí của phần tử trước phần tử hiện tại

        while j >= 0 and key < arr[j]:
            # di chuyển các phần tử lớn hơn key về phía sau để tạo chỗ trống cho key
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Chèn key vào vị trí đã tạo chỗ trống

a = [1, 4, 5, 12, 2, 45, 63, 102, 99, 87, 47, 65]
insertion_sort(a)
print(a)


#Chọn: Tìm phần tử nhỏ nhất trong dãy và đưa nó về đầu dãy. Lặp lại quá trình cho đến khi dãy được sắp xếp.
def selection_sort(arr):
    n = len(arr)  # độ dài của mảng
    for i in range(n):
        min_index = i  # vị trí phần tử nhỏ nhất ban đầu là i
        for j in range(i + 1, n):
            # Duyệt qua các phần tử còn lại từ i+1 đến n để tìm phần tử nhỏ nhất
            if arr[j] < arr[min_index]:
                min_index = j  # phần tử nhỏ nhất sẽ đổi

        # đổi chỗ giữa phần tử hiện tại với phần tử nhỏ nhất tìm được
        arr[i], arr[min_index] = arr[min_index], arr[i]

a = [7, 4, 5, 8]

selection_sort(a)
print(a)


#Trộn: Mảng được chia thành hai phần, sau đó các phần nhỏ được sắp xếp và trộn lại với nhau để tạo ra mảng đã sắp xếp.
def mergeSort(arr):
	if len(arr) > 1:

		# Vị trí giữa mảng
		mid = len(arr)//2

		# chia thành 2 nửa
		L = arr[:mid]
		R = arr[mid:]

		# sắp xếp mảng trái
		mergeSort(L)

		# sắp xếp mảng phải
		mergeSort(R)

		i = j = k = 0

		# cho 2 mảng vào mảng phụ 
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# check để xem còn phần tử nào thiếu 
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
arr = [12, 11, 13, 5, 6, 7]
selection_sort(arr)
print(arr)


#Nhanh: 
	


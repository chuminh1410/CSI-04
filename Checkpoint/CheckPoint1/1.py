def tinh_tong(n):
    if n == 1:
        return 1
    else:
        return n + tinh_tong(n-1)

n= 4
output = tinh_tong(n)
print("Tổng của các số là: " + str(output))
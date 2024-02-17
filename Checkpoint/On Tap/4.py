def tinh_tong(n):
    if n == 1 :
        return 1 
    else:
        return n + tinh_tong(n-1)
    
n = 5
print(f'Tổng các số từ 1 tới n là: {tinh_tong(n)}')
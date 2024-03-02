def giai_thua(n):
    # Điều kiện để dừng
    if n == 0 or n == 1:
        return 1
    else:
        # Cách tính đệ quy bằng cách gọi lại chính nó
        return n * giai_thua(n-1)

n = 5
result = giai_thua(n)

# In kết quả
print(f'Giai thừa của {n} là: {result}')

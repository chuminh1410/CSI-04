#Đệ quy (recursion) là một khái niệm trong lập trình mà một hàm có thể tự gọi lại chính nó để giải quyết một vấn đề. Đề bài tính giai
#thừa chúng ta có thể làm như sau:

def giai_thua(n):
    # Điều kiện để dừng
    if n == 0 or n == 1:
        return 1
    else:
        # Tính đệ quy bằng cách gọi lại hàm
        return n * giai_thua(n-1)

n = 5
result = giai_thua(n)

# In kết quả
print(f'Giai thừa của {n} là: {result}')

def giai_thua(n):
    if n == 1 or n == 0:
        #điều kiện bình thường của giai thừa khi 1,0 thì sẽ về 1
        return 1
    else:
        return n * giai_thua(n-1)
    # lấy n nhân với n trừ 1 đến khi n về bằng 0
n = 10
result = giai_thua(n)
print(result)

def fibo(n):
    if n <= 1:
        # nếu n <= 1 thì sẽ trả n
        return n
    else:
        # sẽ gọi đi gọi lại và cộng lại các số trước bởi vì mỗi số là tổng của 2 số liền trước
        return fibo(n-1) + fibo(n-2)

n = 10
print(fibo(n))

def prime(num):
    if num < 2 :
        return False
    # số dưới 2 không có nguyên tố
    for i in range(2,(num**0.5) + 1):
        print
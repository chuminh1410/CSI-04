def fibo(n):
    if n <= 1:
        # nếu n <= 1 thì sẽ trả n vì đó là điều kiện mặc định
        return n
    else:
        # sẽ gọi đi gọi lại và cộng lại các số trước bởi vì mỗi số là tổng của 2 số liền trước cho đến khi n = 1
        return fibo(n-1) + fibo(n-2)

n = 10
print(fibo(n))
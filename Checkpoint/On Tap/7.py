def fibo(n):
    if n <= 1:
        return n 
    else:
        return fibo(n-1) + fibo(n-2)
n = 5

print(f'số fibonacci thứ n là: {fibo(n)}')
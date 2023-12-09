def sum_num(num):
    str_num = str(num)
    total = 0
    for digit in str_num:
        total += int(digit)
    return total
print(sum_num(12345))
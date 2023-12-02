listnum = []
for x in range (10):
    temp = int(input(f"Enter number {x+1}: "))
    listnum.append(temp)
even_num = 0
odd_num = 0
div_4 = 0
prime = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(0,len(listnum)):
    if listnum[i]%2 == 0:
        even_num += listnum[i]
        count1 += 1
    else:
        odd_num += listnum[i]
        count2 += 1

    if listnum[i] % 4 == 0:
        div_4 += listnum[i]
        count3 += 1
    
    if is_prime(listnum[i]):
        prime += listnum[i]
        count4 += 1
        
avg_even = even_num / count1
avg_odd = odd_num / count2
avg_div_4 = div_4 / count3
avg_prime = prime / count4

print("Tổng số chắn:" , str(even_num))
print("Tổng số lẻ:" , str(odd_num))
print("Tổng số chia hết cho 4:" , str(div_4))
print("Tổng số nguyên tố:" , str(prime))
print("Trung bình số chẵn:" , str(avg_even))
print("Trung bình số lẻ:" , str(avg_odd))
print("Trung bình số chia hết cho 4:" , str(avg_div_4))
print("Trung bình số nguyên tố:" , str(avg_prime))


def tim_uoc_chung(a, b):
    if b == 0:
        return a
    else:
        return tim_uoc_chung(b, a%b)
    
so = 12
so1 = 48

result = tim_uoc_chung(so,so1)
print("Ước chung lớn nhất là: " + str(result))

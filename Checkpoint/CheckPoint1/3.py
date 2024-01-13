a=[1,2,5,7,15,22,41,55,65,73,82,91]
def tim_tuyen_tinh(a,x):
    for i in range(len(a)):
        if a[i] ==x:
            return i
    return -1

x = 73
result = tim_tuyen_tinh(a,x)
print("Kết quả x vị trí : " + str(result))
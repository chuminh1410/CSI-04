a = [2,4,6,7,9,11]
x = 7
def tim_kiem_nhi_phan(a,x):
    low = a[0]
    high = a[len(a)-1]
    mid = (low+high)/2
    if mid < x:
        mid = low 
        high = a[len(a)-1]


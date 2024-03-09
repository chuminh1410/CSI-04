def thap_ha_noi(n,start,end,middle):    #lấy 4 đầu vào n: số đĩa, start: cột đầu tiên,
    if n == 1:                          #middle: cột giữa, end: cột cuối
        print(f'Chuyển đĩa 1 từ {start} sang {end}')
        return  #nếu chỉ có 1 đĩa để di chuyển thì sẽ chuyển từ cột đầu sang cột cuối
    thap_ha_noi(n-1,start,middle,end)
    print(f'Chuyển đĩa {n} từ {start} sang {end}')
    thap_ha_noi(n-1,middle,end,start)
#nếu mà có trên 1 đĩa thì vòng lặp sẽ lặp lại mỗi lần với đĩa số n-1 từ cột đầu đến cột giữa
#xong đĩa số n-2 (n-1-1) từ cột giữa ra cột cuối
n = 4
thap_ha_noi(n,"A","C","B")
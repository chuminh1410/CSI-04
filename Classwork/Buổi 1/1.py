def nam_nhuan(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def ngay_thang(month,year):
    if month == 2 :
        return 29 if nam_nhuan(year) else 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31

input_date = input("Nhập ngày tháng năm: (dd/mm/yyyy): ")
day, month, year = [int(temp) for temp in input_date.split('/')]
day += 1
if day > ngay_thang(month,year):
    day = 1
    month += 1
if month > 12:
    month = 1
    year += 1

print(f"Ngày tiếp theo là: {day}/{month}/{year}")

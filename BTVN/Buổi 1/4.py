def day_in_week(day_int):
    if 2 <= day_int <= 8:
        days_of_week = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[day_int - 1] 
    else:
        return "Invalid input"

print(day_in_week(2))
print(day_in_week(8))

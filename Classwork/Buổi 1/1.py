from datetime import *

inp_date = input("Input: (dd/mm/yyyy): ")

next_date = (datetime.strptime(inp_date, '%d/%m/%Y') + timedelta(days=1)).strftime('%d/%m/%Y')

print("Next day is", next_date)

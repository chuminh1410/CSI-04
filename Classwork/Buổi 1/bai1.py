class MobilePhone:
    def __init__(self, name, OS, batt_capacity, status=bool):
        self.name = name
        self.OS = OS
        self.batt_capacity = batt_capacity
        self.status = status

    def on_status(self):
        self.status = True
        print(f"The status is: {self.status}")

    def off_status(self):
        self.status = False
        print(f"The status is: {self.status}")

    def check_batt(self):
        print(f"The remaining battery is {self.batt_capacity}")

my_phone = MobilePhone(name="MyPhone", OS="Android", batt_capacity=92)

print(my_phone.batt_capacity)
my_phone.check_batt()

my_phone.on_status()
my_phone.off_status()

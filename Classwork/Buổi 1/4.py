class nhan_vien:
    def __init__(self, ID, name, age, birth_date, work_date, hometown, salary=4.2):
        self.ID = ID
        self.name = name
        self.age = age
        self.birthdate = birth_date
        self.work_date = work_date
        self.hometown = hometown
        self.salary = salary

class  quan_ly(nhan_vien):
    def __init__(self, ID, name, age, birth_date, work_date, hometown, position = "quan ly", salary=5.0):
        super().__init__(ID, name, age, birth_date, work_date, hometown, salary)
        self.position = position

class  giam_doc(nhan_vien):
    def __init__(self, ID, name, age, birth_date, work_date, hometown, position = "giam doc", salary=7.0):
        super().__init__(ID, name, age, birth_date, work_date, hometown, salary)
        self.position = position
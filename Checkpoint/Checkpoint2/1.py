from datetime import date
class sinh_vien:
    def __init__(self, name, year_birth, adress, hometown, math, physic, chemistry):
        self.name = name
        self.year_birth = year_birth
        self.adress = adress
        self.hometown = hometown
        self.math = math
        self.physic = physic
        self.chemistry = chemistry
    def return_age(self):
        year_now = date.today().year
        tuoi = year_now - self.year_birth
        return tuoi
    def avg_score(self):
        avg_score = (self.math + self.physic + self.chemistry)/3
        return round(avg_score,1)
    def award(self):
        avg_score = self.avg_score()
        excellence = "Giỏi"
        merit = "Khá"
        good = "Trung Bình"
        low = "Yếu"
        if avg_score >= 8.0 and self.math > 6.5 and self.physic > 6.5 and self.chemistry > 6.5:
            return excellence
        elif avg_score >= 6.5 and self.math > 5.0 and self.physic > 5.0 and self.chemistry > 5.0:
            return merit
        elif avg_score >= 5.0 and self.math > 4.0 and self.physic > 4.0 and self.chemistry > 4.0:
            return good
        else:
            return low


ex1 = sinh_vien("Nguyen Van B",2007,"Ha Noi","Thai Binh",6,9,7)
age_now = ex1.return_age()
print(f'Tuổi hiện tại: {age_now}')
avg_scr = ex1.avg_score()
print(f'Điểm trung bình: {avg_scr}')
hoc_luc = ex1.award()
print(f'Học lục: {hoc_luc}')
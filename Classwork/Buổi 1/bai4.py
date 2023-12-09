class HocSinh():
    def __init__(self, name, math, literature):
        self.name = name
        self.math = math
        self.literature = literature
    
    def calculate_average(self):
        return (self.math + self.literature) / 2

    def avg_score(self):
        avg_sco = self.calculate_average()
        print(f"Student {self.name}'s average score: {avg_sco}")

    def determine_rank(self):
        avg_sco = self.calculate_average()
        if avg_sco >= 8:
            ranking = "Excellence"
        elif 6 <= avg_sco < 8:
            ranking = "Merit"
        else:
            ranking = "Good"
        return ranking

    def display_rank(self):
        ranking = self.determine_rank()
        print(f"Student {self.name}'s ranking is {ranking}")

# Tạo một đối tượng HocSinh
hoc_sinh_instance = HocSinh(name="Chu", math=2, literature=7)

# Hiển thị điểm trung bình và xếp loại của học sinh
hoc_sinh_instance.avg_score()
hoc_sinh_instance.display_rank()

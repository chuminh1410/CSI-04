class HocSinh():
    def __init__(self, name, math, literature):
        self.name = name
        self.math = math
        self.literature = literature
    
    def avg_score(self):
        avg_sco = (self.math + self.literature) / 2
        print(f"Student average score: {avg_sco}")

    def rank(self):
        avg_sco = (self.math + self.literature) / 2
        if avg_sco >= 8:
            ranking = "Excellence"
        elif 6 <= avg_sco < 8:
            ranking = "Merit"
        else:
            ranking = "Good"
        print(f"Student {self.name} ranking is {ranking}")

hoc_sinh_instance = HocSinh(name="Chu", math=2, literature=7)

hoc_sinh_instance.avg_score()
hoc_sinh_instance.rank()

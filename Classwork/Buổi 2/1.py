class Student:
    def __init__(self, ma_sv="", ho_ten="", tuoi=0, diem=0.0):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.diem = diem

    def nhap(self):
        self.ma_sv = input("Nhập mã sinh viên: ")
        self.ho_ten = input("Nhập họ tên sinh viên: ")
        self.tuoi = int(input("Nhập tuổi sinh viên: "))
        self.diem = float(input("Nhập điểm sinh viên: "))

    def xuat(self):
        return f"\nThông tin sinh viên:\nMã sinh viên: {self.ma_sv}\nHọ tên: {self.ho_ten}\nTuổi: {self.tuoi}\nĐiểm: {self.diem}"


def nhap_danh_sach():
    n = int(input("Nhập số lượng sinh viên: "))
    danh_sach = []

    for i in range(n):
        sinh_vien = Student()
        sinh_vien.nhap()
        danh_sach.append(sinh_vien)

    return danh_sach

def xuat_danh_sach(danh_sach):
    print("\nThông tin của tất cả sinh viên:")
    for i in range (0,len(danh_sach)):
        print(danh_sach[i].xuat())

danh_sach_sinh_vien = nhap_danh_sach()
xuat_danh_sach(danh_sach_sinh_vien)

class student:
    def __init__(self, name = "", ID="", age=0, avg_score=0.0, ):
        self.name = name
        self.ID = ID
        self.age = age 
        self.avg_score = avg_score
        
    def nhap(self):
        self.name = input("Nhập tên sinh viên: ")
        self.ID = input("Nhập mã sinh viên: ")
        self.age = int(input("Nhập tuổi sinh viên: "))
        self.avg_score = float(input("Nhập điểm trung bình sinh viên: "))

    def xuat(self):
        return f"\nThông tin sinh viên:\nMã sinh viên: {self.ID}\nHọ tên: {self.name}\nTuổi: {self.age}\nĐiểm: {self.avg_score}"


def nhap_danh_sach():
    n = int(input("Nhập số lượng sinh viên: "))
    danh_sach = []

    for i in range(n):
        sinh_vien = student()
        sinh_vien.nhap()
        danh_sach.append(sinh_vien)

    return danh_sach

def xuat_danh_sach(danh_sach):
    print("\nThông tin của tất cả sinh viên:")
    for i in range (0,len(danh_sach)):
        print(danh_sach[i].xuat())

danh_sach_sinh_vien = nhap_danh_sach()
xuat_danh_sach(danh_sach_sinh_vien)

def tim_kiem(self,search):
    result = [sinh_vien for sinh_vien in self.danh_sach if search in sinh_vien.name or search in sinh_vien.ID]
    return result

def sua_thong_tin(self.ID,ten_moi,tuoi_moi,diem_tb_moi):
    for sinh_vien in self.danh_sach:
        if sinh_vien.ID == ID:
            sinh_vien.name = ten_moi
            sinh_vien.age = tuoi_moi
            sinh_vien.avg_score = diem_moi
           
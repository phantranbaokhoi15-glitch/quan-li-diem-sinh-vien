import pandas as pd

# Tạo dữ liệu của 10 sinh viên
data = {
    "Họ và tên": [
        "Phan Trần Bảo Khôi",
        "Lương Minh Tuấn",
        "Nguyễn Quang Tiến",
        "Lê An Bảo Ngọc",
        "Nguyễn Hữu Chiến",
        "Đinh Thị Quỳnh Như",
        "Nguyễn Thị Phương Trâm",
        "Nguyễn Đình Quốc",
        "Dương Quốc Khang",
        "Nguyễn Anh Kiệt"
    ],
    "Điểm chuyên cần": [9, 8, 10, 10, 8, 9, 6, 10, 7, 9],
    "Điểm giữa kỳ": [8, 7, 9, 9, 7.5, 8.5, 5, 9, 6.5, 8],
    "Điểm cuối kỳ": [8.5, 7.5, 9, 8.5, 8, 9, 5.5, 9.5, 7, 8.5]
}
# Tạo DataFrame
df = pd.DataFrame(data)
# Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
)

# Xếp loại sinh viên dựa trên điểm tổng kết
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# Thêm cột Xep_loai vào DataFrame
df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hiển thị bảng dữ liệu
print(df.round(2))
# 1. Tính điểm tổng kết trung bình của lớp
diem_trung_binh = df["Tong_ket"].mean()
print("Điểm tổng kết trung bình của lớp:", round(diem_trung_binh, 2))

# 2. Tìm sinh viên có điểm tổng kết cao nhất
diem_cao_nhat = df["Tong_ket"].max()
sv_cao_nhat = df[df["Tong_ket"] == diem_cao_nhat]
print("\nSinh viên có điểm tổng kết cao nhất:")
print(sv_cao_nhat[["Họ và tên", "Tong_ket"]])

# 3. Tìm sinh viên có điểm tổng kết thấp nhất
diem_thap_nhat = df["Tong_ket"].min()
sv_thap_nhat = df[df["Tong_ket"] == diem_thap_nhat]
print("\nSinh viên có điểm tổng kết thấp nhất:")
print(sv_thap_nhat[["Họ và tên", "Tong_ket"]])

# 4. Đếm số sinh viên đạt (điểm tổng kết >= 5)
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()
print("\nSố sinh viên đạt:", so_sinh_vien_dat)
import matplotlib.pyplot as plt

# Dữ liệu 10 sinh viên và điểm tổng kết[cite: 1]
ten_sinh_vien = [
    "Phan Trần Bảo Khôi",
    "Lương Minh Tuấn",
    "Nguyễn Quang Tiến",
    "Lê An Bảo Ngọc",
    "Nguyễn Hữu Chiến",
    "Đinh Thị Quỳnh Như",
    "Nguyễn Thị Phương Trâm",
    "Nguyễn Đình Quốc",
    "Dương Quốc Khang",
    "Nguyễn Anh Kiệt"
]

diem_tong_ket = [
    8.45, 7.45, 9.20, 8.95, 7.85,
    8.85, 5.45, 9.45, 6.85, 8.45
]

# Kích thước khung hình
plt.figure(figsize=(10, 6))

# Vẽ biểu đồ cột nằm ngang (barh) giống như mẫu trong ảnh[cite: 2]
# Sử dụng reversed() để tên sinh viên đầu tiên xuất hiện ở trên cùng
plt.barh(list(reversed(ten_sinh_vien)), list(reversed(diem_tong_ket)), color="#5b9bd5")

# Thêm tiêu đề và nhãn trục[cite: 2]
plt.title("Biểu đồ điểm tổng kết của 10 sinh viên", fontsize=14, fontweight="bold")
plt.xlabel("Điểm tổng kết", fontsize=12)
plt.ylabel("Tên sinh viên", fontsize=12)

# Giới hạn trục x từ 0 đến 10[cite: 2]
plt.xlim(0, 10)

# Hiển thị lưới để dễ quan sát
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Căn chỉnh bố cục và hiển thị
plt.tight_layout()
plt.show()

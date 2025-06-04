import pandas as pd

# Tạo DataFrame
data = {
    "Name": ["Thanh", "Tu", "Vy", "Hoang", "Khanh", "Linh", "Trang", "Truc", "Phi", "Minh"],
    "Age": [21, 20, 22, 23, 20, 21, 19, 24, 20, 22],
    "Gender": ["Nữ", "Nam", "Nữ", "Nam", "Nữ", "Nữ", "Nữ", "Nữ", "Nam", "Nam"],
    "Score": [8.5, 6.0, 4.5, 7.0, 9.0, 5.0, 4.0, 9.5, 3.0, 6.5]
}

# chuyển dữ liệu kiểu từ điển thành bảng (DataFrame)
df_students = pd.DataFrame(data)

# Hiển thị toàn bộ dữ liệu
print("Toàn bộ dữ liệu:")
print(df_students)

# Hiển thị 3 dòng đầu
print("\n3 dòng đầu:")
print(df_students.head(3))

# Giá trị tại index=2 và cột Name
print("\nGiá trị tại index=2 và cột Name:")
print(df_students.at[2, 'Name'])

# Giá trị tại index=10 và cột Age (sẽ báo lỗi vì không có index=10)
print("\nGiá trị tại index=10 và cột Age:")
if 10 in df_students.index:
    print(df_students.at[10, 'Age'])
else:
    print("Không có index=10 trong DataFrame!")

# Hiển thị 2 cột Name và Score
print("\nCột Name và Score:")
print(df_students[["Name", "Score"]])

# Thêm cột Pass
df_students["Pass"] = df_students["Score"] >= 5
print("\nSau khi thêm cột Pass:")
print(df_students)

# Sắp xếp theo Score giảm dần
print("\nSắp xếp theo Score giảm dần:")

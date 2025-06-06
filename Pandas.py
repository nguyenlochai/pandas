import pandas as pd

# Dữ liệu sinh viên
student_data = {
    "Name": ["Thanh", "Tu", "Vy", "Hoang", "Khanh", "Linh", "Trang", "Truc", "Phi", "Minh"],
    "Age": [21, 20, 22, 23, 20, 21, 19, 24, 20, 22],
    "Gender": ["Nữ", "Nam", "Nữ", "Nam", "Nữ", "Nữ", "Nữ", "Nữ", "Nam", "Nam"],
    "Score": [8.5, 6.0, 4.5, 7.0, 9.0, 5.0, 4.0, 9.5, 3.0, 6.5]
}

# Tạo DataFrame từ dữ liệu
df_students = pd.DataFrame(student_data)

# Hiển thị toàn bộ dữ liệu
print("== Toàn bộ dữ liệu sinh viên ==")
print(df_students)

# Hiển thị 3 dòng đầu tiên
print("== 3 dòng đầu ==")
print(df_students.head(3))

# Lấy giá trị tại index = 2 và cột 'Name'
print("== Giá trị tại index = 2 và cột Name ==")
print(df_students.at[2, 'Name'])

# Kiểm tra và lấy giá trị tại index = 10 và cột 'Age'
print("== Giá trị tại index = 10 và cột Age ==")
if 10 in df_students.index:
    print(df_students.at[10, 'Age'])
else:
    print("Không tồn tại index = 10 trong DataFrame")

# Hiển thị 2 cột Name và Score
print("== Cột Name và Score ==")
print(df_students[['Name', 'Score']])

# Thêm cột 'Pass' dựa trên điều kiện Score >= 5
df_students['Pass'] = df_students['Score'] >= 5
print("== Sau khi thêm cột Pass ==")
print(df_students)

# Sắp xếp theo Score giảm dần
print("== Danh sách sắp xếp theo Score giảm dần ==")
df_sorted_by_score = df_students.sort_values(by='Score', ascending=False)
print(df_sorted_by_score)

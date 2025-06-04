import pandas as pd
import numpy as np

# Tạo bảng Nhân viên
df_nv = pd.DataFrame({
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    "Age": [25, np.nan, 30, 22, 28, 35],
    "Department": ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    "Salary": [700, 800, 750, np.nan, 710, 770]
})

# Tạo bảng Phòng ban
df_dept = pd.DataFrame({
    "Department": ['HR', 'IT', 'Finance', 'Marketing'],
    "Manager": ['Trang', 'Khoa', 'Minh', 'Lan']
})

# Hiển thị toàn bộ dữ liệu
print("== Toàn bộ dữ liệu bảng Nhân viên ==")
print(df_nv)

# 1. Kiểm tra ô dữ liệu bị thiếu
print("== Dữ liệu bị thiếu trong bảng Nhân viên ==")
print(df_nv.isnull())

# 2. Xoá dòng có hơn 2 ô bị thiếu
df_nv = df_nv[df_nv.isnull().sum(axis=1) <= 2]

# 3. Điền giá trị bị thiếu
df_nv['Name'] = df_nv['Name'].fillna('Chưa rõ')
df_nv['Age'] = df_nv['Age'].fillna(df_nv['Age'].mean())
df_nv['Salary'] = df_nv['Salary'].fillna(method='ffill')  # dùng giá trị trước đó
df_nv['Department'] = df_nv['Department'].fillna('Unknown')

# 4. Chuyển Age và Salary sang int
df_nv['Age'] = df_nv['Age'].astype(int)
df_nv['Salary'] = df_nv['Salary'].astype(int)

# 5. Tạo cột Salary_after_tax (giảm 10%)
df_nv['Salary_after_tax'] = df_nv['Salary'] * 0.9

# 6. Lọc nhân viên phòng IT có tuổi > 25
df_filtered = df_nv[(df_nv['Department'] == 'IT') & (df_nv['Age'] > 25)]
print("\n== Nhân viên IT có tuổi > 25 ==")
print(df_filtered)

# 7. Sắp xếp theo Salary_after_tax giảm dần
df_sorted = df_nv.sort_values(by='Salary_after_tax', ascending=False)
print("\n== Danh sách nhân viên theo lương sau thuế giảm dần ==")
print(df_sorted)

# 8. Nhóm theo Department và tính lương trung bình
df_avg_salary = df_nv.groupby('Department')['Salary'].mean().reset_index()
print("\n== Lương trung bình theo phòng ban ==")
print(df_avg_salary)

# 9. Dùng merge() nối với bảng Phòng ban để có Manager
df_merged = pd.merge(df_nv, df_dept, on='Department', how='left')
print("\n== Nhân viên sau khi thêm cột Manager ==")
print(df_merged)

# 10. Thêm 2 nhân viên mới và nối bằng concat()
new_employees = pd.DataFrame({
    "ID": [107, 108],
    "Name": ['Tú', 'Mai'],
    "Age": [29, 27],
    "Department": ['Marketing', 'Finance'],
    "Salary": [780, 760]
})
new_employees['Salary_after_tax'] = new_employees['Salary'] * 0.9

# Nối bảng
df_final = pd.concat([df_nv, new_employees], ignore_index=True)
print("\n== Bảng nhân viên sau khi thêm nhân viên mới ==")
print(df_final)

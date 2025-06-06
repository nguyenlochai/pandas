import pandas as pd
import numpy as np

# Tạo bảng nhân viên
df_employees = pd.DataFrame({
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    "Age": [25, np.nan, 30, 22, 28, 35],
    "Department": ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    "Salary": [700, 800, 750, np.nan, 710, 770]
})

# Tạo bảng phòng ban
df_departments = pd.DataFrame({
    "Department": ['HR', 'IT', 'Finance', 'Marketing'],
    "Manager": ['Trang', 'Khoa', 'Minh', 'Lan']
})

# Hiển thị dữ liệu bảng nhân viên
print("== Toàn bộ dữ liệu bảng Nhân viên ==")
print(df_employees)

# 1. Kiểm tra các ô bị thiếu
print("== Dữ liệu bị thiếu trong bảng Nhân viên ==")
print(df_employees.isnull())

# 2. Xoá dòng có hơn 2 ô bị thiếu
df_employees = df_employees[df_employees.isnull().sum(axis=1) <= 2]

# 3. Điền giá trị bị thiếu
df_employees['Name'] = df_employees['Name'].fillna('Chưa rõ')
df_employees['Age'] = df_employees['Age'].fillna(df_employees['Age'].mean())
df_employees['Salary'] = df_employees['Salary'].fillna(method='ffill')
df_employees['Department'] = df_employees['Department'].fillna('Unknown')

# 4. Chuyển Age và Salary sang kiểu int
df_employees['Age'] = df_employees['Age'].astype(int)
df_employees['Salary'] = df_employees['Salary'].astype(int)

# 5. Tạo cột lương sau thuế (giảm 10%)
df_employees['SalaryAfterTax'] = df_employees['Salary'] * 0.9

# 6. Lọc nhân viên phòng IT có tuổi > 25
df_it_over_25 = df_employees[(df_employees['Department'] == 'IT') & (df_employees['Age'] > 25)]
print("== Nhân viên IT có tuổi > 25 ==")
print(df_it_over_25)

# 7. Sắp xếp theo lương sau thuế giảm dần
df_sorted_salary = df_employees.sort_values(by='SalaryAfterTax', ascending=False)
print("== Danh sách nhân viên theo lương sau thuế giảm dần ==")
print(df_sorted_salary)

# 8. Tính lương trung bình theo phòng ban
df_avg_salary_by_dept = df_employees.groupby('Department')['Salary'].mean().reset_index()
print("== Lương trung bình theo phòng ban ==")
print(df_avg_salary_by_dept)

# 9. Nối với bảng phòng ban để thêm cột Manager
df_with_manager = pd.merge(df_employees, df_departments, on='Department', how='left')
print("== Nhân viên sau khi thêm cột Manager ==")
print(df_with_manager)

# 10. Thêm nhân viên mới
df_new_employees = pd.DataFrame({
    "ID": [107, 108],
    "Name": ['Tú', 'Mai'],
    "Age": [29, 27],
    "Department": ['Marketing', 'Finance'],
    "Salary": [780, 760]
})
df_new_employees['SalaryAfterTax'] = df_new_employees['Salary'] * 0.9

# Nối bảng nhân viên với nhân viên mới
df_final_employees = pd.concat([df_employees, df_new_employees], ignore_index=True)
print("== Bảng nhân viên sau khi thêm nhân viên mới ==")
print(df_final_employees)

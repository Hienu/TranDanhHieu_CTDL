# Ví dụ với đối tượng, sắp xếp theo thuộc tính tên
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [Employee("Alice", 50000), Employee("Bob", 60000), Employee("Alice", 55000)]
sorted_employees = sorted(employees, key=lambda x: x.name)
print("Danh sách nhân viên chưa sắp xếp:", [e.name for e in employees])
print("Danh sách nhân viên đã sắp xếp theo tên:", [e.name for e in sorted_employees])

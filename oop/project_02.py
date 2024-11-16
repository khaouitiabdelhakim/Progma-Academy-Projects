# Code By: ABDELHAKIM KHAOUITI
# Date: 12 08 2024
# Place: Rabat
# Org: Progma.ma


class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id  # رقم الموظف
        self.name = name  # اسم الموظف
        self.position = position  # الوظيفة ديال الموظف
        self.salary = salary  # الأجر ديال الموظف

    def display_info(self):
        # عرض المعلومات ديال الموظف
        print(f"رقم الموظف: {self.emp_id}, الاسم: {self.name}, الوظيفة: {self.position}, الأجر: {self.salary} درهم")


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name  # اسم القسم
        self.employees = []  # لائحة الموظفين فالقسم

    def add_employee(self, employee):
        # إضافة الموظف للقسم
        self.employees.append(employee)
        print(f"تمت إضافة {employee.name} لقسم {self.dept_name}")

    def remove_employee(self, emp_id):
        # حذف الموظف من القسم
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"تمت إزالة {employee.name} من قسم {self.dept_name}")
                return
        print(f"ماكاينش الموظف برقم {emp_id} فالقسم {self.dept_name}")

    def display_employees(self):
        # عرض جميع الموظفين فالقسم
        print(f"الموظفين فالقسم {self.dept_name}:")
        for employee in self.employees:
            employee.display_info()


# مثال للاستخدام:
# إنشاء بعض الموظفين
emp1 = Employee(1, "أحمد", "مدير", 15000)
emp2 = Employee(2, "فاطمة", "محاسبة", 9000)
emp3 = Employee(3, "خالد", "مبرمج", 12000)

# إنشاء قسم
dept = Department("تكنولوجيا المعلومات")

# إضافة الموظفين للقسم
dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(emp3)

# عرض جميع الموظفين فالقسم
dept.display_employees()

# حذف موظف
dept.remove_employee(2)

# عرض الموظفين مرة أخرى بعد الحذف
dept.display_employees()




"""
تمت إضافة أحمد لقسم تكنولوجيا المعلومات
تمت إضافة فاطمة لقسم تكنولوجيا المعلومات
تمت إضافة خالد لقسم تكنولوجيا المعلومات
الموظفين فالقسم تكنولوجيا المعلومات:
رقم الموظف: 1, الاسم: أحمد, الوظيفة: مدير, الأجر: 15000 درهم
رقم الموظف: 2, الاسم: فاطمة, الوظيفة: محاسبة, الأجر: 9000 درهم
رقم الموظف: 3, الاسم: خالد, الوظيفة: مبرمج, الأجر: 12000 درهم
تمت إزالة فاطمة من قسم تكنولوجيا المعلومات
الموظفين فالقسم تكنولوجيا المعلومات:
رقم الموظف: 1, الاسم: أحمد, الوظيفة: مدير, الأجر: 15000 درهم
رقم الموظف: 3, الاسم: خالد, الوظيفة: مبرمج, الأجر: 12000 درهم

"""
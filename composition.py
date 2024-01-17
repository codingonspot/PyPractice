class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_sal = Salary(pay, bonus)

    def total_salary(self):
        return self.obj_sal.annual_salary()


emp = Employee('Ishan', 24, 45000, 10000)
print(emp.total_salary())

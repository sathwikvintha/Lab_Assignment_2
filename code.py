class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeDatabase:
    def __init__(self, employees):
        self.employees = employees

    def display_employees(self):
        for emp in self.employees:
            print(emp)

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting option")

    def get_user_input(self):
        try:
            key = int(input("Enter sorting option (1. Age, 2. Name, 3. Salary): "))
            self.sort_employees(key)
            print("\nSorted Employees:")
            self.display_employees()
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Creating Employee objects
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

# Creating EmployeeDatabase object
employee_database = EmployeeDatabase([employee1, employee2, employee3, employee4])

# Getting user input for sorting and displaying the result
employee_database.get_user_input()

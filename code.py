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

    def sort_employees(self, key, order):
        if key == 1:
            self.employees.sort(key=lambda x: x.age, reverse=(order == 'desc'))
        elif key == 2:
            self.employees.sort(key=lambda x: x.name, reverse=(order == 'desc'))
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary, reverse=(order == 'desc'))
        else:
            print("Invalid sorting option")

    def get_user_input(self):
        try:
            key = int(input("Enter sorting option (1. Age, 2. Name, 3. Salary): "))
            order = input("Enter sorting order (asc or desc): ").lower()
            self.sort_employees(key, order)
            print("\nSorted Employees:")
            self.display_employees()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def add_employee(self, emp_id, name, age, salary):
        new_employee = Employee(emp_id, name, age, salary)
        self.employees.append(new_employee)
        print(f"\nEmployee {name} added successfully!")

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"\nEmployee {emp.name} removed successfully!")
                return
        print(f"\nEmployee with ID {emp_id} not found.")

    def update_employee_salary(self, emp_id, new_salary):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.salary = new_salary
                print(f"\nSalary updated successfully for {emp.name}. New salary: {new_salary}")
                return
        print(f"\nEmployee with ID {emp_id} not found.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for emp in self.employees:
                file.write(f"{emp.emp_id} {emp.name} {emp.age} {emp.salary}\n")
        print(f"\nEmployee data saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.split()
                    emp_id, name, age, salary = data[0], data[1], int(data[2]), int(data[3])
                    self.add_employee(emp_id, name, age, salary)
            print(f"\nEmployee data loaded from {filename}.")
        except FileNotFoundError:
            print(f"\nFile {filename} not found.")

# Creating Employee objects
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

# Creating EmployeeDatabase object
employee_database = EmployeeDatabase([employee1, employee2, employee3, employee4])

# Getting user input for sorting and displaying the result
employee_database.get_user_input()



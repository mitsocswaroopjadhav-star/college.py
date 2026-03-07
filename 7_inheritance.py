class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person_details(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
        def __init__(self,name,age,salary,employee_id):
            super().__init__(name,age)
            self.salary = salary
            self.employee_id = employee_id

        def display_employee_details(self):
            super().display_person_details()
            print(f"Salary: {self.salary}")
            print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
     def __init__(self,name,age,salary,employee_id,department):
        super().__init__(name,age,salary,employee_id)
        self.department = department

     def display_manager_details(self):
        super().display_employee_details()
        print(f"Department: {self.department}")

if __name__ == "__main__":
    while True:
        print("\n Choose an Option: \n 1. Person \n 2. Employee \n 3.Manager \n 4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            person = Person(name,age)
            person.display_person_details() 

        elif choice == '2':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            employee_id = input("Enter employee ID: ")
            employee = Employee(name,age,salary,employee_id)
            employee.display_employee_details()

        elif choice == '3':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            employee_id = input("Enter employee ID: ")
            department = input("Enter department: ")
            manager = Manager(name,age,salary,employee_id,department)
            manager.display_manager_details()

        else:
            break

    print("Exiting the program. Goodbye!")
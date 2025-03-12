import os

FILE_NAME = "employees.txt"

def add_employee():
    """Adds a new employee record to employees.txt"""
    with open(FILE_NAME, "a") as file:
        emp_id = input("Enter Employee ID: ").strip()
        name = input("Enter Employee Name: ").strip()
        position = input("Enter Employee Position: ").strip()
        salary = input("Enter Employee Salary: ").strip()

        if not emp_id or not name or not position or not salary:
            print("All fields are required. Please try again.")
            return
        
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    
    print("Employee record added successfully.\n")

def view_employees():
    """Displays all employee records"""
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return
    
    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        
        if not records:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for record in records:
                print(record.strip())
            print()

def search_employee():
    """Search for an employee by ID"""
    emp_id = input("Enter Employee ID to search: ").strip()
    
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("\nEmployee Found:")
                print(line.strip())
                found = True
                break

    if not found:
        print("Employee not found.")

def update_employee():
    """Update an employee’s information"""
    emp_id = input("Enter Employee ID to update: ").strip()

    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    updated_lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("\nCurrent Record:", line.strip())

                name = input("Enter new name (leave blank to keep unchanged): ").strip()
                position = input("Enter new position (leave blank to keep unchanged): ").strip()
                salary = input("Enter new salary (leave blank to keep unchanged): ").strip()

                data = line.strip().split(", ")
                if name:
                    data[1] = name
                if position:
                    data[2] = position
                if salary:
                    data[3] = salary

                updated_lines.append(", ".join(data) + "\n")
                found = True
            else:
                updated_lines.append(line)

    if not found:
        print("Employee not found.")
        return

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)

    print("Employee record updated successfully.")

def delete_employee():
    """Delete an employee record by ID"""
    emp_id = input("Enter Employee ID to delete: ").strip()

    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    updated_lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                found = True
                print("\nDeleting:", line.strip())
            else:
                updated_lines.append(line)

    if not found:
        print("Employee not found.")
        return

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)

    print("Employee record deleted successfully.")

def main():
    """Main menu for managing employee records"""
    while True:
        print("\nEmployee Records Manager")
        print("1. Add Employee Record")
        print("2. View Employee Records")
        print("3. Search Employee by ID")
        print("4. Update Employee Information")
        print("5. Delete Employee Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
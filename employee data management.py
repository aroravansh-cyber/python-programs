employees = {}
#to make infinite loop so user is able to enter employee acc to his/her need
while True:
    print("\n1. Add Employee")
    print("2. View Specific Employee")
    print("3. View All Employees")
    print("4. Edit Employee")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    # condition to add specific employee
    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        employees[emp_id] = {"name": name, "salary": salary}
        print("Added!")
    # to view specific employee
    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print(f"ID: {emp_id}, Name: {employees[emp_id]['name']}, Salary: {employees[emp_id]['salary']}")
        else:
            print("Not found!")
    #view all employee 
    elif choice == "3":
        for emp_id, emp in employees.items():
            print(f"ID: {emp_id}, Name: {emp['name']}, Salary: {emp['salary']}")
    #edit employee
    elif choice == "4":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            name = input("Enter new name: ")
            salary = input("Enter new salary: ")
            employees[emp_id] = {"name": name, "salary": salary}
            print("Updated!")
        else:
            print("Not found!")
    #exit
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")
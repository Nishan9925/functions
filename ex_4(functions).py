# Create a function show_employee () in such a way that it should accept employee name,
# and its salary and display both.If the salary is missing in the function call assign default value 9000 to salary

def show_employee(name, salary=9000):
    print("This is employees salary data")
    print(name, salary)


show_employee("Nshan")

# Create a function show_whole_employee_info () that will call in it two functions from the last two exercises.
def show_employee_basic_data(name, age):
    print("This employees basic data")
    print(name, age)

def show_employee(name, salary=9000):
    print("This is employees salary data")
    print(name, salary)




def show_whole_employee_info(name):
    show_employee_basic_data(name, 21)
    show_employee(name)


show_whole_employee_info("Nshan")

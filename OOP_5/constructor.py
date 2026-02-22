class employee():
    emp_name = "john"
    emp_department = "IT"
    company = "ABC"

# default constructor
    def __init__(self):
        print("Constructor is called")

    def __init__(self, name, department, company):
        self.emp_name = name
        self.emp_department = department
        self.company = company    

# Methods
    def info(self):
        print("Employee name is ", self.emp_name)
        print("Employee department is ", self.emp_department)
        print("Company is ", self.company)


# obj of the class
emp_1 = employee("Alice", "HR", "XYZ")



# copy constructor
class employee():
    emp_name = "john"
    emp_department = "IT"
    company = "ABC"

    def __init__(self, name, department, company):
        self.emp_name = name
        self.emp_department = department
        self.company = company

    def info(self):
        print("Employee name is ", self.emp_name)
        print("Employee department is ", self.emp_department)
        print("Company is ", self.company)
    
    
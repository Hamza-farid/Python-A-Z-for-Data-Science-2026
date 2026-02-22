

class employee():
    emp_name = "john"
    emp_department = "IT"
    company = "ABC"
# getter
    
    def info(self):
        print("Employee name is ", self.emp_name)
        print("Employee department is ", self.emp_department)
        print("Company is ", self.company)
# setter
    def change_info(self, name, department, company):
        self.emp_name = name
        self.emp_department = department
        self.company = company

emp_1 = employee()
emp_1.emp_name = "Alice"
emp_1.emp_department = "HR"

emp_2 = employee()
emp_2.info()
emp_2.change_info("Bob", "Finance", "XYZ")
emp_2.info()



# @property and func_name.setter 



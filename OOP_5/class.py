class employee():
# Attributes
    emp_name = "john"
    emp_department = "IT"

# Methods
    def info(self):
        print("Employee name is ", self.emp_name)
        print("Employee department is ", self.emp_department)


# obj of the class
emp_1 = employee()
print(emp_1.emp_name)

emp_1.info()
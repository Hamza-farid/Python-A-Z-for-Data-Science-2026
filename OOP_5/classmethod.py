class employee():
    company_name='abc'


    def changes(self, name):
        self.company_name = name


    @classmethod
    def class_method(cls, name):
        cls.company_name = name


emp_1 = employee()
        
emp_1.changes('xyz')
print(emp_1.company_name)





class Employee:
  emp_comp = "Amazon"
  emp_age = 20

  def defaultMethod(self):
    print("This is a default method")
    
e = Employee()
e1 = Employee()

print(getattr(e, 'emp_age')) 
print(hasattr(e, 'emp_comp'))      
print(hasattr(e1, 'emp_comp'))      
delattr(Employee, 'emp_comp')    
print(hasattr(e, 'emp_comp'))      
print(hasattr(e1, 'emp_comp'))      

print(hasattr(e, 'emp_age'))      
print(hasattr(e1, 'emp_age'))      
del Employee.emp_age          
print(hasattr(e, 'emp_age'))      
print(hasattr(e1, 'emp_age'))  







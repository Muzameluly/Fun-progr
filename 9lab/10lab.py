
import math
a = int(input('введи коэфициент a:'))
b = int(input('введи коэфициент b:'))
c = int(input('введи коэфициент с:'))

D = (math.pow(b,2) - 4 * a * c)
if D<0:
   print (" D>=0 ")
 
elif D==0:
   print (-b/(2*a))
else:
   x1 = (-b + math.sqrt(D))/(2*a)
   x2 = (-b - math.sqrt(D))/(2*a)
   print (x1, x2)



def maximum(arr): 
    max = arr[0]
    for ele in arr:
        if ele > max:
           max = ele
    return max 


list1 = [1.45,4.21,5,2,6.123]
result = maximum(list1)
print(round(result))


def fill_list(m1, m2, amount, l):
    from random import randint
    for i in range(amount):
        l.append(randint(m1, m2))
 
 
def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
 
 
lst = []
dct = {}
 
mn = int(input('Минимум: '))
mx = int(input('Максимум: '))
qty = int(input('Количество элементов: '))
 
fill_list(mn, mx, qty, lst)
analysis(lst, dct)
 
for item in sorted(dct):
    print("'%d':%d" % (item, dct[item]))



#Super
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

# Если создать дочерний класс `Laptop`, то будет доступ 
# к свойству базового класса благодаря функции super().
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model


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


lenovo = Laptop('lenovo', 2, 512, 'l420')

print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)
# Вывод
# This computer is: lenovo
# This computer has ram of 2
# This computer has ssd of 512
# This computer has this model: l420

#Open,close
my_file = open("some.txt")
print ("Имя файла: ", my_file.name)
print ("Файл закрыт: ", my_file.closed)
my_file.close()
print ("А теперь закрыт: ", my_file.closed)

#Next
marks = [65, 71, 68, 74, 61]

# convert list to iterator
iterator_marks = iter(marks)

# the next element is the first element
marks_1 = next(iterator_marks)
print(marks_1)

# find the next element which is the second element
marks_2 = next(iterator_marks)
print(marks_2)

#Write append
# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
file1.writelines(L)
file1.close()
  
# Append-adds at last
file1 = open("myfile.txt","a")#append mode
file1.write("Today \n")
file1.close()
  
file1 = open("myfile.txt","r")
print("Output of Readlines after appending") 
print(file1.readlines())
print()
file1.close()
  
# Write-Overwrites
file1 = open("myfile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()
  
file1 = open("myfile.txt","r")
print("Output of Readlines after writing") 
print(file1.readlines())
print()
file1.close()

#Sorted
numbers = [4, 2, 12, 8]

sorted_numbers = sorted(numbers)
print(sorted_numbers)

#max min
a = [11,8,12,0] 
print(min(a)) 
print(max(a)) 



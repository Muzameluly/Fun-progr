'''
#нефункциональное функция
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(cap_count)
'''
'''
#функциональное функция
from functools import reduce

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = reduce(lambda a, x: a + x.count('капитан'),
                   sentences,0)

print(cap_count)
'''


'''
def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
 
 
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
 
 
operation = select_operation(1)     # operation = sum
print(operation(10, 6))             # 16
 
operation = select_operation(2)     # operation = subtract
print(operation(10, 6))    
'''
'''

def showInfo(**students):
    print("\nType arguments:",type(students))

    for key, value in students.items():
        print("{} is {}".format(key,value))

showInfo(Firstname="Raiymbek", Lastname="Muzameluly", Age=21, Phone=87784778225)
showInfo(Firstname="Ernar", Lastname="Mazhenov", Email="e.mazhenov@gmail.com", Country="Taldykorgan", Age=20, Phone=87078329322)
'''
'''

def printScores(students, *scores):
   print(f"Student Name: {students}")
   for score in scores:
      print(score)
printScores("Raiymbek",100, 95, 88, 92, 99)
printScores("Ernar",100, 85, 90, 92, 100)
'''

'''

from functools import reduce

# filter
def f(x): 
	return x % 5 == 0
print(list(filter(f, range(2, 25))))

# map
def f(x):
	return x + 2
print(list(map(f, range(1, 11))))

# reduce
def add(x,y):
	return x + y
print(reduce(add, range(1, 11)))
'''




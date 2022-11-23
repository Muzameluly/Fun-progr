'''
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
'''

'''
def maximum(arr): 
    max = arr[0]
    for ele in arr:
        if ele > max:
           max = ele
    return max 


list1 = [1.45,4.21,5,2,6.123]
result = maximum(list1)
print(round(result))
'''

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



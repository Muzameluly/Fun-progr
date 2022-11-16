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
<<<<<<< HEAD

#Raiymbek
#Asylbek
=======
 #ERnar
>>>>>>> 339b2f9ece6b8774831c8e7a429f4fc47c351024

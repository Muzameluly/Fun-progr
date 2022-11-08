def season(m):
    if m==12 or m<3:
        return "Зима"
    if m>2 and m<6:
        return "Весна"
    if m>5 and m<9:
        return "Лето"
    if m>8 and m<12:
        return "Осень"

m=int(input("Введите номер месяц: "))
print(season(m))
print('=== Електронний журнал ===')
Stud=[
    {"name": 'Ігор',
    "login": 'Wonderful',
    "password": '100%misses',
    "grades": [1, 3, 3, 5, 7]},
    {"name": 'Павук',
     "login": 'BabiVnuk',
     "password": '3000elodota2',
     "grades": [5, 8, 2, 6, 7] },
    {"name": 'ПапаЄті',
     "login": 'TeammatePavuk',
     "password": '>3000elodota2',
     "grades": [9, 8, 4, 8, 10]},
    {"name": 'Лунтік',
     "login": 'Top1Faceit',
     "password": '6666',
     "grades": [9, 9, 8, 10, 12]}
]
found= False
print('Щоб увійти:')
login=input("Введіть ваш логін - ")
password=input("Введіть ваш Пароль - ")
for student in Stud:
    if student['login'] == login and student['password'] == password:
        print("Все гаразд,")
        print("Ваші оцінки:", student['grades'])

        good = 0
        bad = 0

        for grade in student['grades']:
            if grade >= 5:
                good += 1
            else:
                bad += 1
        print("Good Оцінки:", good)
        print("Bad Оцінки:", bad)
        found= True
        break
if found == False:
        print("Неправильно введений логін чи пароль")
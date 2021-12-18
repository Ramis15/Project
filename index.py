from dataset import users, countries

users_wrong_password = []
girls_drivers = []
best_occupation = {}
maxim = 0 #Переменная что бы вычислить максимальную зарплату.
max_summ_salary = 0
sum_salary = 0
vip_user = ''
Car_frend = 0 
car_srednee = 0
for_del = []
for user in users:
    # Плохие пароли начало блока
    try: 
        int(user['password'])
        users_wrong_password.append({'name': user['name'], 'mail':user['mail']})
    except Exception as e:
        pass
    # Плохие пароли начало блока

    try:
        for fendy in user['friends']:
            #Женщины водители начало блока
            try:
                fendy['cars']
                Car_frend += 1
                if fendy['sex'] == 'F':
                    girls_drivers.append(fendy['name']) 
                for travel in fendy['flights']:
                    car_srednee += 1
                   
            except Exception as e:
                pass
            #Женщины водители конец блока
            #Лучшая профессия начало блока
            if fendy['job']['salary'] > maxim:
                maxim = fendy['job']['salary']
                best_occupation = dict(fendy['job'])

            #Лучшая профессия начало блока
            #Самый влиятельный пользователь начало блока
            sum_salary += fendy['job']['salary']

        if sum_salary > max_summ_salary:
            max_summ_salary = sum_salary
            vip_user = user['name']
        sum_salary = 0

    except Exception as e:
        pass
                          
avg_flights = round(car_srednee / Car_frend, 5)


# задание 1
def f_to_c(f_temp):
    c_temp = ( f_temp - 32 ) * (5/9)
    return c_temp


f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) +  32
    return f_temp


c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# задание 2

def get_force(m,a):
    return m*a


train_mass = 5
train_acceleration = 25
train_force = get_force(train_mass,train_acceleration)

print(f'Поезд GE поставляет {train_force} ньютонов силы')

def get_energy(m, c = 3*10**8):
    return m*c**2

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print(f'1 кг бомбы составляет {bomb_energy} Джоулей')

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance


train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)

print(f'Поезд выполняет {train_work} Джоулей за {train_distance} метров.')

# задание 3 

def clothes_routine(clothes):
    print("У меня большой гардероб")
    print(f"Утром лучше всего подходит {clothes}")
    print(f"Днём лучше всего подходит {clothes}")
    print(f"Вечером лучше всего подходит {clothes}")
    print(f"Ночью лучше всего подходит {clothes}")


clothes = "домашняя одежда"

clothes_routine(clothes)


def meal_routine(meal):
    print("Мои предпочтения в еде")
    print(f"На завтрак я предпочитаю {meal}")
    print(f"На обед я предпочитаю {meal}")
    print(f"На ужин я предпочитаю {meal}")


meal = "стейк"

meal_routine(meal)

# задание 4

user = input('Введите имя пользователя: ')
arm_1 = int(input('Введите номер АРМ: '))
Dmitriy_check = """Дмитрий, твое рабочее место находится в другой комнате. 
Отойди от чужого компьютера и займись работой!"""
wellcome = 'Добро пожаловать'

def user_name_check(user_name):
    if user_name == 'Дмитрий': print(Dmitriy_check)
    else: print(wellcome)

user_name_check('Дмитрий')
user_name_check('Ангелина')

#господи это мучение 
users = ['Дмитрий', 'Ангелина','Василий','Екатерина']
arms = [1,2,3,4]
def arm_check (user_name,arm):
    for i in range(len(users)):
        if users[i] == user_name:
            if arms[i] == arm: 
                print(wellcome)
                break
            else:
                if user_name == 'Дмитрий': 
                    print(Dmitriy_check)
                    break
                else:
                    print("""Логин или пароль не верный, попробуйте еще раз""")
                    break
        else:
            print("""Логин или пароль не верный, попробуйте еще раз""")
            break
        
arm_check(user,arm_1)

# задание 5 я так и не понял, надо ли изначально делать через элиф а потом функцию, или сразу функцию. в общем я думаю спрошу у вас.

def grading(grade):
    if grade >= 4.0: return "A"
    elif grade >= 3.0: return "B"
    elif grade >= 2.0: return "C"
    elif grade >= 1.0: return "D"
    elif grade >= 0: return "F"
    else: return "ошибка"


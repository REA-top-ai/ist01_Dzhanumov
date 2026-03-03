# задание 1
print("задание 1\n")

print("TRUE" if (6 * 6) - 1 == 8 + 1 else "FALSE")
print("TRUE" if 13 - 7 != (3 * 2) + 1 else "FALSE")
print("TRUE" if 3 * (2 - 1) == 4 - 1 else "FALSE")
#вывод
# FALSE
# TRUE
# TRUE

print(" ")
# задание 2 (я использовал тернарный оператор, так чуть удобнее)
print("задание 2\n")

print("TRUE" if (6 * 6) - 1 >= 8 + 1 else "FALSE")
print("TRUE" if 13 - 7 <= (3 * 2) + 1 else "FALSE")
print("TRUE" if 3 * (2 - 1) > 4 - 1 else "FALSE")
#вывод
# TRUE
# TRUE
# FALSE
print(' ')
# задание 3
print("задание 3\n")

#bool_variable = true # NameError: name 'true' is not defined. Did you mean: 'True'?
#(больно писать тру с маленькой буквы...) Ответ на вопрос: какая ошибка ? nameError. Почему? строч буква.

#print(bool_variable)

bool_variable = 'true'
print(type(bool_variable)) #<class 'str'>

bool_variable_2 = True
print(type(bool_variable_2))#<class 'bool'>

print('')
# задание 4
print("задание 4")

user_name = input('введите имя\n')
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
wellcome = "Добро пожаловать"
if user_name != "Дмитрий":
    print(wellcome)
else:
    print(Dmitriy_check)

#кажется не хватает ТЗ, сам допридумаю условный пароль 1122
true_password = "1122"
enter_number = 0
user_password = (input('Введите пароль.\n'))
if user_password != true_password:
    enter_number += 1
    print(f"Попробуйе еще раз. У вас осталось {(3 - enter_number)} попыток.")
    user_password = (input('Введите пароль.\n'))
    if user_password != true_password:
        enter_number += 1
        print(f"Попробуйе еще раз. У вас осталось {(3 - enter_number)} попыток.")
        user_password = (input('Введите пароль.\n'))
        if user_password != true_password:
            enter_number += 1
            print("Вы првевысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки")
        else: print(wellcome)
    else: print(wellcome)
else: print(wellcome)

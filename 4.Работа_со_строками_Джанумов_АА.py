# задание 1
favour_word = 'деньги'
print(favour_word)

# задание 2

first_name1 = 'Виталий'
last_name1 = 'Красилов'
new_account1 = last_name1[:4]
temp_password1 = last_name1[2:6]


# задание 3

def account_generator(first_name,last_name):
    return first_name[:3] + last_name[:3]

new_account = account_generator('гарик','харламов')
print(new_account)

# задание 4 ("Руководство компании снова хочет обновить способ генерации..." гарика харламова взломали - главного сотрудника)

def password_generator(first_name,last_name): return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

temp_password2 = password_generator('гарик','харламов')
print(temp_password2)

# задание 5

company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# задание 6

first_name = 'жоб'
last_name = 'дейли'

fixed_first_name = 'Р' + first_name[1:]

# задание 7

password_rob = 'theycallme\"crazy\"91'

# задание 8

poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()

print(poem_title, poem_title_fixed)





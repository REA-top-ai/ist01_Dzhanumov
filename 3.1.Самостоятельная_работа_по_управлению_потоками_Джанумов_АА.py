# задание 1 (чуть правило хорошего тона придерживаюсь, пока не выгорел)

import random
import sys

name = input('Введите Ваше имя.\n')
question = input('Задайте вопрос, на который можно ответить да или нет\n')
answer = ''
random_number = random.randint(1, 9)
question_count = 0

while question.strip() == '':

    print('Magic 8-Ball не может принести удачу, иначе ткань реальности окажется под угрозой!')
    question = input('Задайте вопрос, на который можно ответить ИЛИ ДА ИЛИ НЕТ!\n')
    question_count += 1

    if question_count > 3:

        print('бро... ты не обучаем... извини, но ты в черном списке.')
        with open("blacklist.txt", "a", encoding="utf-8") as f:
            f.write(name + '\n')
        sys.exit()

if name == '':

    if question.strip().lower() == 'какой лучший вуз?':
        print('рэу, что за вопросы? Ваше имя запис.. а, вы не ставили ник. Я все равно найду тебя!')
        sys.exit()

    else:
        if random_number == 1:
            answer = 'Да, безусловно.'
        elif random_number == 2:
            answer = 'Это решительно так.'
        elif random_number == 3:
            answer = 'Без сомнения.'
        elif random_number == 4:
            answer = 'Ответ туманный, попробуйте еще раз.'
        elif random_number == 5:
            answer = 'Спросите еще раз позже.'
        elif random_number == 6:
            answer = 'Лучше не говорить вам сейчас.'
        elif random_number == 7:
            answer = 'Мои источники говорят «нет».'
        elif random_number == 8:
            answer = 'Прогноз не очень хороший.'
        elif random_number == 9:
            answer = 'Очень сомнительно.'
        else:
            answer = 'Ошибка, попробуйте перезапустить команду!'

        print(f'спрашивает: {question}')
        print(f'Магический шар отвечает: {answer}')
else:

    if question.strip().lower() == 'какой лучший вуз?':

        print('рэу, что за вопросы? Ваше имя записано в черный список!')
        with open("blacklist.txt", "a", encoding="utf-8") as f:
            f.write(name + '\n')
        sys.exit()

    else:

        if random_number == 1:
            answer = 'Да, безусловно.'
        elif random_number == 2:
            answer = 'Это решительно так.'
        elif random_number == 3:
            answer = 'Без сомнения.'
        elif random_number == 4:
            answer = 'Ответ туманный, попробуйте еще раз.'
        elif random_number == 5:
            answer = 'Спросите еще раз позже.'
        elif random_number == 6:
            answer = 'Лучше не говорить вам сейчас.'
        elif random_number == 7:
            answer = 'Мои источники говорят «нет».'
        elif random_number == 8:
            answer = 'Прогноз не очень хороший.'
        elif random_number == 9:
            answer = 'Очень сомнительно.'
        else:
            answer = 'Ошибка, попробуйте перезапустить команду!'

        print(f'{name} спрашивает: {question}')
        print(f'Магический шар отвечает: {answer}')

# задание 2

mini = float(input('Введите минимальное значениие: '))
maxi = float(input('Введите максимальное значение: '))
avarage = float(input('Введите среднее значиение: '))
standart = float(input('Введите стандартное отклонение: '))
 
if (maxi > 5 * standart + avarage) or (mini < avarage - standart * 5 ): print('В ваших данных имеются экстремальные значения и требуют предобработки\n')
elif (maxi > 3 * standart + avarage) or (mini < avarage - standart * 3 ): print('В ваших данных имеются выбросы и требуют предобработки\n')
else: print('Ваши данные пригодны для анализа\n')


# задание 3

age_of_user = int(input('Возраст введите: '))
age_limit = 18
print("Приятного просмотра!" if age_of_user >= age_limit else 'Извините, ваш возраст не соответствует введенным возрастным ограничениям')


# задание 4


age = int(input('Введите ваш возраст: '))
stazh = int(input('Введите ваш стаж: '))
reputation = int(input('Введите вашу репутацию (1–5): '))
traffic = int(input('Введите уровень пробок (1–7): '))
car = int(input('1 — Volkswagen Polo, 777 — BMW X1: '))
time = int(input('Введите время поездки (в минутах): '))

tarif = None


if 20 <= age <= 27:
    age_group = '20-27'
elif 27 < age <= 34:
    age_group = '27-34'
else:
    print('Возраст вне диапазона')
    sys.exit()

if 2 <= stazh <= 9:
    stazh_group = '2-9'
elif 10 <= stazh <= 15:
    stazh_group = '10-15'
else:
    print('Стаж вне диапазона')
    sys.exit()

if 1 <= reputation <= 2:
    rep_group = '1-2'
elif 3 <= reputation <= 5:
    rep_group = '3-5'
else:
    print('Репутация вне диапазона')
    sys.exit()

if 1 <= traffic <= 3:
    traffic_group = '1-3'
elif 4 <= traffic <= 7:
    traffic_group = '4-7'
else:
    print('Пробки вне диапазона')
    sys.exit()


if car == 1:  
    if age_group == '20-27' and stazh_group == '2-9' and rep_group == '1-2' and traffic_group == '1-3':
        tarif = 8
    elif age_group == '20-27' and stazh_group == '2-9' and rep_group == '1-2' and traffic_group == '4-7':
        tarif = 8.5
    elif age_group == '20-27' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '1-3':
        tarif = 7.5
    elif age_group == '20-27' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '4-7':
        tarif = 7.4
    elif age_group == '27-34' and stazh_group == '2-9' and rep_group == '1-2' and traffic_group == '1-3':
        tarif = 7.2
    elif age_group == '27-34' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '1-3':
        tarif = 7
    elif age_group == '27-34' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '4-7':
        tarif = 7.2
    elif age_group == '27-34' and stazh_group == '10-15' and rep_group == '1-2' and traffic_group == '1-3':
        tarif = 6.9
    elif age_group == '27-34' and stazh_group == '10-15' and rep_group == '1-2' and traffic_group == '4-7':
        tarif = 6.7
    elif age_group == '27-34' and stazh_group == '10-15' and rep_group == '3-5' and traffic_group == '4-7':
        tarif = 6.6

elif car == 777:  
    if age_group == '20-27' and stazh_group == '2-9' and rep_group == '1-2' and traffic_group == '1-3':
        tarif = 12
    elif age_group == '20-27' and stazh_group == '2-9' and rep_group == '1-2' and traffic_group == '4-7':
        tarif = 12.5
    elif age_group == '20-27' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '1-3':
        tarif = 11.6
    elif age_group == '20-27' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '4-7':
        tarif = 11.3
    elif age_group == '27-34' and stazh_group == '2-9' and rep_group == '1-2' and traffic_group == '1-3':
        tarif = 11.4
    elif age_group == '27-34' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '1-3':
        tarif = 11.7
    elif age_group == '27-34' and stazh_group == '2-9' and rep_group == '3-5' and traffic_group == '4-7':
        tarif = 11.9
    elif age_group == '27-34' and stazh_group == '10-15' and rep_group == '1-2' and traffic_group == '1-3':
        tarif = 10.8
    elif age_group == '27-34' and stazh_group == '10-15' and rep_group == '3-5' and traffic_group == '4-7':
        tarif = 10.9
    elif age_group == '27-34' and stazh_group == '10-15' and rep_group == '1-2' and traffic_group == '4-7':
        tarif = 11
else:
    print('Неверный выбор автомобиля')
    sys.exit()


if tarif is None:
    print('Для ваших параметров тариф не найден')
else:
    price = tarif * time
    print(f'Стоимость вашей поездки составит {price}')


# задание 5

coffe_number = int(input('выберете кофе от 1-4: капучино латте фрапучино эспрессо\n'))

if coffe_number == 1:
    print("""
    рецепт капучино:
    1.	Сварите кофе. Можно сварить в турке (доведите до кипения 2–3 раза, чтобы напиток получился насыщеннее). Или заварить во френч-прессе. Обязательно процедите, налейте в подогретую кружку.
	2.	Подогрейте молоко. Старайтесь не перегревать его больше, чем 65 градусов. Оно не должно быть сильно горячим.
	3.	Взбейте с помощью блендера или миксера. Добивайтесь однородной пены, без крупных пузырьков.
	4.	Влейте взбитую массу в кофе.
    """)
elif coffe_number == 2:
    print("""
    рецепт латте:
    1.	Кофе следует заварить, причем любым способом, который вам кажется удобнее.
	2.	Главное, чтобы кофе был довольно крепким.
	3.	Молоко нужно разогреть, но не кипятить: оптимальной будет температура в 50–60 градусов. Читайте ещё: вкусный рецепт приготовления кофе по-турецки.
	4.	После этого его нужно тщательно взбить с помощью блендера (либо миксера).
	5.	Процедура займёт порядка 5 минут, пока не образуется воздушная пена.
	6.	Следующий шаг — это переливание молока в заранее подготовленный высокий бокал (лучше всего для этого подходит так называемый айриш-бокал).
	7.	Пена в итоге всё равно останется сверху.
	8.	Затем нужно влить в молоко кофе.
	9.	Делать это нужно очень аккуратно, кофе должен литься тоненькой струйкой.
	10.	Дело в том, что только таким образом может получиться правильный трёхслойный напиток: молоко, кофе и пена сверху.
	11.	Завершается приготовление классического латте добавлением корицы либо шоколада сверху.
	12.	Впрочем, можно и вовсе не добавлять ничего.    
    """)
elif coffe_number == 3:
    print(""""
    рецепт фрапучино:
    1.	Варим и охлаждаем кофе. Для его приготовления можно использовать турку, кофемашину и любой другой прибор.
        Внимание! Для данного рецепта кофе можно заменить зелёным чаем. Объём тот же — 150 мл.
	2.	Все компоненты помещаем в стационарный блендер. Ингредиенты взбиваем до тех пор, пока лёд не превратится в мелкую крошку.
	3.	Взбиваем сливки. Их предварительно нужно охладить, подержав 1–2 часа в холодильнике. При этом продукт нельзя замораживать, в противном случае он отслоится, и крем не получится. Сливки взбиваем миксером. Сначала устанавливаем минимальные обороты, постепенно увеличивая их количество. Продукт взбиваем до того момента, пока масса не будет сохранять форму.
	4.	Кофе переливаем в бокал. Сверху украшаем сливками. Подаём холодным.
    """)
elif coffe_number == 4:
    print("""
    рецепт эспрессо:
    1.	В чашку с толстыми стенками насыпают растворимый кофе и сахарный песок в тех количествах, которые обычно используются для одной порции.
	2.	Далее в чашку добавляют немного кипятка и интенсивно взбивают ложкой полученную смесь.
	3.	После некоторого времени масса посветлеет и приобретёт консистенцию сметаны.
	4.	Во взбитую смесь аккуратно доливают оставшуюся воду, медленно помешивая до образования густой пены.     
    """)
else:
    while  coffe_number < 0 or coffe_number > 4:
        coffe_number = int(input("Ошибка: введите число от 1 до 4. кап латт фрап эспр.")) 

# задание 6 с1-с5 это столбцы
c1 = random.randint(1, 8)
c2 = random.randint(1, 8)
c3 = random.randint(1, 8)
c4 = random.randint(1, 8)
c5 = random.randint(1, 8)


if c1 == 1:
    p1 = 'Коллеги,'
elif c1 == 2:
    p1 = 'В то же время,'
elif c1 == 3:
    p1 = 'Однако,'
elif c1 == 4:
    p1 = 'Тем не менее,'
elif c1 == 5:
    p1 = 'Следовательно,'
elif c1 == 6:
    p1 = 'Соответственно,'
elif c1 == 7:
    p1 = 'Вместе с тем,'
else:
    p1 = 'С другой стороны,'


if c2 == 1:
    p2 = 'парадигма цифровой экономики'
elif c2 == 2:
    p2 = 'контекст цифровой трансформации'
elif c2 == 3:
    p2 = 'диджитализация бизнес-процессов'
elif c2 == 4:
    p2 = 'прагматичный подход к цифровым платформам'
elif c2 == 5:
    p2 = 'совокупность сквозных технологий'
elif c2 == 6:
    p2 = 'программа прорывных исследований'
elif c2 == 7:
    p2 = 'ускорение блокчейн-транзакций'
else:
    p2 = 'экспоненциальный рост Big Data'


if c3 == 1:
    p3 = 'открывает новые возможности для'
elif c3 == 2:
    p3 = 'выдвигает новые требования'
elif c3 == 3:
    p3 = 'несет в себе риски'
elif c3 == 4:
    p3 = 'расширяет горизонты'
elif c3 == 5:
    p3 = 'заставляет искать варианты'
elif c3 == 6:
    p3 = 'не оставляет шанса для'
elif c3 == 7:
    p3 = 'повышает вероятность'
else:
    p3 = 'обостряет проблему'


if c4 == 1:
    p4 = 'дальнейшего углубления'
elif c4 == 2:
    p4 = 'бюджетного финансирования'
elif c4 == 3:
    p4 = 'синергетического эффекта'
elif c4 == 4:
    p4 = 'компрометации конфиденциальных'
elif c4 == 5:
    p4 = 'универсальной коммодитизации'
elif c4 == 6:
    p4 = 'несанкционированной кастомизации'
elif c4 == 7:
    p4 = 'нормативного регулирования'
else:
    p4 = 'практического применения'


if c5 == 1:
    p5 = 'знаний и компетенций.'
elif c5 == 2:
    p5 = 'непроверенных гипотез.'
elif c5 == 3:
    p5 = 'волатильных активов.'
elif c5 == 4:
    p5 = 'опасных экспериментов.'
elif c5 == 5:
    p5 = 'государственно-частных партнерств.'
elif c5 == 6:
    p5 = 'цифровых следов граждан.'
elif c5 == 7:
    p5 = 'нежелательных последствий.'
else:
    p5 = 'внезапных открытий.'

print(p1, p2, p3, p4, p5)

#это была пытка..
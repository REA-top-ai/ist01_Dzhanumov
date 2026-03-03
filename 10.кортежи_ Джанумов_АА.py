# задание 1

correct_answers = (
    1, 2, 3, 2, 1,
    2, 1, 3, 1, 2,
    1, 2, 3, 3, 2,
    1, 2, 1, 2, 1
)

user_answers = []

print("Введите ответы (20 чисел от 1 до 3):")
for i in range(20):
    answer = int(input(f"Вопрос {i + 1}: "))
    user_answers.append(answer)

if tuple(user_answers) == correct_answers:
    print("Экзамен сдан")
else:
    print("Хахахахахха не сдал")
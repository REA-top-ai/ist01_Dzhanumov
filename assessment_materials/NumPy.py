import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
print(test_1)

# task 2
test_2_csv = np.genfromtxt("test_2.csv", delimiter=",")

print(test_2_csv)

# task 3

test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2

print(test_3_fixed)

# task 4

total_grade = test_1 + test_2_csv + test_3_fixed

final_grade = total_grade / 3

print(final_grade)

# task 5

coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_2 = np.array([0, 0, 1, 1, 1])

coin_toss_again = np.array([coin_toss, coin_toss_2])

# task 6

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[3]

manual_adwoa_test_1 = test_1[1:3]


# task 7

student_scores = np.array([test_1, test_2, test_3])

tanya_test_3 = student_scores[2, 3]

cody_test_scores = student_scores[:, 4]

# task 8

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge > 60) & (porridge < 80)]

print(cold, hot, just_right)


# task 9 final

temperature_data = np.genfromtxt("temperature_data.csv", delimiter=",")

print(temperature_data)

temperature_data_fixed = temperature_data + 3

print(temperature_data_fixed)

monday_temperas = temperature_data_fixed[0, :]

print("1", monday_temperas)

thursday_friday_morning = np.array(
    [temperature_data_fixed[3, 1], temperature_data_fixed[4, 1]]
)

print("2", thursday_friday_morning)

temperature_extremes = temperature_data_fixed[(temperature_data_fixed < 50) | (temperature_data_fixed > 60)]

print(temperature_extremes)

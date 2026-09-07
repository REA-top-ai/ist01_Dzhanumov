# task 1
import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18, 9, 2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)

print(store_one_avg, store_two_avg, store_three_avg)

best_seller = np.max([store_one_avg, store_two_avg, store_three_avg])
print(best_seller)

# task 2

class_year = np.array(
    [
        1967,
        1949,
        2004,
        1997,
        1953,
        1950,
        1958,
        1974,
        1987,
        2006,
        2013,
        1978,
        1951,
        1998,
        1996,
        1952,
        2005,
        2007,
        2003,
        1955,
        1963,
        1978,
        2001,
        2012,
        2014,
        1948,
        1970,
        2011,
        1962,
        1966,
        1978,
        1988,
        2006,
        1971,
        1994,
        1978,
        1977,
        1960,
        2008,
        1965,
        1990,
        2011,
        1962,
        1995,
        2004,
        1991,
        1952,
        2013,
        1983,
        1955,
        1957,
        1947,
        1994,
        1978,
        1957,
        2016,
        1969,
        1996,
        1958,
        1994,
        1958,
        2008,
        1988,
        1977,
        1991,
        1997,
        2009,
        1976,
        1999,
        1975,
        1949,
        1985,
        2001,
        1952,
        1953,
        1949,
        2015,
        2006,
        1996,
        2015,
        2009,
        1949,
        2004,
        2010,
        2011,
        2001,
        1998,
        1967,
        1994,
        1966,
        1994,
        1986,
        1963,
        1954,
        1963,
        1987,
        1992,
        2008,
        1979,
        1987,
    ]
)

millenial_procent = np.mean(class_year >= 2005)

print(millenial_procent)

# task 3

allergy_trials = np.array([[6, 1, 3, 8, 2], [2, 6, 3, 9, 8], [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)

trial_mean = np.mean(allergy_trials, 1)

patient_mean = np.mean(allergy_trials, 0)

print("3", total_mean, trial_mean, patient_mean)


# task 4

temps = np.array(
    [
        86,
        88,
        94,
        85,
        97,
        90,
        87,
        85,
        94,
        93,
        92,
        95,
        98,
        85,
        94,
        91,
        97,
        88,
        87,
        86,
        99,
        89,
        89,
        99,
        88,
        96,
        93,
        96,
        85,
        88,
        191,
        95,
        96,
        87,
        99,
        93,
        90,
        86,
        87,
        100,
        187,
        98,
        101,
        101,
        96,
        94,
        96,
        87,
        86,
        92,
        98,
        94,
        98,
        90,
        99,
        96,
        99,
        86,
        97,
        98,
        86,
        90,
        86,
        94,
        91,
        88,
        196,
        195,
        93,
        97,
        199,
        87,
        87,
        90,
        90,
        98,
        88,
        92,
        97,
        88,
        85,
        94,
        88,
        93,
        198,
        90,
        91,
        90,
        92,
        92,
    ]
)

sorted_temps = np.sort(temps)

print("4", sorted_temps)

# task 5

zarplata = np.array([10100, 35500, 105000, 85000, 25500, 40500, 65000])

sorted_zarplata = np.sort(zarplata)
print(sorted_zarplata)
mediana = None

if len(zarplata) % 2 == 1:
    mediana = sorted_zarplata[(len(zarplata) - 1) // 2]
else:
    m1 = (((len(zarplata) - 1)) // 2) - 1
    m2 = ((len(zarplata)) - 1) // 2
    mediana = (sorted_zarplata[m1] + sorted_zarplata[m2]) / 2

print(mediana)

# task 6

large_set = np.genfromtxt("home_income.csv", delimiter=" ")

large_set_median = np.mean(large_set)

print("task 6 -", large_set_median)

# task 7

time_spent = np.genfromtxt("time_spent.csv")

minutes_mean = np.mean(time_spent)

minutes_median = np.median(time_spent)

print(minutes_mean, minutes_median)

best_measure = minutes_median

# task 8

patrons = np.array([2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 30)

seventieth_percentile = np.percentile(patrons, 70)

print(thirtieth_percentile, seventieth_percentile)

# task 9

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)

therd_quarter = np.percentile(movies_watched, 75)

terquartile_range = therd_quarter - first_quarter

print(f'task 9 - {terquartile_range}')

# task 10 

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])
acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)

pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)

print(pumpkin_std, acorn_squash_std)

winner = pumpkin

# task 11

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.36, 4.82, 5.11])

rain_mean = np.mean(rainfall)
rain_median = np.median(rainfall)
first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)
mezh = third_quarter - first_quarter
rain_std = np.std(rainfall)

#всем спасибо всем пока
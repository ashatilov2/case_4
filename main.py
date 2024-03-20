# Case-study #4
# Developers: Shatilov A., Obidin D.
#

"""
Программа на вход получает вес, рост, возраст, коэффициент активности и выводит дневную норму калорий.
Затем на вход вводится рацион на завтрак, обед, ужин и суммируется в количество потребленных калорий за сутки.
Итог программы - сравнение нормы калорий с потребленными.

"""


import ru_local_1 as ru


def main():
    weight = int(input(ru.weight_1))
    height = int(input(ru.height_1))
    age = int(input(ru.age_1))
    activity_w = int(input(ru.activity_1))

    match activity_w:
        case 1:
            activity = 1.2
        case 2:
            activity = 1.38
        case 3:
            activity = 1.46
        case 4:
            activity = 1.55
        case 5:
            activity = 1.64
        case 6:
            activity = 1.73
        case 7:
            activity = 1.9
        case _:
            activity = 'Неверно введён знак'

    pol = int(input(ru.pol_1))

    match pol:
        case 1:
            dci = (weight * 10 + height * 6.25 - age * 5 + 5) * activity
        case 2:
            dci = (weight * 10 + height * 6.25 - age * 5 - 161) * activity
        case _:
            dci = 'Неверно введён знак'

    print('DCI = ', dci)

    # вводим меню завтрака
    breakfast = int(input(ru.breakfast_1))

    match breakfast:
        case 1:
            breakfast_cal = 240
        case 2:
            breakfast_cal = 270
        case 3:
            breakfast_cal = 308
        case 4:
            breakfast_cal = 461
        case 5:
            breakfast_cal = 252
        case 6:
            breakfast_cal = 678
        case 7:
            breakfast_cal = 340
        case 8:
            breakfast_cal = 200
        case _:
            breakfast_cal = 'Неверно введён знак'

    print('калории на завтрак:', breakfast_cal)

    # вводим меню обеда
    dinner = int(input(ru.dinner_1))

    match dinner:
        case 1:
            dinner_cal = 264
        case 2:
            dinner_cal = 280
        case 3:
            dinner_cal = 500
        case 4:
            dinner_cal = 400
        case 5:
            dinner_cal = 200
        case 6:
            dinner_cal = 496
        case 7:
            dinner_cal = 800
        case _:
            dinner_cal = 'Неверно введён знак'
    print('калории на обед:', dinner_cal)

    # вводим меню ужина
    evening_meal = int(input(ru.evening))

    match evening_meal:
        case 1:
            evening_cal = 200
        case 2:
            evening_cal = 500
        case 3:
            evening_cal = 467
        case 4:
            evening_cal = 253
        case 5:
            evening_cal = 545
        case 6:
            evening_cal = 496
        case 7:
            evening_cal = 800
        case 8:
            evening_cal = 1700
        case _:
            evening_cal = 'Неверно введён знак'

    print('калории на ужин:', evening_cal)

    # общее число калорий
    calories = breakfast_cal + evening_cal + dinner_cal
    print('Ваши калории за день: ', calories)

    if dci < calories + 100:
        print('избыток калорий')
    elif dci > calories - 100:
        print('дефицит калорий')
    elif (dci >= calories + 100) and (dci <= calories - 100):
        print('норма калорий')


if __name__ == '__main__':
    main()


import math
# метод для разложения введенного числа на простые множители
def prime_factors(input_num):
    prime_factors_list = []
    # проходим по всем числам от 2 до введенного
    for i in range(2, input_num + 1):
        # пока полученное число делится на текущее значение i без остатка, записываем этот делитель в список
        while not input_num % i:
            prime_factors_list.append(i)
            input_num //= i
    return prime_factors_list


def pow_pi(num):
    # рассчитываем коэффициент для вычисления с заданной точностью - единицу делим на введенное число
    # и округляем до целого
    k = int(round(1/float(num), 0))
    # возвращаем кортеж из числа Пи, математически посчитанного результата и результата через округление
    # до количества знаков = количеству знаков после "." во введенном числе
    return int(math.pi * k) / k

# метод для создания списка из элементов исходного списка, которые не повторяются
def exclude_duplicates(input_list):
    type(input_list)
    new_list = []
    for i in input_list:
        if input_list.count(i) < 2:
            new_list.append(i)
    return new_list



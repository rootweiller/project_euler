"""
    @Author: Juan Vargas
"""
import time

start = time.time()


def bouncy_execution(number):
    """

    :param number: 21780
    :return: string with result of exercise
    """
    increment = False
    decrement = False
    result = str(number)

    for item in range(len(result)-1):
        if result[item+1] > result[item]:
            increment = True
        elif result[item+1] < result[item]:
            decrement = True
        if increment and decrement:
            return True
    return False


def number_bouncy():
    """

    :return: solution of problem
    """

    number = input("Insert number: ")

    p_range = 0.90
    b = int(number) * p_range

    while p_range != 0.99:
        number += 1
        if bouncy_execution(number):
            b += 1
        p_range = b / number

    print("Solution is = {0} executed in {1} seconds".format(number, str(time.time()-start)))

    return p_range


execution = number_bouncy()

#!/bin/env python3
# -*- coding: utf-8 -*-


import math
import matplotlib.pyplot as plt


wektor_cech = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 10, 10, 12, 12, 12, 12, 13, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 18, 20, 23, 25, 30]


def n(lista):
    return len(lista)


def rozstep(lista):
    return max(lista) - min(lista)


def k_1(lista):
    k_1 = 5 * math.log10(n(lista))
    return k_1

def k_2(lista):
    k_2 = 1 + 3.322 * math.log10(n(lista))
    return k_2


def print_result(list_of_tests):
    print()
    for i in list_of_tests:
        print("{:50} {:>9.3f}".format(i[0], i[1]))


def rozpietosc(lista):
    k = int(k_2(lista))
    return round(rozstep(lista) / k, 0)


list_of_tests = [
                    ["Liczebność populacji N:", n(wektor_cech)],
                    ["Rozstep R(x):", rozstep(wektor_cech)],
                    ["Liczba przedziałów klasowych k = 5log(N):", k_1(wektor_cech)],
                    ["Liczba przedziałów klasowych k = 1 + 3.222log(N):", k_2(wektor_cech)],
                    ["Rozpiętość przedziału i':", rozpietosc(wektor_cech)]
                ]



print_result(list_of_tests)

num_bins = 6

fig, ax = plt.subplots()
n, bins, patches = ax.hist(wektor_cech, num_bins, density=1)

fig.tight_layout()
plt.show()
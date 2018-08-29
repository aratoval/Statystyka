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
    return int(round(rozstep(lista) / k, 0))


list_of_tests = [
                    ["Liczebność populacji N:", n(wektor_cech)],
                    ["Rozstep R(x):", rozstep(wektor_cech)],
                    ["Liczba przedziałów klasowych k = 5log(N):", k_1(wektor_cech)],
                    ["Liczba przedziałów klasowych k = 1 + 3.222log(N):", k_2(wektor_cech)],
                    ["Rozpiętość przedziału i':", rozpietosc(wektor_cech)]
                ]



print_result(list_of_tests)

num_bins = 6
rozpietosc_przedzialu = rozpietosc(wektor_cech)

fig, ax = plt.subplots()
n, bins, patches = ax.hist(wektor_cech, num_bins)
ax.set_xlabel('Ilość zatrudnionych osób')
ax.set_ylabel('Ilość firm w danym przedziale')
fig.tight_layout()
#plt.show()


def f(lista, num_bins, rozpietosc_przedzialu):
    wektor_f =[0] * num_bins
    przedzialy = range(0, num_bins*rozpietosc_przedzialu + 1, rozpietosc_przedzialu)
    for i in lista:
        for j in przedzialy:
            if i <= j + rozpietosc_przedzialu and i > j:
                wektor_f[int(j/5)] += 1
    return wektor_f


wektor_f = f(wektor_cech, num_bins, rozpietosc_przedzialu)
print("Liczebność przedziału f\u1D62:", wektor_f)

def xi(num_bins, rozpietosc_przedzialu):
    wektor_xi = []
    for i in range(0, num_bins * rozpietosc_przedzialu, rozpietosc_przedzialu):
        wektor_xi.append((2 * i + rozpietosc_przedzialu) / 2)
    return wektor_xi

wektor_xi = xi(num_bins, rozpietosc_przedzialu)
print("Reprezentant przedziału x\u1D62':", wektor_xi)

suma_fi = sum(wektor_f)
suma_xifi = sum([a*b for a,b in zip(wektor_f, wektor_xi)])

print("{:50} {:>9.3f}".format("\u2211f\u1D62:", suma_fi))
print("{:50} {:>9.3f}".format("\u2211f\u1D62x\u1D62':", suma_xifi))

x_srednie = suma_xifi / suma_fi

print("{:50}  {:>9.3f}".format("Wartość średnia x\u0304:", x_srednie))

def dominanta(rozpietosc_przedzialu, wektor_f):
    fD = max(wektor_f)
    poz = wektor_f.index(fD)
    fD_1 = wektor_f[poz - 1]
    fD_p1 = wektor_f[poz + 1]
    x0D = poz * rozpietosc_przedzialu
    D = x0D + rozpietosc_przedzialu * (fD - fD_1) / (2 * fD - fD_1 - fD_p1)
    return round(D, 2)

num_diminanta = dominanta(rozpietosc_przedzialu, wektor_f)
print("{:50} {:>9.3f}".format("Dominanta D(x):", num_diminanta))

def mediana(wektor_f, rozpietosc_przedzialu):
    temp = 0
    half = sum(wektor_f) / 2
    for i in wektor_f:
        temp = temp + i
        if temp == half:
            break
    x0M = rozpietosc_przedzialu * wektor_f.index(i)
    fM = wektor_f[wektor_f.index(i)]
    suma_fi = 0
    for j in range(wektor_f.index(i)):
        suma_fi = suma_fi + wektor_f[j]
    return x0M + rozpietosc_przedzialu * (sum(wektor_f) / 2 - suma_fi) / fM


num_mediana = mediana(wektor_f, rozpietosc_przedzialu)
print("{:50} {:>9.3f}".format("Mediana M(x):", num_mediana))

def wariancja(wektor_f, x_srednie, wektor_xi):
    wektor_xi_x_srednie_2 = []
    for i in wektor_xi:
        wektor_xi_x_srednie_2.append((i - x_srednie)**2)
    return sum([a*b for a,b in zip(wektor_f, wektor_xi_x_srednie_2)])/sum(wektor_f)


num_wariancja = wariancja(wektor_f, x_srednie, wektor_xi)
print("{:50} {:>10.4f}".format("Wariancja S\u00B2(x):", num_wariancja))


def odchylenie_standardowe(num_wariancja):
    return math.sqrt(num_wariancja)

num_odchylenie_standardowe = odchylenie_standardowe(num_wariancja)
print("{:50} {:>8.2f}".format("Odchylenie standardowe S(x):", num_odchylenie_standardowe))


def v(num_odchylenie_standardowe, x_srednie):
    return num_odchylenie_standardowe / x_srednie

num_v = v(num_odchylenie_standardowe, x_srednie)
print("{:50} {:>8.2f}".format("Współczynnik zmienności V(x):", num_v))
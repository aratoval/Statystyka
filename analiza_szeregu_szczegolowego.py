#!/bin/env python3
# -*- coding: utf-8 -*-


def srednia(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma/len(lista)


def srednia_wazona(lista, wagi):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i] * wagi[i]
    return suma/len(lista)


def maks(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max


def mins(lista):
    mins = lista[0]
    for i in lista:
        if i < mins:
            mins = i
    return mins


def suma(lista):
    temp = 0
    for i in lista:
        temp = temp + i
    return temp


def n(lista):
    count = 0
    for i in lista:
        count += 1
    return count


def dominanta(lista):
    temp = {}
    for i in lista:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1

    maks_name = list(temp.keys())
    maks = temp[maks_name[0]]

    for i in temp.keys():
        if temp[i] > maks:
            maks = temp[i]
            maks_name = i
    return maks_name


def mediana(lista):
    if len(lista) % 2 == 0.0:
        temp = int(len(lista)/2)
        return (lista[temp - 1] + lista[temp]) / 2.0
    else:
        return lista[int((len(lista) - 1)/2)]


def rozstep(lista):
    return maks(lista) - mins(lista)


def wariancja(lista):
    suma_kwadratow = 0
    srednia_temp = srednia(lista)
    for i in lista:
        suma_kwadratow = suma_kwadratow + (i - srednia_temp) ** 2
    return suma_kwadratow / n(lista)


def odchylenie_standardowe(lista):
    return wariancja(lista) ** 0.5


def wspolczynnik_zmiennosci(lista):
    return odchylenie_standardowe(lista) / srednia(lista)


def odchylenie_przecietne(lista):
    suma_abs = 0
    srednia_temp = srednia(lista)
    for i in lista:
        suma_abs = suma_abs + abs(i - srednia_temp)
    return suma_abs / n(lista)


def rzad_wielkosci_odchylenia(lista):
    return odchylenie_przecietne(lista) / srednia(lista)


def print_result(list_of_tests):
    print()
    for i in list_of_tests:
        print("{:30} {:>9.3f}".format(i[0], i[1]))


lista = [127, 129, 130, 132, 134, 135, 135, 135, 135, 140, 142, 143, 143, 144, 145, 145, 149, 152, 152, 153]

list_of_tests = [
                    ["Wartość średnia x\u0304:", srednia(lista)],
                    ["Wartość MAX:", maks(lista)],
                    ["Wartość MIN:", mins(lista)],
                    ["Suma wszystkich x \u2211x:", suma(lista)],
                    ["Ilosc obeserwacji N:", n(lista)],
                    ["Domoinanta D(x):", dominanta(lista)],
                    ["Mediana M(x):", mediana(lista)],
                    ["Rozstep R(x):",rozstep(lista)],
                    ["Wariancja S\u00B2(x):", wariancja(lista)],
                    ["Odchylenie standardowe S(x):", odchylenie_standardowe(lista)],
                    ["Wspolczynnik zmiennosci V(x):", wspolczynnik_zmiennosci(lista)],
                    ["Odchylenie przecietne d(x):", odchylenie_przecietne(lista)],
                    ["Rzad wielkosci odchylenia:", rzad_wielkosci_odchylenia(lista)]
                ]


print_result(list_of_tests)
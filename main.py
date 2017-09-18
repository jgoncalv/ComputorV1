#!/usr/bin/python3

import sys
import argparse

def parsing(argv):
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

def searchAndAssignCoeff(s1, s2):
    tab = s1.split(' ')
    for index, val in enumerate(tab):
        if val == s2:
            nb = float(tab[index - 2])
            if index - 3 > 0 and tab[index - 3] == "-":
                nb *= float(-1)
            return nb
    return 0

def getValue(s1, s2):
    dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    dic['a'] = searchAndAssignCoeff(s1, "X^0")
    dic['b'] = searchAndAssignCoeff(s1, "X^1")
    dic['c'] = searchAndAssignCoeff(s1, "X^2")
    dic['d'] = searchAndAssignCoeff(s1, "X^3")
    dic['w'] = searchAndAssignCoeff(s2, "X^0")
    dic['x'] = searchAndAssignCoeff(s2, "X^1")
    dic['y'] = searchAndAssignCoeff(s2, "X^2")
    dic['z'] = searchAndAssignCoeff(s2, "X^3")

    dic['a'] = dic['a'] - dic['w']
    dic['b'] = dic['b'] - dic['x']
    dic['c'] = dic['c'] - dic['y']
    dic['d'] = dic['d'] - dic['z']
    dic['w'] = 0
    dic['x'] = 0
    dic['y'] = 0
    dic['z'] = 0

    return dic

def negativeVal(val):
    if val < 0:
        return val * -1
    return val

def reduceForm(equation, dic):
    degre = 0
    for index, val in enumerate(equation):
        if val == "X^0":
            equation[index - 2] = str(negativeVal(dic['a']))
            degre = 0
        elif val == "X^1":
            equation[index - 2] = str(negativeVal(dic['b']))
            degre = 1
        elif val == "X^2":
            equation[index - 2] = str(negativeVal(dic['c']))
            degre = 2
        elif val == "X^3":
            equation[index - 2] = str(negativeVal(dic['d']))
            degre = 3

    equation.append("= 0")

    string = ""
    for val in equation:
        if string != "":
            string += " "
        string += val

    return string, degre

def compareSplit(tab1, tab2):
    del(tab1[-1])
    del(tab2[0])
    if tab1 == tab2:
        print("Tous les nombres réels sont solution.")
        return -1
    elif len(tab1) == len(tab2) and len(tab1) == 3:
        print("Il y a une erreur dans l'equation.")
        return -1
    return 1

def sq_rt(nb):
    return (nb**(0.5))

def resolveEq(dic, degre):
    if degre == 1:
        res = dic['a'] * -1 / dic['b']
        print("La solution est :\n" + str(res))
    elif degre == 2:
        delta = dic['b'] * dic['b'] - 4 * dic['a'] * dic['c']
        if delta == 0:
            print("Le discriminant est égal à 0, la solution est:")
            nb = -1 * dic['b'] / (2 * dic['c'])
            print(str(nb))
        elif delta > 0:
            print("Le discriminant est supérieur à 0, les deux solutions réelles sont:")
            nb1 = (-1 * dic['b'] - sq_rt(delta)) / (2 * dic['c'])
            nb2 = (-1 * dic['b'] + sq_rt(delta)) / (2 * dic['c'])
            print("x1 = " + str(nb1))
            print("x2 = " + str(nb2))
        elif delta < 0:
            print("L'équation n'admet pas de solution réelle, mais deux solutions complexes conjuguées:")
            b = -1 * dic['b']
            delta = -1 * delta
            c = dic['c']
            print("x1 = (" + str(b) + " − i√(" + str(delta) + ")) / (2 * " + str(c)+ ")")
            print("x2 = (" + str(b) + " + i√(" + str(delta) + ")) / (2 * " + str(c)+ ")")

def Main(argv):
    #parsing(argv)
    tab = argv[0].split("=")
    if -1 == compareSplit(tab[0].split(' '), tab[1].split(' ')):
        return
    values = getValue(tab[0], tab[1])
    reducedEq, degre = reduceForm(tab[0].split(' '), values)

    if degre >= 3:
        print("Le degré du polynome est strictement supérieur à 2, je ne peux le résoudre.")
        return
    print("Forme réduite: " + reducedEq)
    print("Polynome de degré: " + str(degre))
    resolveEq(values, degre)

if __name__ == "__main__":
    Main(sys.argv[1:])

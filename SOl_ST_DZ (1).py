# -*- coding: utf8 -*-
import itertools


def div(initial_m):
    # поиск единицы в m
    k = -1
    i = 0
    while k < 0:
        if initial_m[i] == 1:
            k = i
        else:
            if i == 10:
                k = 15
        i = i + 1
    m = []
    if k != 15:
        # деление m на образующий полином
        m.extend(initial_m[k:k + 5])
        g = [1, 0, 0, 1, 1]
        k += 5
        while m[0] == 1:
            for i in range(0, 5):
                if m[i] == g[i]:
                    m[i] = 0
                else:
                    m[i] = 1
            while m[0] == 0 and k < 15:
                del m[0]
                m.append(initial_m[k])
                k = k + 1
        del m[0]
    else:
        m.extend(initial_m[11:15])
    return m


def coding(initial_m):
    m = []
    m = div(initial_m)
    # конкатенация
    for i in range(0, 4):
        initial_m[i + 11] = m[i]
    return initial_m


def correction(m, i):
    if m[i] == 1:
        m[i] = 0
    else:
        m[i] = 1
    return m


def error_search(m):
    s = []
    s = div(m)
    if s != [0, 0, 0, 0]:
        i = 1
    else:
        i = 0
    return [m, i]

def test(m, m_old, err_count):
    err = error_search(m)
    m = []
    m.extend(err[0])
    n = 0
    err_count += err[1]
    for u in range(0, 15):
        if m[u] != m_old[u]:
            n += 1

    return err_count


i = 0
print("Enter binary code.")
while i == 0:
    m = str(input())
    m = list(m)
    if len(m) == 11:
        if [x for x in m if x != "0" and x != "1"]:
            print("Incorrect input. Try again.")
        else:
            print("Correct input.")
            for i in range(0,len(m)):
                m[i] = int(m[i])
                i = 1
    else:
        print("Incorrect input. Try again.")
print("Initial binary code:")
print(m)
m.extend([0, 0, 0, 0])
m = coding(m)
print("Loop binary code:")
print(m)
m_old = []
m_old.extend(m)
for err in range(1, 16):
    err_count = 0
    if err == 1:
        print("\nTEST: " + str(err) + " error\n")
    else:
        print("\nTEST: " + str(err) + " errors\n")
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    mask = []
    mask.extend(list(itertools.combinations(l, err)))
    for i in range(0, len(mask)):
        mask[i] = list(mask[i])
        for j in range(0, len(mask[i])):
            m = correction(m, mask[i][j])
        err_list = test(m, m_old, err_count)
        err_count = err_list
        m = []
        m.extend(m_old)
    print("Detecting ability: " + str(err_count / len(mask) * 100) + "%\n"
                                                                     "    - Detected errors: " + str(err_count))
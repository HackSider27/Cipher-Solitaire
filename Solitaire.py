# Cipher "Solitaire"
# 2 cards + 2 Jockers
# "2" - Jocker A
# "3" - Joker B

from itertools import permutations

def writefile(a, file):
    strf = ""
    for el in a:
        strf += str(el) + " "
    strf += "\t"
    file.write(strf)

def F1(lst):
    index = lst.index(2)
    new_index = index + 1
    if new_index > 3:
        new_index -= 3
    lst.insert(new_index, lst.pop(index))

def F2(lst):
    index = lst.index(3)
    new_index = index + 2
    if new_index > 3:
        new_index -= 3
    lst.insert(new_index, lst.pop(index))

def F3(lst):
    res = []
    k = 0
    i = 0

    index_2 = lst.index(2)
    index_3 = lst.index(3)
    max_index = max(index_3, index_2)
    min_index = min(index_3, index_2)

    while i != min_index:
        res.insert(k, lst[i])
        k += 1
        i += 1
    k = 0
    while i != max_index:
        res.insert(k, lst[i])
        k = k + 1
        i = i + 1
    res.insert(k, lst[max_index])
    k = 0
    i = i + 1
    while i != len(lst):
        res.insert(k, lst[i])
        k = k + 1
        i = i + 1
    for c in range(4):
        lst[c] = res[c]

def F4(lst):
    count = lst[3]
    if count == 3 or count == 0:
        return
    if count == 1:
        lst.insert(2, lst.pop(0))
    if count == 2:
        lst.insert(0, lst.pop(2))

a = [0, 1, 2, 3]
set_a = permutations(a)


crypt_set = [a.copy()]
file = open("result.txt", 'w')

for i in range(24):
    #strf = "Begin " + str(i + 1) + " : "
    #print(strf, a)
    writefile(a, file)
    F1(a)
    writefile(a, file)
    F2(a)
    writefile(a, file)
    F3(a)
    writefile(a, file)
    F4(a)
    writefile(a, file)
    file.write("\n")
    #strf = "End " + str(i + 1) + " : "
    #print(strf, a)
    if a in crypt_set:
        for el in set_a:
            if list(el) not in crypt_set:
                a = list(el)
                crypt_set.append(a.copy())
                break
    else:
        crypt_set.append(a.copy())

file.close()

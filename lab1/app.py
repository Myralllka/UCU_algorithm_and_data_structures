import time
import os
import random
import sys

E = int(sys.argv[1])


def selection_sort(lst):
    sel_counter = 0
    length = len(lst)
    for i in range(length):
        minn_i = i
        for key in range(i+1, length):
            sel_counter += 1
            if lst[minn_i] > lst[key]:
                minn_i = key
        lst[i], lst[minn_i] = lst[minn_i], lst[i]
    return lst, sel_counter


def insertion_sort(lst):
    ins_counter = 0
    for i in range(1, len(lst)):
        key = lst[i]
        flag = i - 1
        ins_counter += 1
        while flag > -1 and lst[flag] > key:
            ins_counter += 1
            lst[flag + 1] = lst[flag]
            flag -= 1
        lst[flag + 1] = key
    return lst, ins_counter


def shell_sort(lst):
    she_counter = 0
    length = len(lst)
    gap = length // 2
    while gap:
        for i in range(gap, length):
            element = lst[i]
            flag = i
            she_counter += 1
            while flag > gap-1 and lst[flag - gap] > element:
                she_counter += 1
                lst[flag] = lst[flag - gap]
                flag -= gap
            lst[flag] = element
        gap //= 2
    return lst, she_counter


selection_time_list = []
insertion_time_list = []
shell_time_list = []
shell_time_list.append('random: ')
insertion_time_list.append('random: ')
selection_time_list.append('random: ')
ll = [random.randrange(1000) for i in range(2 ** E)]
for _ in range(4):
    for i in range(10):
        new = ll.copy()
        time1 = time.time()
        co = selection_sort(new)[1]
        selection_time_list.append(time.time() - time1)
        selection_time_list.append(co)
        new = ll.copy()
        time1 = time.time()
        co = insertion_sort(new)[1]
        insertion_time_list.append(time.time() - time1)
        insertion_time_list.append(co)
        new = ll.copy()
        time1 = time.time()
        co = shell_sort(new)[1]
        shell_time_list.append(time.time() - time1)
        shell_time_list.append(co)
    if _ == 0:
        shell_time_list.append('sorted')
        insertion_time_list.append('sorted')
        selection_time_list.append('sorted')
        ll = sorted(ll)
    elif _ == 1:
        shell_time_list.append('back sorted')
        insertion_time_list.append('back sorted')
        selection_time_list.append('back sorted')
        ll = ll[::-1]
    else:
        shell_time_list.append("1-3")
        insertion_time_list.append("1-3")
        selection_time_list.append("1-3")
        ll = [random.randrange(3) for i in range(2 ** E)]


print(shell_time_list)
print('*'*20)
print(insertion_time_list)
print('*'*20)
print(selection_time_list)

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

print("Изначальный список", lst)

min = 0
max = 10

lst_new = [i for i in lst if min <= i <= max]


def index_range(lst_new):
    print("---- Выводим индексы диапазона ----")
    for i in lst_new:
        ind = lst.index(i)
        print(ind, end=" ")


print("Выводим элементы диапазона:", lst_new)
index_range(lst_new)
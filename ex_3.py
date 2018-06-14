import ex_1
import ex_2


list1 = ex_1.create_list(10)


def change_to_zero_diagonal(list):
    for i in range(len(list)):
        list[i][i] = 0
    return list


def change_to_binary(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] % 2 == 0:
                list[i][j] = 1
            else:
                list[i][j] = 0
    return list

def max_value_string(list):
    max_summ = 0
    i_max_summ = 0
    for i in range(len(list)):
        if sum(list[i]) > max_summ:
            max_summ = sum(list[i])
            i_max_summ = i
    print(list[i])

max_value_string(list1)
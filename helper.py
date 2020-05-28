# for bubble sort


def sort(list_to_sort, related_list):
    for i in range(len(list_to_sort)):
        j = len(list_to_sort) - 1
        while j > i:
            if list_to_sort[j] > list_to_sort[j - 1]:
                list_to_sort = exchange(list_to_sort, j, j - 1)
                related_list = exchange(related_list, j, j - 1)
            j -= 1
    return list_to_sort, related_list


def exchange(input_list, index1, index2):
    tmp = input_list[index1]
    input_list[index1] = input_list[index2]
    input_list[index2] = tmp
    return input_list

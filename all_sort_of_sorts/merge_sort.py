def merge_sort(lista):
    list_length = len(lista)

    if list_length == 1:
        return lista

    mid_point = list_length // 2

    left_partition = merge_sort(lista[:mid_point])
    right_partition = merge_sort(lista[mid_point:])

    return merge(left_partition, right_partition)


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

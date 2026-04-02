
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    first_list = participants_first_group.split(separator)
    second_list = participants_second_group.split(separator)
    first_set = set(first_list)
    second_set = set(second_list)
    result = first_set.intersection(second_set)
    result_list = sorted(result)
    return result_list


first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result_1 = find_common_participants(first_group, second_group, separator=".")
print(result_1)


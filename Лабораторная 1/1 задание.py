numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_of_numbers1 = numbers[:4]
list_of_numbers2 = numbers[5:]
count_of_numbers = len(numbers)
average = (sum(list_of_numbers1)+sum(list_of_numbers2))/len(numbers)
list_of_all_numbers = list_of_numbers1 + [average] + list_of_numbers2
print("Измененный список:", list_of_all_numbers)

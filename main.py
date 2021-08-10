
def average_string_length(list):
    total_letters = 0
    for i in list:
        total_letters = total_letters + len(i)
    average = total_letters / len(list)
    print('Average length of word is', average, 'characters')


input = (str(input('Enter words:')))
input_list = input.split()
average_string_length(input_list)

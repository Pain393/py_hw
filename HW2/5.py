my_list = [7, 5, 3, 3, 2]
max_element = max(my_list)
while True:
    new_element = input('Введите новый рейтинг в виде натурального числа: ')
    if new_element.isdigit():
        new_element = int(new_element)
        if new_element > max_element:
            my_list.insert(0, new_element)
            print(my_list)
            break
        elif new_element in my_list:
            my_list.insert(-my_list[::-1].index(new_element), new_element)
            print(my_list)
            break
        else:
            for element in range(len(my_list)):
                if my_list[element] < new_element:
                    my_list.insert(element, new_element)
                    print(my_list)
                    break
                elif min(my_list) > new_element:
                    my_list.append(new_element)
                    print(my_list)
                    break
            break
    else:
        print('Вы не соблюдаете правила, попробуйте еще раз!')
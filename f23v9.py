def find_empty_elements(arr):
    new_arr = []
    for element in arr:
        new_element = []
        for temp in element:
            if temp is None:
                continue
            else:
                new_element.append(temp)
        new_arr.append(new_element)
    return new_arr


def find_copy_elements(arr):
    new_arr = []
    bool_next = False
    for element in arr:
        for new_element in new_arr:
            if element == new_element:
                bool_next = True
                break
        if bool_next:
            bool_next = False
            continue
        else:
            new_arr.append(element)
    return new_arr


def convert_date(date_string):
    temp = ""
    for i in range(len(date_string)):
        if date_string[i] == "/":
            continue
        else:
            temp += date_string[i]
        if len(temp) == 4:
            temp += '-'
        if len(temp) == 7:
            temp += '-'
    return temp


def convert_mail(date_string):
    temp = ""
    for i in range(len(date_string)):
        if date_string[i] == "[":
            if date_string[i] + date_string[i+1] + date_string[i+2] + date_string[i+3] == "[at]":
                temp = ""
                for z in range(i + 4, len(date_string)):
                    temp += date_string[z]
                break
    return temp


def convert_name(date_string):
    string = str(date_string).split()
    temp = string[2] + " " + string[0]
    return temp


def turn_arr(arr):
    finale_arr = []
    finale_element_date = []
    finale_element_mail = []
    finale_element_name = []
    for element in arr:
        finale_element_date.append(element[0])
        finale_element_mail.append(element[1])
        finale_element_name.append(element[2])
    finale_arr.append(finale_element_date)
    finale_arr.append(finale_element_mail)
    finale_arr.append(finale_element_name)
    return finale_arr


def f23(arr):
    arr = find_empty_elements(arr)
    arr = find_copy_elements(arr)
    for element in arr:
        element[0] = convert_date(element[0])
        element[1] = convert_mail(element[1])
        element[2] = convert_name(element[2])
    arr = turn_arr(arr)
    return arr

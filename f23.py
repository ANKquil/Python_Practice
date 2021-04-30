def f23(arr):
    new_arr = []
    for element in arr:
        if element[0] is None:
            if element[1] is None:
                if element[2] is None:
                    continue
        new_arr.append(element)

        num = 0
        if element[num] == 'N':
            element[num] = 'false'
        elif element[num] == 'Y':
            element[num] = 'true'

        num = 1
        temp = ''
        date_year = ' '
        date_month = ' '
        date_day = ' '
        bool_1 = False
        bool_2 = False
        for i in range(len(str(element[num]))):
            if element[num][i] == '.':
                bool_1 = True
                break
        if bool_1:
            for i in range(len(str(element[num]))):
                if element[num][i] == '.':
                    if date_year == ' ':
                        date_year = temp
                        temp = ''
                    else:
                        date_month = temp
                        temp = ''
                if element[num][i].isdigit():
                    temp += element[num][i]
            date_day = temp
        else:
            for i in range(len(str(element[num]))):
                letter = str(element[num][i])
                if letter.isdigit():
                    temp += letter
                    print(temp)
                    if len(temp) == 2:
                        if date_day == ' ':
                            date_day = temp
                            temp = ''
                        elif date_month == ' ':
                            date_month = temp
                            temp = ''
                    elif len(temp) == 4:
                        date_year = temp
                        break
        element[num] = date_day + '/' + date_month + '/' + date_year

        num = 2
        temp = ''
        count = 0
        for i in range(len(str(element[num]))):
            number = element[num][len(str(element[num])) - i - 1]
            if number.isdigit():
                temp += number
                if count == 6:
                    break
                count += 1
        element[num] = ""
        for i in range(len(temp)):
            element[num] += temp[len(temp) - i - 1]
    return new_arr

from decimal import *


#zadanie1('00-000', '01-000')
def zadanie1(start, end):
    code1 = int(start.replace("-", ""))+1
    code2 = int(end.replace("-", ""))
    data = []
    while code1 < code2:
        code_string = str(code1)[:2]+"-"+str(code1)[2:]
        data.append(code_string)
        code1 += 1
    return data


#zadanie2([1,2,3], 10)
def zadanie2(data, n):
    full_list = list(range(1, n+1))
    set_full = set(full_list)
    set_data = set(data)
    return sorted(list(set_full.difference(set_data)))


#zadanie3(1, 3.0, 0.5)
def zadanie3(start, end, j):
    iter = Decimal(start)
    jump = Decimal(j)
    last_element = Decimal(end)
    data = []
    while iter <= last_element:
        data.append(iter)
        iter += jump
    return data


print(zadanie1("79-900", "80-155"))
print(zadanie2([2, 3, 7, 4, 9], 10))
print(zadanie3(2, 5.5, 0.5))

import re


def reformatNumber(number: str):
    x = []
    for item in number:
        if item.isdigit():
            x.append(item)
    # x = re.findall(r'\d+', number)
    resp = ''
    index = 0
    digit_amount = len(x)
    count = 0
    while digit_amount > 4:
        if count > 0:
            resp += '-'
        digit_amount -= 3
        resp += ''.join(x[index:index + 3])
        index += 3
        count += 1

    if count > 0:
        resp += '-'
    if digit_amount == 4:
        resp += ''.join(x[index:index + 2]) + '-' + ''.join(
            x[index + 2:index + 4])
    elif digit_amount == 3:
        resp += ''.join(x[-3:])
    elif digit_amount == 2:
        resp += ''.join(x[-2:])
    return resp


print(reformatNumber("1-23-45 6"))
print(reformatNumber("123 4-567"))
print(reformatNumber("123 4-5678"))
print(reformatNumber("12"))
print(reformatNumber("--17-5 229 35-39475 "))

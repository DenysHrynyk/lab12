import re


def result():
    regexp = r'(.*\[01/Jul/1995:00:((00:00:[2-5][1-9])|([0-2][0-9]:[1-5]:[0-5][0-9])|([1-2][0-5]:[0-9]:[0-5][0-9])|(06:5[1-2])).*\].\"((POST)|(DELETE)|(PUT)).*\".[^2].*)' \
             r''
    file = open("access_log.txt", 'r')
    temp = 0
    for line in file.readlines():
        if re.search(regexp, line):
            temp += 1
            print(line)
    print(temp)


result()


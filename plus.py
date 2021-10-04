import re
import sys


def test():
    path = sys.argv[1]
    # path = 'E:/大三上/编译原理/pre-词法分析/file.txt'
    content = read_file(path)
    word_list = content.split()
    for word in word_list:
        l = len(word)
        while l > 0:
            k = number(word)
            if k != -1:
                word = word[k:]
                l = len(word)
                continue
            k = identifier(word)
            if k != -1:
                tmp = keyword(word, 0)
                if tmp == -1 or tmp < k:
                    word = word[k:]
                    l = len(word)
                    continue
            k = keyword(word, 1)
            if k != -1:
                word = word[k:]
                l = len(word)
                continue
            k = operate(word)
            if k != -1:
                word = word[k:]
                l = len(word)
                continue
            print('Err')
            return


# 识别标识符
def identifier(input):
    form = re.compile(r'[0-9a-zA-Z_]+')
    result = re.match(form, input)
    if result is None:
        return -1
    else:
        loc = result.span()[1]
        print('Ident(' + input[0:loc] + ')')
        return loc


# 识别无符号整数
def number(input):
    form = re.compile(r'[0-9]+')
    result = re.match(form, input)
    if result is None:
        return -1
    else:
        loc = result.span()[1]
        print('Number(' + input[0:loc] + ')')
        return result.span()[1]


# 识别关键字
def keyword(input, flag):
    if re.match('if', input) is not None:
        if flag == 1:
            print('If')
        return 2
    elif re.match('else', input) is not None:
        if flag == 1:
            print('Else')
        return 4
    elif re.match('while', input) is not None:
        if flag == 1:
            print('While')
        return 5
    elif re.match('break', input) is not None:
        if flag == 1:
            print('Break')
        return 5
    elif re.match('continue', input) is not None:
        if flag == 1:
            print('Continue')
        return 8
    elif re.match('return', input) is not None:
        if flag == 1:
            print('Return')
        return 6
    return -1


# 识别符号
def operate(input):
    if re.match('==', input) is not None:
        print('Eq')
        return 2
    elif re.match('=', input) is not None:
        print('Assign')
        return 1
    elif re.match(';', input) is not None:
        print('Semicolon')
        return 1
    elif re.match('\(', input) is not None:
        print('LPar')
        return 1
    elif re.match('\)', input) is not None:
        print('RPar')
        return 1
    elif re.match('{', input) is not None:
        print('LBrace')
        return 1
    elif re.match('}', input) is not None:
        print('RBrace')
        return 1
    elif re.match('\+', input) is not None:
        print('Plus')
        return 1
    elif re.match('\*', input) is not None:
        print('Mult')
        return 1
    elif re.match('/', input) is not None:
        print('Div')
        return 1
    elif re.match('<', input) is not None:
        print('Lt')
        return 1
    elif re.match('>', input) is not None:
        print('Rt')
        return 1
    return -1


def read_file(filepath):
    with open(filepath) as fp:
        content = fp.read()
    return content


test()

import re
import sys


def test():
    # path = sys.argv[1]
    path = 'E:/大三上/编译原理/pre-词法分析/file.txt'
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
            if k is not None:
                tmp = keyword(word)
                if tmp is None or len(tmp) != len(k):
                    # 不是关键字
                    word = word[len(k):]
                    l = len(word)
                    print("Ident(" + k + ")")
                    continue
                elif len(tmp) == len(k):
                    # 是关键字
                    word = word[len(tmp):]
                    l = len(word)
                    print(tmp)
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
        return None
    else:
        loc = result.span()[1]
        return input[0:loc]


# 识别无符号整数
def number(input):
    form = re.compile(r'[0-9]+')
    result = re.match(form, input)
    if result is None:
        return -1
    else:
        loc = result.span()[1]
        print("Number(" + input[0:loc] + ")")
        return loc


# 识别关键字
def keyword(input):
    if re.match('if', input) is not None:
        return "If"
    elif re.match('else', input) is not None:
        return "Else"
    elif re.match('while', input) is not None:
        return "While"
    elif re.match('break', input) is not None:
        return "Break"
    elif re.match('continue', input) is not None:
        return "Continue"
    elif re.match('return', input) is not None:
        return "Return"
    return None


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

def decode_string(str):
    stack = []
    num, char = 0, ''

    for s in str:
        if s.isdigit():
            num = 10*num + int(s)
        elif s == '[':
            stack.append(char)
            stack.append(num)
            num, char = 0, ''
        elif s == ']':
            new_num = stack.pop()
            new_char = stack.pop()
            char = new_char + char*new_num
        else:
            char = char + s

    return char

s = '3[a2[bc]d]'
print(decode_string(s))
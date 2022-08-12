def nested_prop(s):
    count = 0
    for i in range(len(s)):
        if (s[i] == '{') & (s[-1 - i] == '}'):
            count += 1
        if (s[i] == '[') & (s[-1 - i] == ']'):
            count += 1
        if (s[i] == '(') & (s[-1 - i] == ')'):
            count += 1

    if len(s) / 2 == count:
        num = 1
    else:
        num = 0

    return num


print(nested_prop(''))
print(nested_prop('{[()()]}'))
print(nested_prop('([)()]'))

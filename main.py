s = input()

letter = 0
digit = 0
space = 0
other = 0

i = 0
while i < len(s):
    c = s[i]
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        letter += 1
    elif c >= '0' and c <= '9':
        digit += 1
    elif c == ' ':
        space += 1
    else:
        other += 1
    i += 1

print("英文字符: " + str(letter))
print("数字: " + str(digit))
print("空格: " + str(space))
print("其他字符: " + str(other))

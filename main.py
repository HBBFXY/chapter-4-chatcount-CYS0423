s = input()

letters = 0
digits = 0
spaces = 0
others = 0

i = 0
while i < len(s):
    c = s[i]
    # 检查是否为英文字符
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        letters += 1
    # 检查是否为数字
    elif c >= '0' and c <= '9':
        digits += 1
    # 检查是否为空格
    elif c == ' ':
        spaces += 1
    # 其他字符
    else:
        others += 1
    i += 1

# 严格按照指定格式输出
print("英文字符: " + str(letters))
print("数字: " + str(digits))
print("空格: " + str(spaces))
print("其他字符: " + str(others))

s = input()

# 初始化计数器
letter = 0
digit = 0
space = 0
other = 0

# 遍历每个字符
for i in range(len(s)):
    c = s[i]
    # 检查英文字符
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        letter = letter + 1
    # 检查数字
    elif ord(c) >= ord('0') and ord(c) <= ord('9'):
        digit = digit + 1
    # 检查空格
    elif ord(c) == ord(' '):
        space = space + 1
    # 其他字符
    else:
        other = other + 1

# 输出结果，严格控制格式
print("英文字符: " + str(letter))
print("数字: " + str(digit))
print("空格: " + str(space))
print("其他字符: " + str(other))

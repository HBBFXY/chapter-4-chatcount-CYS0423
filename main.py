# 从键盘输入一行字符
s = input()

# 初始化各类字符计数器
letters = 0  # 英文字符
digits = 0   # 数字
spaces = 0   # 空格
others = 0   # 其他字符

# 遍历每个字符进行统计
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    elif c == ' ':
        spaces += 1
    else:
        others += 1

# 按照要求格式输出结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")

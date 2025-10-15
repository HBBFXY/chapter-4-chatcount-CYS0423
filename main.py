# 读取输入
s = input()

# 初始化计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 遍历每个字符
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
    else:
        others += 1

# 输出结果（使用基础字符串格式化，避免f-string可能的问题）
print("英文字符: %d" % letters)
print("数字: %d" % digits)
print("空格: %d" % spaces)
print("其他字符: %d" % others)

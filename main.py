# 接收用户输入的一行字符
s = input()

# 初始化各类字符的计数器
letter_count = 0  # 英文字符计数
digit_count = 0   # 数字计数
space_count = 0   # 空格计数
other_count = 0   # 其他字符计数

# 遍历每个字符进行分类统计
for char in s:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == ' ':
        space_count += 1
    else:
        other_count += 1

# 按照要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")

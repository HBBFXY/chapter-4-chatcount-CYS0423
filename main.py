# 读取输入字符串
input_str = input()

# 初始化各类字符计数器
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

# 遍历每个字符进行统计
for char in input_str:
    if char.isalpha():  # 判断英文字符（字母）
        letter_count += 1
    elif char.isdigit():  # 判断数字
        digit_count += 1
    elif char.isspace():  # 判断空格
        space_count += 1
    else:  # 其他字符
        other_count += 1

# 严格按照格式输出
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")

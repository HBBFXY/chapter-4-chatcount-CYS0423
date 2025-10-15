# 这个文件用于编写代码
# 初始化各类型字符计数器
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

# 从键盘获取输入
input_str = input("请输入一行字符：")

# 遍历每个字符进行统计
for char in input_str:
    if char.isalpha():  # 判断是否为英文字符（字母）
        letter_count += 1
    elif char.isdigit():  # 判断是否为数字
        digit_count += 1
    elif char.isspace():  # 判断是否为空格
        space_count += 1
    else:  # 其他字符
        other_count += 1

# 按照要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")

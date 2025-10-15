# 字符统计程序
# 从键盘读取一行输入（不添加额外提示，避免影响测试）
line = input()

# 初始化各类字符计数器
letter_count = 0   # 英文字符
digit_count = 0    # 数字
space_count = 0    # 空格
other_count = 0    # 其他字符

# 遍历每个字符进行分类统计
for char in line:
    # 判断是否为英文字母
    if char.isalpha():
        letter_count += 1
    # 判断是否为数字
    elif char.isdigit():
        digit_count += 1
    # 判断是否为空格
    elif char.isspace():
        space_count += 1
    # 其他字符
    else:
        other_count += 1

# 按照要求的格式输出结果，确保与测试解析格式完全匹配
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
    

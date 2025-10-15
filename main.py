#!/usr/bin/env python3
# 字符统计程序
try:
    # 从键盘读取一行输入（不添加额外提示）
    line = input().strip('\n')  # 确保移除可能的换行符

    # 初始化计数器
    letter_count = 0   # 英文字符
    digit_count = 0    # 数字
    space_count = 0    # 空格
    other_count = 0    # 其他字符

    # 遍历每个字符
    for char in line:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    # 严格按照格式输出，确保无多余空格和空行
    print(f"英文字符: {letter_count}")
    print(f"数字: {digit_count}")
    print(f"空格: {space_count}")
    print(f"其他字符: {other_count}", end='')  # 避免最后添加额外换行

except Exception as e:
    # 捕获并输出任何可能的错误，帮助调试
    print(f"程序错误: {str(e)}")

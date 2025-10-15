def main():
    # 从键盘输入一行字符
    text = input()
    
    # 初始化计数器
    english_chars = 0  # 英文字符
    digits = 0         # 数字
    spaces = 0         # 空格
    others = 0         # 其他字符
    
    # 遍历每个字符并统计
    for char in text:
        if char.isalpha():  # 判断是否为字母（包括中英文）
            english_chars += 1
        elif char.isdigit():  # 判断是否为数字
            digits += 1
        elif char.isspace():  # 判断是否为空格
            spaces += 1
        else:
            others += 1
    
    # 输出统计结果，严格按照要求的格式
    print(f"英文字符: {english_chars}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

if __name__ == "__main__":
    main()

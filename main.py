input_str = input("请输入一行字符：")
alpha_count = digit_count = space_count = other_count = 0
for char in input_str:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == ' ':
        space_count += 1
    else:
        other_count += 1
print("英文字符:", alpha_count)
print("数字:", digit_count)
print("空格:", space_count)
print("其他字符:", other_count)

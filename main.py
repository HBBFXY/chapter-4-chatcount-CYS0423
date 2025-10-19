def count_characters(input_string):
    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    return letter_count, digit_count, space_count, other_count

def main():
    input_string = input("请输入一行字符: ")
    letters, digits, spaces, others = count_characters(input_string)
    print(f"英文字符:{letters} 数字:{digits} 空格:{spaces} 其他字符:{others}")

if __name__ == "__main__":
    main()

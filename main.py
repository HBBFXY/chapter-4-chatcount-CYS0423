s = input()

letters = 0
digits = 0
spaces = 0
others = 0

i = 0
n = len(s)
while i < n:
    c = s[i]
    
    # 检查小写字母
    if c >= 'a' and c <= 'z':
        letters = letters + 1
    # 检查大写字母
    elif c >= 'A' and c <= 'Z':
        letters = letters + 1
    # 检查数字
    elif c >= '0' and c <= '9':
        digits = digits + 1
    # 检查空格
    elif c == ' ':
        spaces = spaces + 1
    # 其他字符
    else:
        others = others + 1
        
    i = i + 1

# 输出结果，使用最基础的字符串拼接
print("英文字符: " + str(letters))
print("数字: " + str(digits))
print("空格: " + str(spaces))
print("其他字符: " + str(others))

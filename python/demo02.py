# author: JK
# date: 2023/9/3 16:36
# 转义字符

print('Hello\nWorld')   # \n——newline
print('Hello\tWorld')   # \t——Table
print('Hello\rWorld')   # \r——return
print('Hello\bWorld')   # \b——backspace
print(r'Hello\nWorld')  # 前置r表示使用原字符
# print(r'Hello\nWorld\')   # 字符串最后不能为单一反斜线
print(r'Hello\nWorld\\')
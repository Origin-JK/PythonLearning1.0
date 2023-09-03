# author: JK
# date: 2023/9/3 16:13

#输出数字
print(520)

#输出字符
print('Hello World!')

#输出表达式结果
print(2+3)

#在文件中写内容
fp = open('E:/Python/PythonLearning1.0/python/Data/test01.txt','a+')
print('Hello World!',file = fp)
fp.close()

#在一行中输出
print('Hello','World','!')
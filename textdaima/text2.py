# list1=[1,43,4,4,5,5,634,6,43,1412]
# str_list = ' '.join(str(i) for i in list2)

# import random
# random.seed(10)
# n=100
# num=random.randint(0,n)
# print(num)
# str1='fhqiFGLfhlwfhlf'
# print(str1[-1])

# list1=['fgweg','fafgg','rhtjthe','gherh']
# print(list1[1])

# num=0
# q=0
# list1=[1,2,3,4]
# list2=[]
# for i in list1:
#     for j in list1:
#         for z in list1:
#             if (i!=j)and(j!=z)and(i!=z):
#                 num+=1
#                 q=100*i+10*j+z
#                 list2.append(q)
# print(num)
# print(list2)
# list1=[]
# num=0
# for i in range(101,201):
#     for j in range(2,int(i/2)+1):
#         if i%j==0:
#             break
#     else:
#         num+=1
#         list1.append(i)
# print(num)
# print(list1)
# str1='1465461123465'
# print(str1[-2:])
# print(str1[:-2])
# print()
# dic={'a': 1, 'b': 1, 'c': 2, '(': 4, ')': 4}
# key=list(dic.values())
# value=list(dic.keys())
# print(key)
# # print(value)
# str1=input()
# print(''.join(str1.split()))


# import itertools
 
# # 假设我们要排列的数字是1, 2, 3
# numbers = [1, 2, 3]
 
# # 使用itertools.permutations()生成排列
# permutations = list(itertools.permutations(numbers))
 
# # 打印所有排列
# print(type(permutations))
# for permutation in permutations:
#     print(permutation)


# num=0
# for i in str1:
#     if int(i)%2==0:
#         list2.append(int(i))
#     else:
#         list1.append(int(i))
# num+=len(list2)

# def generate_even_magic_square(n):  
#     if n % 4 != 0:  
#         raise ValueError("n must be a multiple of 4")  
      
#     # 初始化一个n阶的二维列表，所有元素为0  
#     magic_square = [[0 for _ in range(n)] for _ in range(n)]  
      
#     # 填充数字，从左到右，从上到下  
#     num = 1  
#     for i in range(n):  
#         for j in range(n):  
#             magic_square[i][j] = num  
#             num += 1  
      
#     # 修正每个4x4小方阵的对角线数字  
#     for i in range(0, n, 4):  
#         for j in range(0, n, 4):  
#             for x in range(4):  
#                 for y in range(4):  
#                     # 判断当前位置是否在对角线上  
#                     if x == y or x + y == 3:  
#                         complement = n * n + 1 - magic_square[i + x][j + y]  
#                         magic_square[i + x][j + y] = complement  
      
#     # 输出幻方，每个数字后加一个制表符  
#     for row in magic_square:  
#         print('\t'.join(map(str, row)))  
  
# # 输入一个整数n（n为4的整数倍）  
# n = int(input("请输入一个整数n（n为4的整数倍）: "))  
# try:  
#     generate_even_magic_square(n)  
# except ValueError as e:  
#     print(e)



import jieba  
import logging  
import csv  
from collections import Counter  
  
# 屏蔽jieba库系统信息  
jieba.setLogLevel(logging.WARN)  
  
# 定义排除词  
ex = ['不错', '比较', '可以', '感觉', '没有', '我们', '就是', '还是', '非常', '但是', '不过', '有点', '一个', '一般', '下次', '携程', '不是', '晚上', '而且', '他们', '什么', '不好', '时候', '知道', '这样', '这个', '还有', '总体', '位置', '客人', '因为', '如果', '这里', '很多', '选择', '居然', '不能', '实在', '不会', '这家', '结果', '发现', '竟然', '已经', '自己', '问题', '不要', '地方', '只有', '第二天', '酒店', '房间', '虽然']  
  
# 读取评论数据  
def read_comments(filename):  
    comments = []  
    labels = []  
    with open(filename, 'r', encoding='GBK') as f:  
        reader = csv.reader(f)  
        next(reader)  # 跳过标题行  
        for row in reader:  
            label, content = row  
            labels.append(label)  
            comments.append(content)  
    return labels, comments  

# 分词并过滤  
def tokenize_and_filter(content):  
    words = jieba.lcut(content)  
    return [word for word in words if len(word) >= 2 and not word.isdigit() and word not in ex]  
  
# 计算平均评论长度  
def average_length(comments):  
    return round(sum(len(comment) for comment in comments) / len(comments))  
  
# 词频分析  
def word_frequency(comments, label):  
    words = [word for comment in comments if label == comment[0] for word in tokenize_and_filter(comment[1])]  
    return Counter(words).most_common(15)  
  
# 主程序  
def main():  
    filename = 'comment.csv'  
    labels, comments = read_comments(filename)  
      
    n = input('输入n: ')  
      
    if n == '总评':  
        total_comments = len(comments)  
        positive_comments = sum(1 for label in labels if label == '1')  
        negative_comments = sum(1 for label in labels if label == '0')  
        print(f'总评论: {total_comments}')  
        print(f'好评: {positive_comments}')  
        print(f'差评: {negative_comments}')  
    elif n == '平均':  
        print(average_length(comments))  
    elif n == '好评':  
        for word, count in word_frequency(zip(labels, comments), '1'):  
            print(f'{word}: {count}')  
    elif n == '差评':  
        for word, count in word_frequency(zip(labels, comments), '0'):  
            print(f'{word}: {count}')  
    else:  
        print('无数据')  
  
# 运行主程序  
if __name__ == '__main__':  
    main()
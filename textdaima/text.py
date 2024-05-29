#将列表转换为字符串输出list1，print(''.join(list1))


# My_str='13,3152,6574'
# print(My_str[::-1][5:8])      
# print(My_str.split(','))#[1].replace('3','')[::-1])

# list1=[14,145,5,6,6,7,88,5,2,414,3,4,4,6,7,3,2,1,1]
# set1=set(list1)
# for i in list1:
#     print(f'列表{i}')
# for x in set1:
#     print(f'集合{x}')

# from my_package import model1,model2
# print(model1.str_reverse('fhlafhlagh'))
# print(model2.append_to_file('text.txt','fgwALFGHLGF'))


# 使用随机函数randint()，依次向二维列表A和B中增加元素，建立两个长度为5的二维列表A和B。两个列表包含的数据如下：
# A列表：包含子列表 [学号，p成绩，m成绩]，学号为从1开始递增的正整数，成绩为0-100之间的随机整数。
# B列表：包含子列表 [学号，q成绩]，学号为从1开始递增的正整数，成绩为0-100之间的随机整数
# 先需要将A,B两个列表数据进行合并，即将B列表中的‘q成绩’添加到A列表中的相同学号的子列表中。
# 输入一个整数k，将B列表中的'q成绩'插入到A列表相同学号的子列表的k位置上。
# 合并完成后，输出合并后的A列表。
# 注意：为保证生成固定序列，本题需要使用同一个循环结构生成两个随机列表A和B，类似：
# for #######：
#     A列表添加 学号，p成绩，m成绩
#     B列表添加 学号，q成绩
# 输入格式
# 第一行输入整数s，随机种子
# 第二行输入整数p，插入位置
# 输出格式
# 合并后的A列表
# 示例
# 输入：
# 1
# 1
# 输出： 
# [[1, 97, 17, 72], [2, 15, 8, 32], [3, 57, 63, 97], [4, 48, 60, 83], [5, 12, 100, 26]]
#45 2 [[1, 34, 62, 53], [2, 32, 38, 10], [3, 43, 9, 2], [4, 61, 14, 1], [5, 36, 39, 15]]
#2022 1 [[1, 56, 68, 36], [2, 74, 69, 39], [3, 100, 7, 66], [4, 52, 88, 90], [5, 40, 87, 81]]
#8 2 [[1, 29, 48, 47], [2, 16, 90, 24], [3, 5, 17, 10], [4, 31, 26, 64], [5, 51, 3, 82]]
# import random
# num=int(input())
# k=int(input())
# random.seed(num)
# list1=[]
# list2=[]
# for i in range(5):
#     list1.append([i+1,random.randint(0, 100),random.randint(0, 100)])
#     list2.append([i,random.randint(0, 100)])
# for x,j in enumerate(list2):
#     list1[x].insert(k,j[1])
# print(list1)


# 输入两个整数，在这两个整数组成的闭区间范围内生成100个随机整数，并统计出现数据的次数，
#出现0次的数字不输出（而不是输出0）。为满足评测需要，程序必须使用seed函数将随机种子设为10，并使用randint函数生成随机数。
# 输入格式
# 一行当中输入两个整数，以空格间隔。题目保证两个整数从小到大
# 输出格式
# 按照生成随机数从小到大的顺序，每行输出一个生成的整数以及其出现的次数，以空格间隔。
# 示例 1
# 输入:
# 3 5
# 输出:
# 3 36
# 4 39
# 5 25
# import random
# random.seed(10)
# n,m=map(int,input().split())
# list1=[]
# list2=[]
# num=0
# for i in range(100):
#     list1.append(random.randint(n,m))
# list2=sorted(list(set(list1)))
# for z in list2:
#     num=list1.count(z)
#     print(z,num)



# 回文素数是指一个数既是素数又是回文数。例如，131，既是素数又是回文数。 用户输入一个正整数 n , 请你在一行内输出从小到大排列的的前n个回文素数，数字后面用一个空格进行分隔。
# 输入格式
# 输入一个正整数
# 输出格式
# 符合要求的回文素数
# 示例
# 输入：
# 10
# 输出：
# 2 3 5 7 11 101 131 151 181 191 
# def su(num):
#     if num < 2:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
# def hui(num):
#     return str(num) == str(num)[::-1]
# if __name__=='__main__':
#     n = int(input())
#     i=1
#     list1=[]
#     while n:
#         while True:
#             if (su(i) and hui(i)):
#                 list1.append(i)
#                 break
#             i+=1
#         i+=1
#         n-=1
#     print(' '.join(str(i) for i in list1))
        


# 反素数(逆向拼写的素数)是指一个将其逆向拼写后也是一个素数的非回文数。
# 例如：
# 13和31都是素数，且13和31都不是回文数，所以，13和31是反素数。
# 输入一个正整数 n , 请在同一行输出从小到大排列的的前n个反素数，每个数字后面加一个空格。
# 输入格式
# 输入一个正整数
# 输出格式
# 符合条件的反素数
# 示例
# 输入：
# 10
# 输出：
# 13 17 31 37 71 73 79 97 107 113 
# def su(num):
#     if num < 2:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
# def fansu(num):
#     return str(num)[::-1]
# def hui(num):
#     if str(num) == str(num)[::-1]:
#         return False
#     else:
#         return True
# if __name__=='__main__':
#     n = int(input())
#     i=1
#     list1=[]
#     while n:
#         while True:
#             if (su(i) and hui(i) and su(int(fansu(i)))):
#                 list1.append(i)
#                 break
#             i+=1
#         i+=1
#         n-=1
#     print(' '.join(str(i) for i in list1))




# 你从武汉搬到美国生活，这里的人都讲英语，你的英语不好，好在你有一个程序，可以把英语译成中文，帮助你与人沟通。
# （注意：词典文件没有精校，存在部分格式不一致的问题，处理时根据空格切分一次，只把英文和中文解释切分开。）
# 输入
# 输入一个英文句子
# 输出
# 输出英文句子中每个单词的中文意思，每行一个单词，单词字母转小写，"'s" 用 " is"替换，"n't" 用" not" 替换（替换为空格加is或not），
#单词与意义间用空格分隔，当查询的词在文件中不存在时，输出'自己猜'
# 示例 1
# 输入：
# For others, but to live for yourself.
# 输出：
# for 给，作...用的
# others 自己猜
# but 但是，除了
# to 向，到
# live 居住,生存 活的
# for 给，作...用的
# yourself 你(们)自己
# import re
# dic = {}
# with open('dicts.txt','r',encoding = 'utf-8') as f:
#     for x in f:
#         ls1=x.split()
#         dic[ls1[0]]=' '.join(ls1[1:])
# words=''.join(input().split(',')).lower()
# words=words.replace("n't",' not')
# words=words.replace("'s",' is')
# words1=re.sub('[^\w\s]','',words)
# words_list = [word for word in words1.split() if word != ',']
# for j in words_list:
# 	if j in dic:
# 		print(f'{j} {dic[j]}')
# 	else:
# 		print(f'{j} 自己猜')



# 输入一个1000以内的正整数 n,在同一行内输出 [0,n] 之间各位数字之和为5的数，数字之间用空格分开（行末有一个空格）。
# 输入格式
# 输入一个1000以内的正整数 n
# 输出格式
# 在一行内依次输出所有符合条件的数，数字之间用空格分开（行末有一个空格）
# 示例
# 输入：
# 100
# 输出：
# 5 14 23 32 41 50 
# list1=[]
# list2=[]
# def panduan(num):
#     m=0
#     z=len(str(num))
#     list1=list(str(num))
#     for i in range(z):
#         m+=int(list1[i])
#     if m==5:
#         return True
#     else:
#         return False
# n=int(input())
# for j in range(1,n+1):
#     if panduan(j):
#         list2.append(j )
# print(' '.join(map(str,list2)))



# 输入一个正整数，计算其各个位的数字之和
# 输入格式
# 输入一个正整数
# 输出格式
# 输出各位上数字之和
# 示例
# 输入：
# 123    
# 输出：
# 6
# def he(num):
#     m=0
#     z=len(str(num))
#     list1=list(str(num))
#     for i in range(z):
#         m+=int(list1[i])
#     return m
# n=int(input())
# print(he(n))

# n=int(input())
# list1=input().split()
# m=int(input())
# for i in range(m):
#     list2=[]
#     list2=input().split()
#     if list2[0]=='1':
#         list1[int(list2[1])-1]=list2[2]
#     elif list2[0]=='2':
#         for j in range(n):
#             if int(list1[i]) < int(list2[1]):
#                 list1[i]=list2[1]
# print(' '.join(list1))



# 输入一个英文句子，每个单词间用空格分隔，标点符号前面无空格，后面跟一个空格。
#请按出现顺序将每个单词分行输出（标点符号归属于前面的单词）。
# 输入格式
# 一个英文句子
# 输出格式
# 分行依次输出句子中的单词
# 示例
# 输入：
# Never forget to say "thanks".    
# 输出：
# Never
# forget
# to
# say
# "thanks".
# list1=input().split()
# for i in list1:
#     print(i)



# 月份的缩写为月份单词的前3个字母（九月为前4个），且首字母大写，以 '.' 做为缩写结束标记。月份的英文单词及其缩写如下表所示：
# 月份	缩写	单词	月份	缩写	单词
# 一月	Jan.	January	二月	Feb.	February
# 三月	Mar.	March	四月	Apr.	April
# 五月	May.	May	六月	Jun.	June
# 七月	Jul.	July	八月	Aug.	August
# 九月	Sept.	September	十月	Oct.	October
# 十一月	Nov.	November	十二月	Dec.	December
# 编写一个程序，用户输入一个月份单词，不论输入的单词各字符是大写还是小写，请正确输出对应月份的缩写。
#当输入单词拼写错误时，输出“spelling mistake”。
# 提示:
# 字符串有以下方法可用
# str.upper()    转换字符串 str 中所有字母为大写
# str.lower()    转换字符串 str 中所有字母为小写
# str.capitalize()    把字符串 str 的第一个字符大写
# 月份名列表
# month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
#'September', 'October', 'November', 'December']
# 输入格式
# 某月份的英文单词
# 输出格式
# 该月的缩写或“spelling mistake”
# 示例 1
# 输入：
# february    
# 输出：
# Feb.
# 示例 2
# 输入：
# auGust    
# 输出：
# Aug.
# month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# str1=input().capitalize()
# if (str1 in month_lst)and(str1 != 'September'):
#     print(str1[:3]+'.')
# elif str1 not in month_lst:
#     print('spelling mistake')
# elif str1=='September':
#     print(str1[:4]+'.')




# 用户输入一个小于10的正整数n，求1 + 12 + 123 + 1234 + …… 的前n项的和。当输入n大于或等于10时，直接输出“data error!”
# 输入格式
# 一个小于10的正整数
# 输出格式
# 数列的前 n 项和或“data error!”
# 示例
# 输入：
# 5    
# 输出：
# 13715
# n=int(input())
# m=1
# x=1
# num=1
# if 0<n<10:
#     for i in range(n-1):
#         x+=1
#         m*=10
#         m=m+x
#         num+=m
        
#     print(num)
# elif n>=10:
#     print('data error!')



# 输入一个字符串，将其中大写字母转为小写，小写字母转为大写，其他字符保持原样，输出转换后的字符串。
# 输入格式
# 输入一个字符串。
# 输出格式
# 输出转换后的字符串。
# 示例
# 输入：
# "Hello, Python 3.7.4"
# 输出：
# "hELLO, pYTHON 3.7.4"
# str1=' '.join(input().split())
# str2=str1.swapcase()
# print(str2)



# 编写程序，从用户给定字符串中查找某指定的字符。
# 输入格式
# 分两行输入：
# 第一行是一个待查找的字符
# 第二行是一个以回车结束的非空字符串。
# 输出格式
# 如果找到，在一行内按照格式index = 下标输出该字符在字符串中所对应的最小下标（下标从0开始）； 否则输出"Not Found"。
# 示例
# 输入：
# m
# programming    
# 输出：
# index = 6
# m=input()
# z=input()
# for x,i in enumerate(z):
#     if i==m:
#         print(f'index = {x}')
#         break
# else:
#     print('Not Found')



# 某电商平台开发出一个新功能：友谊验真器。“是不是朋友，帮忙砍一刀！” 一件商品价格为 price 元，假设每位朋友帮忙砍价都是整数，
#最少可以砍掉0元，最多只能砍掉不超过商品标价十分之一的价钱，请问每件商品至少要多少人帮忙砍价才能0元拿？
# 本题使用random函数库，要求使用random.randint()函数生成每次砍价的整数金额
# 输入格式
# 在一行中输入用逗号分隔的2个正整数，分别代表商品标价和随机数种子
# 输出格式
# 砍价到0元的最少次数
# 示例
# 输入：
# 100,10
# 输出：
# 22
# import random
# n,m=map(int,input().split(','))
# random.seed(m)
# q=int(n/10)
# j=0
# while n>=0:
#     num=int(random.randint(0,q))
#     n-=num
#     j+=1
# print(j)



# 从字符串 '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\\()*+,-.' 中每次随机抽取 1 个字符,
#重复 n 次，用取得的字符构成的一个新字符串用做密码，密码长度 n 和随机数种子 s 由用户输入。
# 本题必须使用random.choice()函数进行随机抽取
# 输入格式
# 在一行内输入2个正整数 n 和 s，分别表示密码长度和随机数种子，数字间用半角逗号分隔。
# 输出格式
# 一个长度为 n 字符串
# 示例
# 输入：
# 10,5
# 输出：
# wJ&3Xv6keL
# import random
# str1='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\\()*+,-.'
# n,s=map(int,input().split(','))
# random.seed(s)
# list1=[]
# for i in range(n):
#     list1.append(random.choice(str1))
# print(''.join(list1))



# 微软产品一般都一个25位的序列号，是用来区分每份微软产品的产品序列号。产品序列号由五组被“-”分隔开，由字母数字混合编制的字符串组成，
#每组字符串是由五个字符串组成。如： 36XJE-86JVF-MTY62-7Q97Q-6BWJ2 
# 序列号中每个字符是取自于以下24个字母及数字之中的一个： B C E F G H J K M P Q R T V W X Y 2 3 4 6 7 8 9 。
#采用这24个字符的原因是为了避免混淆相似的字母和数字，如I 和1，O 和0等，避免产生不必要的麻烦。 
# 请编写程序，根据用户输入的个数和随机数种子，随机生成相应个数的序列号并输出。
# 随机数种子函数语法为：random.seed(n)
# 本题要求应用random.choice()方法每次获得一个随机字符！！！
# 输入格式
# 分两行中依次输入：
# 第一行输入一个正整数，代表要生成的序列号的个数
# 第二行输入一个正整数，代表随机数种子
# 输出格式
# 分行依次输出指定个数的序列号
# 示例
# 输入：
# 2
# 10
# 输出：
# 3CVX3-BJWXM-6HCYX-QEK9R-CVG4R
# TVP7M-WH7P7-RGWKW-4TC3B-KGJP2
# import random
# str1='BCEFGHJKMPQRTVWXY2346789'
# n=int(input())
# s=int(input())
# random.seed(s)
# for i in range(n):
#     list1=[]
#     for j in range(1,30):
#         if j%6==0:
#             list1.append('-')
#         else:
#             list1.append(random.choice(str1))
#     print(''.join(list1))
#     list1.clear()
        


# 本关任务：编写一个能换算薪资范围的小程序。
# 相关知识
# 为了完成本关任务，你需要掌握：
# 1.字符串切分
# 2.索引
# 3.eval()
# 字符串切分
# 字符串的split()方法用于将字符串切分为列表
# 索引
# 有序列后加一个方括号，用序号可以获取序列中对应位置的一个元素。
# eval()
# eval()可以将字符串转为python支持的数据类型
# eval('[1,2,3,4]') 可得到列表[1,2,3,4]
# 编程要求
# 某公司招聘时，人力资源部给出的薪资标准如下：
# "'薪资': ['5-8千/月', '8-10千/月', '10-15千/月', '15-25千/月', '25-50千/月']"
# 请将其换算为以元为单位的月薪，并参考示例数据的格式输出不同级别的薪资表。
# 测试说明
# 测试输入：
# 1
# 预期输出：
# 1级员工月薪范围5000-8000元
# salary_str = "'薪资': ['5-8千/月', '8-10千/月', '10-15千/月', '15-25千/月', '25-50千/月']"
# list1=eval(salary_str[6:])
# list2=[]
# list2.append(list1[0][0]+'000-'+list1[0][2]+'000')
# list2.append(list1[1][0]+'000-'+list1[1][2:4]+'000')
# list2.append(list1[2][:2]+'000-'+list1[2][3:5]+'000')
# list2.append(list1[3][:2]+'000-'+list1[3][3:5]+'000')
# list2.append(list1[4][:2]+'000-'+list1[4][3:5]+'000')
# n=eval(input())
# print(f'{n}级员工月薪范围{list2[n-1]}元')



# 18位身份证号码第7 ~ 10位为出生年份(四位数)，第11 ~ 12位为出生月份，第13 ~ 14位代表出生日期，
#第17位代表性别，奇数为男，偶数为女。 用户输入一个合法的身份证号，请输出用户的出生年月日和性别。（不要求较验输入的合法性）
# 输入格式
# 输入一个合法的身份证号字符串
# 输出格式
# 类似以下格式输出：
# 出生：1995年11月11日
# 性别：女
# 示例 1
# 输入：
# 110111199511111101  # 210203197503102721  
# 输出：
# 出生：1995年11月11日
# 性别：女
# str1=input()
# list1=[]
# list1.append(str1[6:10])
# list1.append(str1[10:12])
# list1.append(str1[12:14])
# num=int(str1[16])
# if num%2==0:
#     list1.append('女')
# else:
#     list1.append('男')
# print(f'出生：{list1[0]}年{list1[1]}月{list1[2]}日')
# print(f'性别：{list1[3]}')



# 编写一个美元与人民币转换的程序，用户输入金额和汇率（合理的汇率是正数），输出转换为另一种货币表示的金额。
# 美元:'$'
# 人民币:'¥'
# 货币标识可从上述描述中复制
# 输入格式
# 第一行输入一个以货币符号结尾的正数，数值作为金额，货币符号表明货币种类
# 第二行输入一个浮点数作为汇率
# 输出格式
# 输入符合要求时输出一个带货币符号的数值（保留2位小数）
# 输入不符合要求时输出“Data error!”
# 示例 1
# 输入：
# 58$
# 6.75
# 输出：
# 391.50¥
# 示例 2
# 输入：
# 100¥
# 6.85
# 输出：
# 14.60$
# 示例 3
# 输入：
# 58
# 6.75
# 输出：
# Data error!
# 725$
# -7.2
# str1=input()
# n=eval(input())
# num=0
# if (eval(str1[:-1])<=0)or(n<=0):
#     print('Data error!')
# else:
#     if str1[-1]=='$':
#         num=n*eval(str1[:-1])
#         print(f'{num:.2f}¥')
#     elif str1[-1]=='¥':
#         num=eval(str1[:-1])/n
#         print(f'{num:.2f}$')
#     else:
#         print('Data error!')



# 用户输入自己的个人信息，格式如下：
# 0122923450321 王昊 法学1801 河北 2001年
# 数据分别表示：学号 姓名 专业班级 籍贯 出生年份，各数据间空格间隔
# 有些用户没有按照规则输入数据，输入自己出生年份的时候写成了类似‘1900年生’或‘出生于1985’或‘19岁生于2006年11月’的数据格式。
#请注意程序此时仍然需要正确读取该项数据，本题保证这些用户输入时一定只含有1个4位数字连续组成的年份数据。
# 请按照输出样式输出姓名，班级，出生年份。
# 提示：
# 列表中的数据和字符串当中的字符一样，都具有有序的索引，且引用数据和切片方式一致。
# str.isdigit()可以帮助判断字符串是否全部由数字字符组成，返回值为'True'或'False'
# 输入格式
# 按如下示例，在一行内依次输入5个字符串，分别表示：学号 姓名 专业班级 籍贯 出生年份，各数据间空格间隔
# 0122923450321 王昊 法学1801 河北 2001年
# 输出格式
# 按如下示例，分行依次输出姓名，班级，出生年份
# 姓名：王昊
# 班级：法学1801
# 出生：2001年
# 示例
# 输入：
# 0122923450321 王昊 法学1801 河北 2001年
# 输出：    
# 姓名：王昊
# 班级：法学1801
# 出生：2001年
#0122923450511 赵武 材料1501 湖北 1998年11月20日
# list1=input().split()
# str1=''.join([i for i in list1[4] if i.isdigit()])
# print(f'姓名：{list1[1]}')
# print(f'班级：{list1[2]}')
# if len(str1)!=4:
#     str2=str1[:-4]
#     print(f'出生：{str2}年')
# else:
#     print(f'出生：{str1}年')



# 中国目前采用的是18位身份证号，其第7-10位数字是出生年，11-12位是出生月份，13-14是出生日期，第17位是性别，奇数为男性，偶数为女性，
#第18位是校验位。 如果身份证号码的其中一位填错了（包括最后一个校验位），则校验算法可以检测出来。
#如果身份证号的相邻2位填反了，则校验算法可以检测出来。校验规则如下：
# 将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2
# 将这17位数字和系数相乘的结果相加
# 用加出来和除以11，看余数只可能是：0－1－2－3－4－5－6－7－8－9－10 分别对应的最后一位身份证的号码为：1－0－X－9－8－7－6－5－4－3－2
# 通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的X（大写英文字母X）。如果余数是10，身份证的最后一位号码就是2。
# 用户输入一个身份证号，需校验其是否是合法的身份证号码，包括:
# 输入长度是否合法
# 输入数据校验位是否合法
# 输入数据中年月日范围是否合法，考虑闰年
# 如身份证号码不合法输出 '身份证校验错误'， 如身份证号码合法则分别在3行中输出'身份证号码校验为合法号码'以及该人的出生年月日和性别。
# 输入格式
# 一个18位身份证号，末位为数字或大写字母X
# 输出格式
# 如身份证号码不合法输出 '身份证校验错误'， 如身份证号码合法则分别在3行中输出'身份证号码校验为合法号码'以及该人的出生年月日和性别。
#（月份和日期均为2位数表示）
# 示例 1
# 输入:    
# 432831196411150810
# 220221197305166534
# 输出:
# 身份证号码校验为合法号码
# 出生：1964年11月15日
# 性别：男
# 示例 2
# 输入:
# 432831196811150810
# 220221200504450030
# 输出:
# 身份证校验错误
# def Year(year):
#     if (year%4==0 and year%100!=0)or(year%400==0):   return 'T'
#     else:   return 'F'
# def mo(a,b):
#     if a=='T' and b<=29:
#         return True
#     elif a=='F' and b<=28:
#         return True
#     else:   return False
# def panduan(str2,list7,list8):
#     num=0
#     m=0
#     for i in range(17):
#         num+=int(str2[i])*int(list7[i])
#     m=int(num%11)
#     if str2[-1]==list8[m]:
#         return True
#     else:
#         return False
# def xinbie(nm):
#     if nm%2==0:
#        return '女'
#     else:
#         return '男'
# def riqi(month,day):
#     if ((month==1)or(month==3)or(month==5)or(month==7)or(month==8)or(month==10)or(month==12))and(0<day<=31)and(0<month<=12):
#         return True
#     elif ((month==2)or(month==4)or(month==6)or(month==9)or(month==11))and(0<day<=30)and(0<month<=12):
#         return True
#     else:    return False
# list7=['7','9','10','5','8','4','2','1','6','3','7','9','10','5','8','4','2']
# list8=['1','0','X','9','8','7','6','5','4','3','2']
# if __name__=='__main__':
#     list1=[]
#     str1=input()
#     if len(str1)!=18:
#         print('身份证校验错误1')
#     else:
#         list1.append(str1[6:10])
#         list1.append(str1[10:12])
#         list1.append(str1[12:14])
#         if (list1[1]=='02')and(mo(Year(int(list1[0])),int(list1[2]))):
#            if panduan(str1,list7,list8):
#                print('身份证号码校验为合法号码')
#                print(f'出生：{list1[0]}年{list1[1]}月{list1[2]}日')
#                nm=int(str1[16])
#                str3=xinbie(nm)
#                print(f'性别：{str3}')
#            else:
#                print('身份证校验错误31')
#         elif list1[1]!='02' and riqi(int(list1[1]),int(list1[2])):
#             if panduan(str1,list7,list8):
#                print('身份证号码校验为合法号码')
#                print(f'出生：{list1[0]}年{list1[1]}月{list1[2]}日')
#                nm=int(str1[16])
#                str3=xinbie(nm)
#                print(f'性别：{str3}')
#             else:
#                print('身份证校验错误32')
#         else:
#             print('身份证校验错误2')



# 密码对照表的构造方法为：
# 第一行为明码行，放置大写字母表（如下表第一行所示。）
# 第二行为按照以下规则生成的密码行：
# 给定一个单词，将单词中所有字符转为大写字母，对于单词中重复出现的字母，保留第一次出现的，删除之后重复出现的该字符
# 用剩余字母组成秘钥从密码行的开始位置放置
# 再用未在秘钥中出现的其他大写字母按字母表顺序依次填充密码行剩余位置
# 例如：给定单词“HelloPython”，所有字符转为大写字母并删除其中重复出现字母后得到秘钥“HELOPYTN”，将秘钥依次填入密码行最开始的位置，
#再用未在秘钥中出现的其他大写字母按字母表顺序依次填充密码行的剩余位置，最终得到密码行（如下的第二行所示） 
# 密码对照表
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# HELOPYTNABCDFGIJKMQRSUVWXZ
# 现要求分两行依次输入两个字符串：其中第一个字符串做秘钥，用于构造明码密码对照表；第二个字符串，将其中所有字母转为大写字母，
#依照明码密码对照表对其做加密处理。最终输出加密后的密文字符串。
# 输入格式
# 输入分两行依次输入两个字符串：
# 输入一个字符串做秘钥
# 输入一个需要加密的符串
# 输出格式
# 输出加密后的密文字符串
# 示例 1
# 输入：
# HelloPython
# GONE WITH THE WIND
# 输出：
# TIGP VARN RNP VAGO
# 示例 2
# 输入：
# GonewiththeWind
# Directed by Victor Fleming
# 输出：
# EDPWNRWE OY UDNRKP ICWFDJT
# str10='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# str11=''
# list2=[]
# list4=[]
# list1=list(input().upper())
# list3=list(input().upper().replace(' ','1'))
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# for j in range(26):
#     if str10[j] not in list2:
#         list2.append(str10[j])
#     if len(list2)==26:
#         break
# for z in list3:
#     if z=='1':
#         list4.append('1')
#     else:
#         for x,n in enumerate(str10):
#             if z==n:
#                 list4.append(list2[x])
#             else:
#                 continue
# str1=(''.join(list4)).replace('1',' ')
# print(str1)



# 用户在一行中输入一个包括大小写字母和数字的字符串，编程实现字符串加密。加密规则如下：
# 将字符串中的大写字母用字母表中该字母后的第5个字母替代
# 将字符串中的小写字母用字母表中该字母后的第3个字母替代
# 字符串中的其他字符原样输出
# 输入格式
# 输入一个至少包含一个字母的字符串
# 输出格式
# 输出加密后的字符串
# 示例 1
# 输入：
# Life is short, you need Python!    
# 输出：
# Qlih lv vkruw, brx qhhg Ubwkrq!
#'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# list1=list(input())
# list2=[]
# for i in list1:
#     if 'a'<=i<='w':
#         list2.append(chr(ord(i)+3))
#     elif 'w'<i<='z':
#         list2.append(chr(ord(i)+3-26))
#     elif 'A'<=i<='U':
#         list2.append(chr(ord(i)+5))
#     elif 'U'<i<='Z':
#         list2.append(chr(ord(i)+5-26))
#     else:
#         list2.append(i)
# print(''.join(list2))



# 在两行中分别输入一个字符串s和一个整数n，定义一个函数将字符串s循环移动n位。其中，n为正数时，循环向右移动n位；
#n为负数时，循环向左移动n位。
# 若s为空字符串''，则不论n为多少，均输出空字符串''。
# 如 s='123456'    n=3
# 输出结果：456123
# 代码框架如下：
#  def f(s,n):
#     ......
# s=input()
# n=int(input())
# print(f(s,n))
# 输入格式
# 输入分两行输入，第一行输入一个字符串，第二行输入一个整数n
# 输出格式
# 输出循环移位后的字符串
# 示例 1
# 输入：
# 123456
# 2
# 输出：    
# 561234
# 示例 2
# 输入：
# 123456
# -2
# 输出：    
# 345612
# def f(s,n):

#     if n>=0:
#         return(s[-n:]+s[:-n])
#     elif n<0:
#         n=-1*n
#         return(s[n:]+s[:n])
# if __name__=="__main__":
#     str1=input()
#     n=int(input())
#     if str1=='':
#         print('')
#     else:
#         m=n%len(str1)
#         print(f(str1,m))



# 输入一个字符串s，s由若干个非数字的字符组成，且相同的字符保证连续排列，将字符串按照下列规则进行长度压缩：
# 将字符放前面，出现次数放后面，如果仅出现1次，则不需要保存次数
# 按照字符在s中出现的顺序输出压缩后的字符串.
# 输入格式
# 输入一个字符串
# 输出格式
# 如果输入字符串中有数字字符，直接输出‘ERROR’；否则分四行依次输出：
# 第一行以字典形式输出字符及其出现次数，键值对为字符: 出现次数
# 第二行输出原字符串的长度
# 第三行输出压缩后的字符串
# 第四行输出压缩后字符串的长度
# 示例 1
# 输入:    
# abcc(((())))
# 输出:    
# {'a': 1, 'b': 1, 'c': 2, '(': 4, ')': 4}
# 12
# abc2(4)4
# 8
# 示例 2
# 输入:    
# abbc&&+++
# 输出:    
# {'a': 1, 'b': 2, 'c': 1, '&': 2, '+': 3}
# 9
# ab2c&2+3
# 8
# 示例 3
# 输入:
# ab1
# 输出:    
# ERROR
# def panduan(str2):
#     for j in str1:
#         if '0'<=j<='9':
#             return True
#     else:
#         return False
# str1=input()
# if panduan(str1):
#     print('ERROR')
# else:
#     dic1={}
#     for i in str1:
#         if i in dic1:
#             dic1[i]+=1
#         else:
#             dic1[i]=1
#     key=list(dic1.keys())
#     value=list(dic1.values())
#     list2=[]
#     for x,i in enumerate(value):
#         if i==1:
#             list2.append(str(key[x]))
#         else:
#             list2.append(str(key[x]))
#             list2.append(str(value[x]))
#     str3=''.join(list2)
#     print(dic1)
#     print(len(str1))
#     print(str3)
#     print(len(str3))



# 字符串的基本操作
# 操作符	描述
# s + t	拼接两个序列 s 和 t
# s * n 或n * s	将序列s重复n次生成新序列
# s[i]	索引，返回序列s的第i项
# s[start:end[:step]]	切片，返回序列 s 从start到end （不包括end ）的步长为step的字符生成新的序列，
#step缺省时，步长为1，返回序号从start到end的子序列。
# len(s)	返回序列s的长度（包含元素的个数）
# min(s,*[,key, default])	返回序列 s的最小值，key关键字缺省时按元素值比较
# max(s,*[,key, default])	返回序列 s的最大值，key关键字缺省时按元素值比较
# s.count(x)	序列s中x的个数
# s.index(x[, i[, j]])	序列中第一个x的索引值，i值表示从索引i处开始查找x，j表示x查找范围在i和j之间。
# x in s	如果序列x与序列s中的任一子序列相等，返回True，否则返回False；当x与s的元素相等时返回True，否则返回False。
# x not in s	如果序列x与序列s中的任何子序列都不相等，返回True，否则返回False
# 请参考上表，根据注释的要求完成模板程序。
# 输入格式
# 1001
# 小明
# 4
# 走路
# 输出格式
# 1001小明
# 小明小明小明小明小明
# 走
# 人可走，就有个路法
# 法方路走个一有是就也，路走以可都人
# 17
# 13
# 2
# 4
# True
# 示例
# 无

# id = input()    # 输入学号
# name = input()  # 输入姓名

# # 输出学号姓名，中间无空格
# print(f'{id}{name}')
# # 重复输出姓名5遍，中间无空格
# list1=[]
# for i in range(5):
#     list1.append(name)
# print(''.join(list1))

# s = '人都可以走路，也就是有一个走路方法'  # '走'的序号为4
# n = int(input())  # 接收一个整数输入n

# # 输出字符串s中序号为n的字符
# print(s[n])
# # 输出字符串s中序号为偶数的字符
# list2=[]
# for x,j in enumerate(s):
#     if x%2==0:
#         list2.append(j)
# print(''.join(list2))
# # 将字符串逆序输出
# print(s[::-1])
# # 输出字符串s的长度
# print(len(s))
# # 输出字符串s中从序号n到字符串结尾包含的字符个数（包括序号为n的字符）
# print(len(s[n:]))
# # 输出字符串s中子字符串‘走路’的个数
# str1=s.split('走路')
# print(len(str1)-1)
# # 输出字符串s中字符‘走’第一次出现的位置序号
# for x,z in enumerate(s):
#     if z=='走':
#         print(x)
#         break

# test = input()          # 输入一个字符串

# # 测试test是否在s中存在，输出测试的结果
# if test in s: 
#     print('True')
# else:
#     print('False')
 

# 我国高铁一等座车座席采用2+2方式布置,每排设有“2+2”方式排列四个座位,以“A、C、D、F”代表,字母“A”和“F”的座位靠窗,
#字母“C”和“D”靠中间走道。 二等座车座席采用2+3布置,每排设有“3+2”方式排列五个座位,以“A、B、C、D、F”代表,
#字母“A”和“F”的座位靠窗,字母“C”和“D”靠中间走道,“B”代表三人座中间座席。每个车厢座位排数是1-17，字母不区分大小写。
# 用户输入一个数字和一个字母组成的座位号，根据字母判断位置是窗口、过道还是中间座席，输入不合法座位号时输出'输入错误'。
# 输入格式
# 输入一个数字和字母组合成的字符串
# 输出格式
# '窗口'、'过道'、'中间' 或'输入错误'
# 示例 1
# 输入：
# 12F
# 输出：
# 窗口
# 示例 2
# 输入：
# 2C
# 输出：
# 过道
# 以下函数可以用于测试输入的座位是否合法，取消注释可以调用此函数
# def seat_numbers(seat):
#     """判定座位是否合法，参数为座位号，返回布尔值"""
#     try:
#         if 1 <= int(seat[:-1]) <= 17 and seat[-1] in 'AaBbCcDdFf':
#             return True
#         else:
#             return False
#     except:
#         return False
# if __name__=='__main__':
#     str1=input().upper()
#     if seat_numbers(str1):
#         if str1[-1]=='A' or str1[-1]=='F':
#             print('窗口')
#         elif str1[-1]=='C' or str1[-1]=='D':
#             print('过道')
#         elif str1[-1]=='B':
#             print('中间')
#     else:
#         print('输入错误')


# 小明在武汉理工大学读书，学校的wifi密码是楼栋号的房间号次幂的前16位的16进制表示，且其中字母均为大写。
#本项目就带你一步一步的破解这个密码。
# 本关任务：编写一个能计算整数的整数次幂的小程序。
# 相关知识
# 为了完成本关任务，你需要掌握：
# 1.幂运算函数
# 幂运算函数
# 内置函数pow(base, exp[, mod])
# 返回 base 的 exp 次幂；如果 mod 存在，
#则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）。 
# 两参数形式 pow(base, exp) 等价于乘方运算符: base**exp。
# print(pow(2,10))
# 输出：
# 1024
# 编程要求
# 根据提示，在右侧编辑器补充代码，输入楼栋号和房间号，计算并输出楼栋号的房间号次幂。
# 测试说明
# 平台会对你编写的代码进行测试：
# 测试输入：
# 4    # 4号楼
# 102  # 102号房间
# 预期输出：
# 25711008708143844408671393477458601640355247900524685364822016
# n=int(input())
# m=int(input())
# z=int(input())
# str1=str(pow(n,m))[:z]
# num1=hex(int(str1))
# print(str(num1).upper()[2:])



# 本关任务：读取附件中的文件，统计文件中大写字母、小写字母、数字、空白字符和其他字符的数量。
# 输出格式
# 文件中大写字母、小写字母、数字、空白字符和其他字符的数量；
# 相关知识
# Python 读取文件
# 读取文件中的内容为字符串可以用以下函数实现：
# # 读文件，返回字符串  
# def read_file(file):  
#     with open(file, 'r', encoding='utf-8') as f:  
#         return f.read()
# Python 常用字符串内建函数
# string.capitalize()  把字符串的第一个字符大写；
# string.count(str, beg=0, end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数；
# string.decode(encoding='UTF-8', errors='strict') 用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”；
#  string.encode(encoding='UTF-8', errors='strict') 用于将 str 类型的数据转换为 byte 二进制数据，这个过程也称为“编码”；
# string.find(str, beg=0, end=len(string)) 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 -1；
# string.format() 格式化字符串；
#  string.isalnum() 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False；
# string.isalpha() 如果 string 至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False；
# string.isdecimal() 如果 string 只包含十进制数字则返回 True 否则返回 False；
# string.isdigit() 如果 string 只包含数字则返回 True 否则返回 False；
#  string.islower() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False；
# string.isnumeric() 如果 string 中只包含数字字符，则返回 True，否则返回 False；
# string.isspace() 如果 string 中只包含空格，则返回 True，否则返回 False；
# string.isupper() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False；
# string.join(seq) 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串；
# string.ljust(width) 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串；
# string.lower() 转换 string 中所有大写字符为小写；
# string.lstrip() 截掉 string 左边的空格；
# max(str) 返回字符串 str 中最大的字母；
# min(str) 返回字符串 str 中最小的字母；
# string.replace(str1, str2,  num=string.count(str1)) 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次；
# string.rstrip() 删除 string 字符串末尾的空格；
# string.split(str="", num=string.count(str)) 以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+1 个子字符串；
# string.startswith(obj, beg=0,end=len(string)) 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查；
# string.swapcase() 翻转 string 中的大小写；
# string.upper() 转换 string 中的小写字母为大写。
# # 统计大写字母、小写字母、数字、空格和其他字符的数量  
# def classify_char(txt):  
#     upper, lower, digit, space, other = 0, 0, 0, 0, 0  
#     for ch in txt:  
#         if ch.islower():  
#             lower = lower + 1  
#         elif ch.isupper():  
#             upper = upper + 1  
#         elif ch.isnumeric():  
#             digit = digit + 1  
#         elif ch.isspace():  
#             space = space + 1  
#         else:  
#             other = other + 1  
#     return upper, lower, digit, space, other 
# 编程要求
# 本项目文件下载：
# mayun.txt
# 在右侧编辑器补充代码，具体要求如下：
# 读取本地的 mayun.txt 文件，返回字符串，文件存放路径为 mayun.txt；
# 分类统计文件中大写字母、小写字母、数字、空白字符（包括空格、\n、\t 等，可用 isspace() 方法判断）和其他字符的数量
# 测试说明
# 平台会对你编写的代码进行测试：
# 预期输出：
# 16 306 11 84 17
# import string
# # 读文件，返回字符串  
# def read_file(file):  
#     # 补充你的代码
#     with open(file,'r',encoding='utf-8') as f:
#         return f.read()
# # 返回大写字母、小写字母、数字、空格和其他字符的数量  
# def classify_char(txt):  
#     # 补充你的代码
#     upper, lower, digit, space, other = 0, 0, 0, 0, 0  
#     for i in txt:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#         elif i.isnumeric():
#             digit+=1
#         elif i.isspace():
#             space+=1
#         else:
#             other+=1
#     return upper, lower, digit, space, other
# if __name__ == '__main__':  
#     filename = 'mayun.txt'  # 读取的文件名  
#     text = read_file(filename)  # text为字符串  
#     print(text)
#     print(*classify_char(text))  
# import string
# # 读文件，返回字符串  
# def read_file(file):  
#     with open(file, 'r', encoding='utf-8') as f:  
#         return f.read()
# def offset_cal(day):  
#     """用字符串中字符ASCII值的和对26取模为偏移量  """
#     sum_of_ch = 0  
#     for c in day:  
#         sum_of_ch = sum_of_ch + ord(c)  
#     offset = sum_of_ch % 26  
#     return offset
# def kaisa(txt, number):  
#     # 补充你的代码
#     for i in txt:
#         if 'a'<=i<='z':
#             if (ord(i)+number)<=122:
#                 list2.append(chr(ord(i)+number))
#             else:
#                 list2.append(chr(ord(i)+number-26))
#         elif 'A'<=i<='Z':
#             if (ord(i)+number)<=90:
#                 list2.append(chr(ord(i)+number))
#             else:
#                 list2.append(chr(ord(i)+number-26))
#         else:
#             list2.append(i)
#     return ''.join(list2)
# list2=[]
# if __name__ == '__main__':  
#     filename = 'mayun.txt'  # 读取的文件名  
#     text = read_file(filename)  # text为字符串  
#     secret_word = input()  
#     offset_number = offset_cal(secret_word)  
#     print(kaisa(text, offset_number))  




# 本关任务：编写一个能输出九宫图的小程序。
# 相关知识
# 为了完成本关任务，你需要掌握：
# 1.创建空的二维列表
# 2.修改二维列表元素值
# 创建特定值的二维列表
# 字符串的split()方法可以将字符串切分为列表。
# # 构造元素为0的二维列表
# print([[0 for i in range(3)] for j in range(3)])
# # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
# 修改二维列表元素值
# 二维列表可以通过索引为每个位置上的元素赋值或修改其值
# 示例如下：
# lst[x][y] = num  # 为列表元素赋值
# 幻方不限于3阶，当n为奇数时，可用以下的方法来填数。
#（1）将1填入第一行的中间； 
#（2）将每一个数字依次放在前一个数的右上方一格（行号减1列号加1）。
# i)出现越界。如果这个数所要放的格已经超出了第一行，那么就把他放在最后一行，仍然放在右一列（列号加1，参考数字“2”）。
# 如果这个数所要放的格已经超过最右列，那么就把他放在最左列的上面一行（行号减1，参考数字“57”）。
# ii）没越界，如果这个数所要放的格已经有数了，此时将其填在这个数的正下方一格（行号加1列号不变，参考数字“10”）。 
#（3）矩阵的最右上方的格子（第一行最后一列）中数的下一个数填在这个数的正下方一格（参考数字“46”）。
# 编程要求
# 输入一个奇数n，输出n阶奇数幻方数。
# 测试说明
# 平台会对你编写的代码进行测试：
# 测试输入：
# 3
# 预期输出：
# 8 1 6
# 3 5 7
# 4 9 2
# n=int(input())
# list1=[[0 for i in range(n)] for j in range(n)]
# num=1
# m,j=0,n//2   #m为行,j为列
# # for a in range(n):
# #     for b in range(n):
# #         num+=1
# for c in range(n*n):
#     # print(' '.join(list1[n]))
#     if c==0:
#         list1[m][int(j)]=str(num)
#         num+=1
#     else:
#         if (0<=m-1<=n-1) and (0<=j+1<=n-1):
#             if list1[m-1][j+1]==0:
#                 m-=1
#                 j+=1
#                 list1[m][j]=str(num)
#                 num+=1
#             else :
#                 m+=1
#                 list1[m][j]=str(num)
#                 num+=1
#         elif m-1<0 and 0<=j+1<=n-1:
#             m=n-m-1
#             j+=1
#             list1[m][j]=str(num)
#             num+=1
#         elif j+1>n-1 and 0<=m-1<=n-1:
#             m-=1
#             j=n-j-1
#             list1[m][j]=str(num)
#             num+=1
#         elif m==0 and j==n-1:
#             m+=1
#             list1[m][j]=str(num)
#             num+=1
# for row in list1:
#     print(' '.join(row))


# 本关任务：编写一个能输出九宫图的小程序。
# 相关知识
# 为了完成本关任务，你需要掌握：
# 1.创建空的二维列表
# 2.修改二维列表元素值
# 创建特定值的二维列表
# 字符串的split()方法可以将字符串切分为列表。
# # 构造元素为0的二维列表
# print([[0 for i in range(3)] for j in range(3)])
# # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
# 修改二维列表元素值
# 二维列表可以通过索引为每个位置上的元素赋值或修改其值
# 示例如下：
# lst[x][y] = num  # 为列表元素赋值
# 4阶幻方的填法：将数字从左到右、从上到下按顺序填写：
# 将对角线上的数字，换成与它互补的数字。
# 把1换成17-1 = 16；
# 把6换成17-6 = 11；
# 把11换成17-11 = 6
# ……
# 换完后就是一个四阶幻方。
# 对于n=4k阶幻方，先把数字按顺序填写。把它划分成kk个44的方阵。
# 然后把每个小方阵的对角线，象制作4阶幻方的方法一样，对角线上的数字换成互补的数字，就构成幻方。 
# 下图以8阶幻方为例：
# (1) 先把数字按顺序填。然后，按44把它分割成2*2个小方阵
# (2) 每个小方阵对角线上的数字，换成和它互补的数。
# 编程要求
# 输入一个整数n(n为4的整数倍)，输出n阶偶数幻方数。
# (每个输出的数字后面用一个制表符分隔)
# 测试说明
# 平台会对你编写的代码进行测试：
# 测试输入：
# 4
# 预期输出：
# 16    2    3    13    
# 5    11    10    8    
# 9    7    6    12    
# 4    14    15    1   
# n=int(input())
# list1=[[0 for i in range(n)] for j in range(n)]
# num,nu=1,0
# for i in range(n):
#     for j in range(n):
#         list1[i][j]=num
#         num+=1
# for i in range(0,n,4):
#     for j in range(0,n,4):
#         for x in range(4):
#             for y in range(4):
#                 if x+y==3 or x==y:
#                     c1=n*n-list1[i+x][j+y]+1
#                     list1[i+x][j+y]=c1
# for i in list1:
#     print("\t".join(map(str,i)))


# 二维列表可以通过索引为每个位置上的元素赋值或修改其值
# 示例如下：
# lst[x][y] = num  # 为列表元素赋值
# 4n+2阶可以看做2（2n+1）,这样一来就转化成了四个求解2n+1阶幻方。
# 下面以6阶幻方为例(4n+2=6，n=1)
# 1.把整个表格分成4个(2n+1)的小表格，分别叫A,B,C,D:
# 2.这样A,B,C,D个小表格就成奇数幻方问题了。
# ①.将1，2，…，（2n+1）（2n+1）这些数划分给A，并对A实现奇数幻方;
# ②.将（2n+1）（2n+1）+1,…，2（2n+1）（2n+1）这些数划分给B，并对B实现奇数幻方；
# ③.将2（2n+1）（2n+1）+1，…3（2n+1）（2n+1）这些数划分C，并对C实现奇数幻方；
# ④.将3（2n+1）（2n+1）+1，…4（2n+1）（2n+1）这些数划分D，并对D实现奇数幻方。
# 3.从A表中的中心（即第n行的MagicSquare[n][n]）开始，按照从左向右的方向，标出n个数，A表中的其他行则标出最左边的n格中的数（在图中用红色背景标出）。并且将这些标出的数和C表中的对应位置互换。
# 4.在B表中的中心（如上解释）开始，自右向左，标出n-1列，将B中标出的数据与D表中对应位置的数据交换。但是6阶幻方中，n-1此时等于0，所以B与D不用做交换
# 下面是6阶幻方的填法：6＝4×1＋2，这时k＝1
# 编程要求
# 输入一个整数n(n为4k+2的倍数)，输出4k+2阶偶数幻方数。
# (输出之间用制表符分隔)
# 测试说明
# 平台会对你编写的代码进行测试：
# 测试输入：
# 6
# 预期输出：
# 33    1    8    24    19    26    
# 7    32    3    25    23    21    
# 29    9    4    20    27    22    
# 6    28    35    15    10    17    
# 34    5    30    16    14    12    
# 2    36    31    11    18    13    




# 读取附件中的csv文件（通讯录信息），放入字典中(后两项以列表形式做为字典的值)，并依次输出其中的信息。文件内数据不需要修改，输出时数据之间以空格间隔。
# 编码格式使用GBK
# 输入‘A’时，按行输出文件信息
# 输入‘D’时，直接输出字典内容
# 输入其他数据时，输出“ERROR”
# 输入格式
# 输入一个字符
# 输出格式
# 张自强 12652141777 材　料
# 庚同硕 14388240417 自动化
# 王　岩 11277291473 文　法
# 杨　彪 18807390227 材　料
# 姚梦雪 14101628144 文　法
# 黄国宝 19439017361 材　料
# 麦啟聪 18844865547 信　息
# 陈天润 14622379485 材　料
# 项子烜 14226176598 文　法
# 任晋宏 15076627604 信　息
# 王玉云 11128829508 文　法
# 周佳乐 10826074903 文　法
# 输入输出示例
# 示例1：
# 输入：A
# 输出：
# 张自强 12652141777 材　料
# .....
# 示例2：
# 输出：D
# 输出：
# {'张自强': ['12652141777', '材\u3000料'], '庚同硕': ['14388240417', '自动化'],...}
# import csv
# with open("info.csv","r",encoding="GBK")as f:
#     readr=csv.reader(f)
#     div={}
#     for i in readr:
#         div[i[0]]=[i[1],i[2]]
# str4=input()
# if str4=='D':
#     print(div)
# elif str4=='A':
#     for i,x in div.items():
#         print(f'{i} {x[0]} {x[1]}')


        
# 根据附件文件对酒店评价数据进行分析，本题使用jieba库中的lcut函数对数据进行分词。
# import jieba
# test_str = '武汉理工大学是一所世人仰慕的大学'` 
# result = jieba.lcut(test_str) # 参数是字符串，结果是将字符串切分为词的列表 `
# print(result) # ['武汉理工大学', '是', '一所', '世人', '仰慕', '的', '大学']
# 文件数据每行包括评论属性和评论内容两个数据，其中评论属性中’1‘代表好评，’0‘代表差评。
# 要求实现以下功能：
# 文件编码格式为GBK，读取函数示例如下：
# with open('comment.csv', 'r', encoding='GBK') as f:
#     ls=[i.strip().split(',',maxsplit=1) for i in f.readlines()[1:]]
# 输入n
# 如果n为’总评‘，分别输出该文件评论总数，好评条数，差评条数，输出格式参照示例一。
# 如果n为’平均‘，输出该文件中所有评论内容的平均长度（不需要排除字母，标点符号和数字），输出四舍五入后的整数，输出格式参照示例二。
# 如果n为’好评‘，对文件中所有好评进行词频分析，并输出词频出现最多的前15个词以及出现次数，输出格式参照示例三
# 如果n为’差评‘，对文件中所有差评进行词频分析，并输出词频出现最多的前15个词以及出现次数，输出格式参照示例四
# 注：3，4两项功能中统计的词语，要求长度不小于2，不是数字组成，并且不是排除词.
# 排除词 
# ex=['不错','比较','可以','感觉','没有', '我们','就是','还是','非常','但是', '不过','有点','一个','一般','下次', '携程','不是','晚上','而且','他们', '什么','不好','时候','知道','这样', '这个','还有','总体','位置','客人', '因为','如果','这里','很多','选择', '居然','不能','实在','不会','这家', '结果','发现','竟然','已经','自己', '问题','不要','地方','只有','第二天', '酒店','房间','虽然']
# 如果n非以上输入，输出’无数据‘，格式参照示例五
# 输入输出示例
# 示例只是输出格式示例，其中数据均与题目无关！
# 注意：
# 为屏蔽jieba库系统信息，本题要求在代码开始处加入如下代码：
# import jieba
# import logging
# jieba.setLogLevel(logging.INFO)
# 示例 1
# 输入:
# 总评
# 输出:
# 总评论: 8888
# 好评: 6666
# 差评: 2222
# 示例 2
# 输入:
# 平均
# 输出:
# 86
# 示例 3
# 输入:
# 好评
# 输出:
# 好像: 1000
# 也许: 901
# 早餐: 817
# 偶尔: 749
# 环境: 694
# 设施: 669
# 无论: 596
# 价格: 495
# 干净: 428
# 程序: 419
# 服务员: 337
# 免费: 269
# 交通: 206
# 餐厅: 162
# 性价比: 154
# 示例 4
# 输入:差评
# 输出:
# 恶劣: 857
# 服务: 788
# 前台: 766
# 服务员: 681
# 早餐: 632
# 宾馆: 632
# 胡说: 502
# 价格: 432
# 退房: 344
# 老虎: 324
# 电话: 319
# 态度: 317
# 卫生间: 315
# 点评: 214
# 方便: 204
# 示例 5
# 输入:
# 1234
# 输出:
# 无数据
# import jieba
# import logging
# jieba.setLogLevel(logging.INFO)
# ex=['不错','比较','可以','感觉','没有', '我们','就是','还是','非常','但是', '不过','有点','一个','一般','下次', '携程','不是','晚上','而且','他们', '什么','不好','时候','知道','这样', '这个','还有','总体','位置','客人', '因为','如果','这里','很多','选择', '居然','不能','实在','不会','这家', '结果','发现','竟然','已经','自己', '问题','不要','地方','只有','第二天', '酒店','房间','虽然']
# with open('comment.csv', 'r', encoding='GBK') as f:
#     ls=[i.strip().split(',',maxsplit=1) for i in f.readlines()[1:]]




# 利用附件中的成绩数据进行成绩统计，根据总分进行升序排序后，输出总分最低分和最高分，按总分升序输出前n名同学和后n名同学成绩信息（n为非负数，当n大于数据行数时，按实际行数输出），输出每题的平均成绩。
# （注：数据文件中最后一列是总分，第4-9列每列为一道题的成绩，打开与关闭文件代码已经给出）
# 输入格式
# 输入一个正整数
# 输出格式
# 参考示例
# 示例
# 输入：
# 2
# 输出：
# 最低分0分,最高分30分
# [['12529', '朱佳年', '0121701100203', '0', '0', '0', '0', '0', '0', '0'], ['12347', '李世祥', '0121701100208', '0', '0', '0', '0', '0', '0', '0']]
# [['11916', '杨旺霖', '0121701100527', '5', '5', '5', '5', '5', '5', '30'], ['11955', '罗家威', '0121701100622', '5', '5', '5', '5', '5', '5', '30']]
# [3.11, 3.24, 2.97, 3.24, 2.57, 3.24]
# import csv
# list1=[]
# list2=[]
# list3=[]
# list4=[]
# list5=[]
# num,num1,num2,num3,num4,num5,num6=0,0,0,0,0,0,0
# with open("成绩单.csv","r",encoding="utf-8") as f:
#     text=csv.reader(f)
#     for i in text:
#         num1+=float(i[3])
#         num2+=float(i[4])
#         num3+=float(i[5])
#         num4+=float(i[6])
#         num5+=float(i[7])
#         num6+=float(i[8])
#         list1.append([i[0],int(i[9])])
# list5.append(float(num1))
# list5.append(float(num2))
# list5.append(float(num3))
# list5.append(float(num4))
# list5.append(float(num5))
# list5.append(float(num6))
# n=int(input())
# list2=sorted(list1,key=lambda x:x[1])
# num=len(list1)
# min3=list2[0][1]
# max4=list2[-1][1]
# print(f'最低分{min3}分,最高分{max4}分')
# if n<=num:
#     for i in range(n):
#         with open("成绩单.csv","r",encoding="utf-8") as f:
#             text=csv.reader(f)
#             for j in text:
#                 if list2[i][0]==j[0]:
#                     list3.append(j)
#                 elif list2[num-i-1][0]==j[0]:
#                     list4.insert(0,j)
# else:
#     for i in range(num):
#         with open("成绩单.csv","r",encoding="utf-8") as f:
#             text=csv.reader(f)
#             for j in text:
#                 if list2[i][0]==j[0]:
#                     list3.append(j)
#                 elif list2[num-i-1]==j[0]:
#                     list4.insert(0,j)
# print(list3)
# print(list4)
# for z in range(6):
#    list5[z]=round(list5[z]/num,2)
# print(list5)
    


# 本题附件包含500名国际高校的研究生申请人的相关信息和预测的录取概率数据。
# 下表为文件中字段及对应含义：
# Serial No	GRE Score	TOEFL Score	University Rating	SOP	LOR	CGPA	Research	Chance of Admit
# 编号1-500	GRE分数	托福分数	本科大学排名分	个人陈述分数	推荐信分数	本科绩点	研究经历（1/0）	录取概率（0-1之间）
# 研究经历：1代表有，0代表无
# 录取概率：0-1之间的小数，如0.73代表73%
# 请按照下列要求对文件中数据进行统计和分析，并严格按照下面所示格式输出结果。
# （描述中示例仅为格式示例，数据与测试用例无关）
# 输入一个数据n
# 1：如果n为'1'，抽取数据中录取概率大于等于80%的记录，计算其中大学排名评分大于等于4分的百分比，程序结束。
# 1
# Top University in >=80%:11.11%
# 2：如果n为'Research'，分别统计和输出录取概率大于等于90%的学生和录取概率小于等于70%的学生中，有研究经历的学生占比，程序结束。（百分比保留两位小数）
# Research
# Research in >=90%:91.03%
# Research in <=70%:22.10%
# 3：如果n为'2'，输出录取概率大于等于80%的学生中TOEFL分数的平均分，最高分和最低分，程序结束。（保留两位小数）
# 2
# TOEFL Average Score:300.12
# TOEFL Max Score:323.00
# TOEFL Min Score:299.00
# 4：如果n为'3'，输出录取概率大于等于80%的学生中绩点的平均分，最高分和最低分，程序结束。（保留三位小数）
# 3
# CGPA Average Score:4.333
# CGPA Max Score:4.910
# CGPA Min Score:4.134
# 5：如果非以上输入，则输出'ERROR'，程序结束。
# import csv
# list1=[]
# list2=[]
# list3=[]
# with open("admit2.csv","r",encoding="utf-8")as f:
#     text=csv.reader(f)
#     for i in text:
#         if i[8]=="Chance of Admit ":
#             continue
#         else:
#             if float(i[8])>=0.8:
#                 list1.append(i)
#             elif 0.7<=float(i[8])<=0.9:
#                 list2.append(i)
# n=input()
# num1=len(list1)
# num2=len(list2)
# num=0
# if n=="1":
#     for i in list1:
#         if int(i[1])>=4:
#             num+=1
#     print(f'Top University in >=80%:{(num/num1*100):.2f}%')
# elif n=="2":
#     for i in list1:
#         num+=int(i[3])
#     list1=sorted(list1,key=lambda x:x[3])
#     print()
#     print()
#     print()
# elif n=="3":

# elif n=="Research":

# else:
#     print("ERROR")


# 为了完成本关任务，你需要掌握：
# 1.数值运算
# 2.格式化输出
# 数值运算
# +、-、*、/、//、%分别可以用于做加、减、乘、除、整除和取模的运算。
# 格式化输出
# str.format()和f-string都可以用于格式化输出的字符串。
# 编程要求
# 收银员分两行输入用户需支付的金额和用户实际支付的金额数，系统先输出找零金额再计算并给出找零方案，
#假设收银员有足够的各种面值的零钱且优先用尽量多的大面值货币做找零，请计算找零中各种面额的货币的数量。
#要求大于或等于1元的一律用纸币，小于1元的一律用硬币做找零。按要求输出找零中每种货币的数量，
#使售货员可以按提示完成找零工作，避免出错。
# 输出格式参考示例，本题中找零只使用以下面值：
# 纸币：50元，20元，10元，5元，2元，1元
# 硬币：5角，2角，1角，5分，2分，1分
# 测试说明
# 平台会对你编写的代码进行测试：
# 测试输入：
# 28.7
# 100
# 预期输出：
# 需支付的金额：28.70元
# 实际支付的金额：100.00元
# 找零金额为：71.30元
# 50元纸币数量为：1张
# 20元纸币数量为：1张
# 1元纸币数量为：1张
# 2角硬币数量为：1个
# 1角硬币数量为：1个
# 提示：
# 浮点数经常无法精确表示可能会带到结果的偏差，需要解决
# num1=round(eval(input()),2)
# num2=round(eval(input()),2)
# num3=round(num2-num1,2)
# q=0
# print(num1,num2)
# print(f'需支付的金额：{num1:.2f}')
# print(f'实际支付的金额：{float(num2):.2f}')
# print(f'找零金额为：{num3:.2f}')
# if num3>=50:
#     q=int(num3//50)
#     num3=round(num3-50*q,2)
#     print(f"50元纸币数量为：{q}张")
# if num3>=20:
#     q=int(num3//20)
#     num3=round(num3-20*q,2)
#     print(f"20元纸币数量为：{q}张")
# if num3>=10:
#     q=int(num3//10)
#     num3=round(num3-10*q,2)
#     print(f"10元纸币数量为：{q}张")
# if num3>=5:
#     q=int(num3//5)
#     num3=round(num3-5*q,2)
#     print(f"5元纸币数量为：{q}张")
# if num3>=2:
#     q=int(num3//2)
#     num3=round(num3-2*q,2)
#     print(f"2元纸币数量为：{q}张")
# if num3>=1:
#     q=int(num3//1)
#     num3=round(num3-1*q,2)
#     print(f"1元纸币数量为：{q}张")
# if num3>=0.5:
#     q=int(num3//0.5)
#     num3=round(num3-0.5*q,2)
#     print(f"5角硬币数量为：{q}个")
# if num3>=0.2:
#     q=int(num3//0.2)
#     num3=round(num3-0.2*q,2)
#     print(f"2角硬币数量为：{q}个")
# if num3>=0.1:
#     q=int(num3//0.1)
#     num3=round(num3-0.1*q,2)
#     print(f"1角硬币数量为：{q}个")
# if num3>=0.05:
#     q=int(num3//0.05)
#     num3=round(num3-0.05*q,2)
#     print(f"5分硬币数量为：{q}个")
# if num3>=0.02:
#     q=int(num3//0.02)
#     num3=round(num3-0.02*q,2)
#     print(f"2分硬币数量为：{q}个")
# if num3>=0.01:
#     q=int(num3//0.01)
#     num3=round(num3-0.01*q,2)
#     print(f"1分硬币数量为：{q}个")


# 物不知数”出自《孙子算经》。题目为“今有物不知其数，三三数之剩二；五五数之剩三；七七数之剩二。问物几何?”
# 意思是说有一些物品，不知道有多少个，3个3个数的话，还多出2个；5个5个数则多出3个；7个7个数也会多出2个。
# 它的系统解法是秦九韶在《数书九章·大衍求一术》中给出的。
# #大衍求一术（也称作“中国剩余定理”）是中国古算中最有独创性的成就之一，属现代数论中的一次同余式组问题。
# 现假设物品总数不超过n (n<=1000)，请编程计算满足条件的物品个数并输出。
# 输入格式
# 输入为一个正整数n，题目保证 0 < n <= 1000 。
# 输出格式
# 输出不超过n且满足条件的物品个数m，如果有多个解，则分行输出，如果无解则输出No solution!。
# 示例 1
# 输入:
# 10
# 输出:
# No solution!
# 示例2
# 输入:
# 200
# 输出:
# 23
# 128
# n=eval(input())
# flag=0
# for i in range(1,n+1):
#     if (i-2)%3==0 and (i-3)%5==0 and (i-2)%7==0:
#         print(i)
#         flag+=1
# if flag==0:
#     print("No solution!")

# 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，如果要求鸡翁、鸡母、鸡雏都不为零，问鸡翁、鸡母、鸡雏各几何？
# 输入格式
# 该题目没有输入
# 输出格式
# 每行输出一组结果，按鸡翁数、鸡母数、鸡雏数的顺序输出，数字之间用空格分隔；
# 如果有多组解时，按鸡翁数量由少到多输出;
# 示例
# 输出：
# x xx xx
# x xx xx
# xx x xx
# list1=[]
# for i in range(1,100):
#     for j in range(1,100):
#         k=300-15*i-9*j
#         if k>0 and k%3==0 and i+j+k==100:
#             list1.append([i,j,k])
# list2=[]
# list2=sorted(list1,key=lambda x:x[0])
# for i in list2:
#     print(f"{i[0]} {i[1]} {i[2]}")

# 大约在1500年前，《孙子算经》中记载一个有趣的问题：今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？
# 大概的意思是：有若干只鸡兔同在一个笼子里，从上面数，有35个头，从下面数，有94只脚，问笼中各有多少只鸡和兔？
# 请编一个程序，用户在同一行内输入两个整数，代表头和脚的数量，编程计算笼中各有多少只鸡和兔
#（假设鸡和兔都正常，无残疾）。如无解则输出Data Error!
# 参考下面的示例代码，从同一行读入两个数
# a, b = input().split() # 将输入的以空格分隔的两个数命名为a和b
# a, b = map(int,input().split(',')) # 将输入的以逗号分隔的两个值，转换为整数后命名为a和b
# 输入格式
# 输入为一行，以空格分隔的两个整数heads, legs，分别代表鸡兔的总头数和总脚数。
# 输出格式
# 若有解输出：
# 有m只鸡，n只兔
# 若无解则输出:
# Data Error!
# 示例 1
# 输入：
# 35 94
# 输出：
# 有23只鸡，12只兔
# 示例 2
# 输入：
# -24 12
# 输出：
# Data Error!
# 示例 3
# 输入：
# 12 35
# 输出：
# Data Error!

# n, m = map(int,input().split(','))
# x=4*n-m
# y=m-2*n
# if x%2==0 and y%2==0:
#     print(f"有{x//2}只鸡，{y//2}只兔")
# else:
#     print("Data Error!")

# 《九章算术》的“盈不足篇”里有一个很有意思的老鼠打洞问题。原文是这么说的：
#今有垣厚十尺，两鼠对穿。大鼠日一尺，小鼠亦一尺。大鼠日自倍，小鼠日自半。问：何日相逢？各穿几何？
# 这道题的意思是：
# 有一堵十尺厚的墙，两只老鼠从两边向中间打洞。大老鼠第一天打一尺，小老鼠也是一尺。
# 大老鼠每天的打洞进度是前一天的一倍，小老鼠每天的进度是前一天的一半。问它们几天可以相逢，相逢时各打了多少。
# 请编程求此题的解，要求使用循环来完成，不允许使用幂运算。
# 输入格式
# 输入为一个整数wall，代表墙的厚度，单位为尺。
# 输出格式
# 输出为两行
# 第一行输出 1 个整数，表示相遇时所需的天数。
# 第二行输出 2 个浮点数，依次为小鼠和大鼠打洞的距离，单位为尺，保留小数点后 1 位数字。
# （提示：round(f,1)为浮点数 f 保留一位小数。）
# 示例 1
# 输入：
# 10
# 输出：
# 4
# 1.8 8.2
# 示例2
# 输入：
# 2
# 输出：
# 1
# 1 1
# 提示
# 最后一天可能不足一天便打通了
# 3
# 2
# 1.2 1.8
# 100
# 7
# 2.0 98.0
# 20
# 5
# 1.9 18.1



# wall=int(input())
# da,da1=1,0
# xiao,xiao1=1,0
# time,day=1,0
# while wall>0:
#     if wall-da-xiao<0:
#         time=wall/(da+xiao)
#     wall=wall-da-xiao
#     xiao1=xiao1+time*xiao
#     da1=da1+time*da
#     da*=2
#     xiao/=2
#     day+=1
# print(day)
# print(round(xiao1,1),round(da1,1))
# n = int(input())
# rat, mouse, day, time = 1, 1, 0, 1 #大老鼠进度，小老鼠进度，相遇时间，第一天时间
# distance_of_rat, distance_of_mouse = 0, 0  # 大老鼠和小老鼠的打洞距离
# while n > 0:
#     if n - mouse - rat < 0: #第一天打洞完成
#         time = n / (mouse + rat)	#算出需要时间
#     n = n - mouse - rat	#剩余墙厚
#     distance_of_mouse = distance_of_mouse + time * mouse
#     distance_of_rat = distance_of_rat + time * rat
#     rat = rat * 2	#大老鼠每天进度
#     mouse = mouse / 2	#小老鼠每天进度
#     day = day + 1	#时间过去一天
# print(day)
# print(round(distance_of_mouse, 1), round(distance_of_rat, 1))













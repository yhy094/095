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
def Year(year):
    if (year%4==0 and year%100!=0)or(year%400==0):   return 'T'
    else:   return 'F'
def mo(a,b):
    if a=='T' and b<=29:
        return True
    elif a=='F' and b<=28:
        return True
    else:   return False
def panduan(str2,list7,list8):
    num=0
    m=0
    for i in range(17):
        num+=int(str2[i])*int(list7[i])
    m=int(num%11)
    if str2[-1]==list8[m]:
        return True
    else:
        return False
def xinbie(nm):
    if nm%2==0:
       return '女'
    else:
        return '男'
def riqi(month,day):
    if ((month==1)or(month==3)or(month==5)or(month==7)or(month==8)or(month==10)or(month==12))and(0<day<=31)and(0<month<=12):
        return True
    elif ((month==2)or(month==4)or(month==6)or(month==9)or(month==11))and(0<day<=30)and(0<month<=12):
        return True
    else:    return False
list7=['7','9','10','5','8','4','2','1','6','3','7','9','10','5','8','4','2']
list8=['1','0','X','9','8','7','6','5','4','3','2']
if __name__=='__main__':
    list1=[]
    str1=input()
    if len(str1)!=18:
        print('身份证校验错误1')
    else:
        list1.append(str1[6:10])
        list1.append(str1[10:12])
        list1.append(str1[12:14])
        if (list1[1]=='02')and(mo(Year(int(list1[0])),int(list1[2]))):
           if panduan(str1,list7,list8):
               print('身份证号码校验为合法号码')
               print(f'出生：{list1[0]}年{list1[1]}月{list1[2]}日')
               nm=int(str1[16])
               str3=xinbie(nm)
               print(f'性别：{str3}')
           else:
               print('身份证校验错误31')
        elif list1[1]!='02' and riqi(int(list1[1]),int(list1[2])):
            if panduan(str1,list7,list8):
               print('身份证号码校验为合法号码')
               print(f'出生：{list1[0]}年{list1[1]}月{list1[2]}日')
               nm=int(str1[16])
               str3=xinbie(nm)
               print(f'性别：{str3}')
            else:
               print('身份证校验错误32')
        else:
            print('身份证校验错误2')

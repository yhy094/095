# #qingyunke API 接口：	http://api.qingyunke.com/api.php?key=free&appid=0&msg=你好
# #导库
# import requests  #网络请求库

# #寻址，目标网址
# #青云客：
# url='http://api.qingyunke.com/api.php?key=free&appid=0&msg='
# #请求：
# res=requests.get(url+'你好')
# #处理数据：  网络格式的字典或者列表，统称为json
# #print(res.text)
# res1=res.json()   #使用json方法，将json转换为python中的字典与列表
# print(res1['content'])





#进阶爬虫：
#前置知识：
#网页的骨架：html     网页的衣服：css
    #1.html语言:HTML，全称为超文本标记语言(HyperText Markup Language)，是用于创建网页的标准标记语言。它描述和定义了网页内容的结构。
    #HTML使用标记来注明文档中应如何显示哪些元素。
    #一个HTML标记包含了元素名称以及两种尖括号。这些元素通常成对出现，分为开始标记和结束标记，
    #如 <h1>和</h1>。注：h后的‘1’可以被任意其他的东西所替换
    #主要格式：<标签名> 内容 <标签名/>   所讲内容请跳转到demo2.html中进行观看
    
    #2.css语言:
    #选择器{
    #    属性名：属性值 (设置网页中标签的属性的)
    #   选择器种类：标签名，id（用时需要加个#），种类class(用时在前面加个.)
    #   所讲知识点观看请跳转到demo2.html中进行观看
    #}

# from bs4 import BeautifulSoup  #导入进阶爬虫库
# import requests
# #注意：www.是网页端，而m.是移动端
# url='https://www.thepaper.cn/newsDetail_forward_26425054'
# res=requests.get(url)
# #处理数据
# #将获取到的内容放到bs4中进行解析
# #BeautifulSoup(网页源代码,解析器)
# #解析器：
# # html.parser：这是标准库中的HTML解析器，即不需要安装任何额外的库就可以使用。虽然速度略慢，但可以满足大部分简单的HTML解析需求。
# # lxml：这是一个非常高效的库，可以处理HTML和XML。相比于html.parser，它通常要更快，也更强大。但这是一个外部库，所以使用之前需要安装：pip install lxml
# # html5lib：这个解析器更多地把HTML看作为浏览器所看到的一类文档，并确保象浏览器一样处理它。比如没有闭合的标签，浏览器也会正常解析，而html5lib同样可以处理。但它的速度比另外两种解析器慢。这也是一个外部库，使用之前需要安装：pip install html5lib
# soup=BeautifulSoup(res.text,"html.parser")

# #1.单独查找  使用bs对象的find方法find(标签名，属性)
# unit=soup.find("div",class_="index_cententWrap__Jv8jK")
#     #子标签查找
# image=unit.img
#     #获取属性，使用字典的索引方式
# #print(image.attrs)  #attrs获取到了所有属性的键值对都保存到了一个字典中
# img_src=image.attrs['src']  #获取到了该图片的网址
# with open("img1.png","wb") as f:   #注意：音频与音乐保存到文件中的时候需要用到'wb'
#     img_content=requests.get(img_src)
#     f.write(img_content.content)  #content可以爬取图片，视频，音乐，文本用text，json文件用.json()

#2.查找所有
# from bs4 import BeautifulSoup  #导入进阶爬虫库
# import requests
# #注意：www.是网页端，而m.是移动端
# url='https://www.thepaper.cn/newsDetail_forward_26425054'
# res=requests.get(url)
# soup=BeautifulSoup(res.text,"html.parser")
# # 查找所有，使用bs对象的find_all方法find(标签名，属性),返回的是一个列表
# units=soup.find_all("div",class_="index_cententWrap__Jv8jK")
# #bs对象的text属性，既是查看标签的文本内容
# for i in units:
#     print(i.text)

#3.使用选择器查找
from bs4 import BeautifulSoup  #导入进阶爬虫库
import requests
#注意：www.是网页端，而m.是移动端
url='https://www.thepaper.cn/newsDetail_forward_26425054'
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")


# 选择查找，通过类select(".地址")来查找，通过id来查找select("#地址"),返回的是一个列表
units=soup.select(".index_cententWrap__Jv8jK")
#bs对象的text属性，既是查看标签的文本内容
for i in units:
    print(i.text)








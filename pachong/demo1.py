#部分知识点
# # 服务器：相当于电脑
# # ip地址：相当于电脑接入网络之后的身份证
# # 域名：www.budu.com（相当于人的名字）
# # 二进制文件：视频，音乐，图片，文件
# # dns域名服务器可以寻找到服务器的地址
# # src属性是原地址，原网址
# # https:---是我们的加密的安全协议，  http:---是我们的不加密的安全协议
# # 用content：来获取HTTP响应的二进制内容
# # 用status_code：获取HTTP响应的状态码
# # headers：HTTP响应的头信息（寄件人的身份信息），返回的是一个字典
# # print(response.headers)
# # text：HTTP响应的主体内容，此属性会自动对结果进行解码
# # print(response.text)
# # content：HTTP响应的二进制内容（图片，视频）
# # print(response.content)
# # json()：如果HTTP响应的内容是json（相当于网页格式的列表，字典），我们可以使用此方法解析json，返回一个字典。
# # print(response.json())
# # cookies：一个CookieJar对象（临时存储信息，秘钥），包含服务器设置的所有cookies
# # print(response.cookies)
# # url：URL of the response（网址）
# # print(response.url)
# # encoding：获取响应的编码方式
# # print(response.encoding)




# 代码实验
# import requests   #导入网络请求库

# # 发送get请求（明文发送请求）
# response=requests.get('http://httpbin.org/get')   
# #明文发送response=requests.get('http://httpbin.org/get?zhanghao:value1,mima:1234')
# print(response)
# # 输出状态码
# print(response.status_code)
# # 输出寄件人信息(响应头)
# print(response.headers)
# # 输出包裹里的内容
# print(response.text)
# # 发送post请求(保密的请求，密文发送请求)
# data={
#     'zhaonhao':'value1',
#     'mima':1234
# }
# requests.post('http://httpbin.org/post',data=data)



# #text测试
# # //www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
# # 基础爬虫四部曲：1.导库 2.寻址 3.请求 4.处理数据
# #1.导库
# # import requests
# # #2.寻址
# # url1='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
# # #3.请求
# # res=requests.get(url1)
# # #4.处理数据
# # f=open('image.png','wb')  #创建这个图片，用wb模式打开写入二进制 
# # f.write(res.content)   #图片，音乐，文件都是用content

 

# # 爬取天气信息（用API接口（就是给你了网址，直接可以访问））
# # http://tianqiapi.com/index（提供的天气的API接口的网址）
# # http://v1.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=
# #该网址可以分为两个部分：
# #1.（?之前的部分http://v1.yiketianqi.com/api?）:
# #2.(?之后的部分unescape（）=1、&version（）=v91、&appid（账户名）=43656176、&appsecret（账号密码）=I42og6Lm、&ext（）=、&cityid（）=、&city（城市）=)

# #导库
# import requests
# #访问目标网址
# while True:
#     city=input('请输入城市：')
#     #我自己的账号：http://v1.yiketianqi.com/api?appid=89468848&appsecret=rvj3Mbbb&city=
#     url='http://v1.yiketianqi.com/api?appid=89468848&appsecret=rvj3Mbbb&city='+ city
#     res=requests.get(url)  
#     # print(url)
#     #print(res.text)   #查看爬取到的文本内容
#     # 对于json文件使用.json()方法将网页格式字典转化为python格式字典
#     res2=res.json()
#     res2=res2['aqi']
#     #res2是python字典，将想要的信息通过字典索引出来
#     # print(res2['aqi'])
#     print(f"城市为：{city}")
#     print(f"空气质量：{res2['air_level']}")
#     print(f"运动建议：{res2['air_tips']}")
#     print(f"o3浓度：{res2['o3']}")
#     print(f"no2：{res2['no2']}")
#     print(f"co：{res2['co']}")

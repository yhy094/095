#爬取视频时，可以搜索网址的API接口（如：b站视频解析API接口）
#爬取VIP时需要JS逆向，JAVASCRIPT
#头部网站：网络工程师多，经验丰富，
#中小网站：基本没有网络安全工程师，VIP较容易爬取
#网页请求后会返回HTML(创建网页骨架)文件，以及css(美化网页)文件1.......css文件n，js(设置交互的，功能的)(Javascript)文件1......js文件n





# # 爬取小说的步骤：1.获取小说每个章节的网址。2.进去后拿取本章节的内容
# # 爬取起点小说网下载（免费）
# # 注意：起点小说网站开始就有防爬措施，不会再开发者工具中显示代码，而是一直挂起
# # 解决措施：
# # *1.点击（在开发者.png中）右边最后一个按钮，在点击左边最前一个按钮（解释：在css与js中增加断点，可以阻止让开发者工具暂停的文件的运行，从而使文件能够正常的获取）

#    #1.导库
# import requests
# from bs4 import BeautifulSoup
# import time
#     #2.寻址
# url="https://www.qidian.com/book/1023653558/"
#     #3.请求
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'DNT': "1",
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Sec-Fetch-Dest': 'document',
#     'Cookie':'_yep_uuid=602e6195-a999-195b-c267-885b3fddc5b5; e2=%7B%22l6%22%3A%221%22%2C%22l1%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; e1=%7B%22l6%22%3A%221%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1710485666_1802557666; _csrfToken=ljNtl4r44pWWEKODIrcsgnApfeGCAq4xEL0cv2Gr; fu=1877307984; traffic_utm_referer=; _gid=GA1.2.1339482135.1710485669; supportwebp=true; supportWebp=true; trkf=1; Hm_lvt_f00f67093ce2f38f215010b699629083=1710485668,1710502376; _yep_uuid=44f0ace1-c8a2-9442-48b7-d2a40af16d07; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A9%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l2%22%3A1%7D; Hm_lpvt_f00f67093ce2f38f215010b699629083=1710503039; _ga_FZMMH98S83=GS1.1.1710502376.3.1.1710503038.0.0.0; _ga=GA1.1.863536092.1710485668; _ga_PFYW0QLV3P=GS1.1.1710502376.3.1.1710503038.0.0.0; w_tsfp=ltvgWVEE2utBvS0Q6KrtnE6oED07Z2R7xFw0D+M9Os09AKYhUZuG04ByutfldCyCt5Mxutrd9MVxYnGBU9YmeBIXQ8SRb5tH1VPHx8NlntdKRQJtA5rfUVIZKr0h5DkSdTxXI0PljDx+IYVDxOdhi1kF5yF837ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgW2DugDuLi11A7hB1kCR0C0XG3pV8w2pJbsDal7wcpK9Uv8wrTPzwjn3apCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZUqukO18Lv3wdaN4qzsLDqgaGwwWqlwd4eo7qhJJDn3sZ3OOVPtzvQFVRqZfrcq+NA==',
# }
# res=requests.get(url,headers=headers)
# #4.处理数据   只要网站的部分内容==》》BeautifulSoup
# bs=BeautifulSoup(res.text,"html.parser")     #注意html.parsr是解析器的名称
# bs_a=bs.find_all("a",class_="chapter-name")   #查找所有有<a>标签的代码段
# for i in bs_a:
#     id=i["href"].split('/')[-2]     #属性值的获取类似于字典的索引方式，所有的属性与值构成一个字典
#     name=i.text
    # if "第" in name:
    #     new_url=f"https://www.qidian.com/chapter/1023653558/{id}/"
    #     new_res=requests.get(url=new_url,headers=headers)
    #     new_soup=BeautifulSoup(new_res.text,"html.parser")   #注意html.parsr是解析器的名称
    #     new_html_p=new_soup.find_all("p")    #返回的是列表
    #     with open("xiaoshuo.text",mode="a",encoding="utf-8") as f:
    #         for j in new_html_p:
    #             f.write(j.text+'\n')
    #     time.sleep(1)
# #split讲解,字符串的分割
# # s="春眠不觉晓"
# # a=s.split(',')
# # print(a)



# #笔趣阁小说下载
# #导库
# import requests
# from bs4 import BeautifulSoup
# import time
#  #2.寻址
# url="https://www.bg70.cc/book/72268/"
#     #3.请求
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
#     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     # 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     # 'DNT': "1",
#     # 'Connection': 'keep-alive',
#     # 'Upgrade-Insecure-Requests': '1',
#     # 'Sec-Fetch-Site': 'none',
#     # 'Sec-Fetch-Mode': 'navigate',
#     # 'Sec-Fetch-User': '?1',
#     # 'Sec-Fetch-Dest': 'document',
#     #'Cookie':'_yep_uuid=602e6195-a999-195b-c267-885b3fddc5b5; e2=%7B%22l6%22%3A%221%22%2C%22l1%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; e1=%7B%22l6%22%3A%221%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1710485666_1802557666; _csrfToken=ljNtl4r44pWWEKODIrcsgnApfeGCAq4xEL0cv2Gr; fu=1877307984; traffic_utm_referer=; _gid=GA1.2.1339482135.1710485669; supportwebp=true; supportWebp=true; trkf=1; Hm_lvt_f00f67093ce2f38f215010b699629083=1710485668,1710502376; _yep_uuid=44f0ace1-c8a2-9442-48b7-d2a40af16d07; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A9%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l2%22%3A1%7D; Hm_lpvt_f00f67093ce2f38f215010b699629083=1710503039; _ga_FZMMH98S83=GS1.1.1710502376.3.1.1710503038.0.0.0; _ga=GA1.1.863536092.1710485668; _ga_PFYW0QLV3P=GS1.1.1710502376.3.1.1710503038.0.0.0; w_tsfp=ltvgWVEE2utBvS0Q6KrtnE6oED07Z2R7xFw0D+M9Os09AKYhUZuG04ByutfldCyCt5Mxutrd9MVxYnGBU9YmeBIXQ8SRb5tH1VPHx8NlntdKRQJtA5rfUVIZKr0h5DkSdTxXI0PljDx+IYVDxOdhi1kF5yF837ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgW2DugDuLi11A7hB1kCR0C0XG3pV8w2pJbsDal7wcpK9Uv8wrTPzwjn3apCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZUqukO18Lv3wdaN4qzsLDqgaGwwWqlwd4eo7qhJJDn3sZ3OOVPtzvQFVRqZfrcq+NA==',
# }
# res=requests.get(url,headers=headers)

# #4.处理数据   只要网站的部分内容==》》BeautifulSoup
# bs=BeautifulSoup(res.text,"html.parser")
# soup_html=bs.select("div.listmain dl dd a")    #查找这一部分的内容,逐层查找，找到想要的标签，select返回的是一个列表
# #遍历所有章节超链接
# for i in soup_html:
#     href=i["href"]   #获取每个章节的超链接
#     name=i.text #获取章节名
#     if "/72268" in href:
#         new_url=f"https://www.bg70.cc{href}"
#         new_res=requests.get(url=new_url,headers=headers)
#         new_soup=BeautifulSoup(new_res.text,"html.parser")
#         div_id=new_soup.find("div",id="chaptercontent")
#         with open(f"txt/{name}.txt",mode="a",encoding="utf-8") as f:
#             print(f"正在下载：《{name}》,请稍后~")
#             # f.write(div_id.text)
#             for j in div_id:
#                 f.write(j.text+'\n')
#             time.sleep(1)


    
#笔趣阁小说下载
#导库
import requests
from bs4 import BeautifulSoup
import time
 #2.寻址
url="https://m.bg70.cc/book/5611/list.html"
    #3.请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'DNT': "1",
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Sec-Fetch-Dest': 'document',
#     'Cookie':'_yep_uuid=602e6195-a999-195b-c267-885b3fddc5b5; e2=%7B%22l6%22%3A%221%22%2C%22l1%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; e1=%7B%22l6%22%3A%221%22%2C%22l1%22%3A2%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1710485666_1802557666; _csrfToken=ljNtl4r44pWWEKODIrcsgnApfeGCAq4xEL0cv2Gr; fu=1877307984; traffic_utm_referer=; _gid=GA1.2.1339482135.1710485669; supportwebp=true; supportWebp=true; trkf=1; Hm_lvt_f00f67093ce2f38f215010b699629083=1710485668,1710502376; _yep_uuid=44f0ace1-c8a2-9442-48b7-d2a40af16d07; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A9%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l2%22%3A1%7D; Hm_lpvt_f00f67093ce2f38f215010b699629083=1710503039; _ga_FZMMH98S83=GS1.1.1710502376.3.1.1710503038.0.0.0; _ga=GA1.1.863536092.1710485668; _ga_PFYW0QLV3P=GS1.1.1710502376.3.1.1710503038.0.0.0; w_tsfp=ltvgWVEE2utBvS0Q6KrtnE6oED07Z2R7xFw0D+M9Os09AKYhUZuG04ByutfldCyCt5Mxutrd9MVxYnGBU9YmeBIXQ8SRb5tH1VPHx8NlntdKRQJtA5rfUVIZKr0h5DkSdTxXI0PljDx+IYVDxOdhi1kF5yF837ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgW2DugDuLi11A7hB1kCR0C0XG3pV8w2pJbsDal7wcpK9Uv8wrTPzwjn3apCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZUqukO18Lv3wdaN4qzsLDqgaGwwWqlwd4eo7qhJJDn3sZ3OOVPtzvQFVRqZfrcq+NA==',
}
res=requests.get(url,headers=headers)

#4.处理数据   只要网站的部分内容==》》BeautifulSoup
bs=BeautifulSoup(res.text,"html.parser")
soup_html=bs.select("div.book_last dl dd a")    #查找这一部分的内容,逐层查找，找到想要的标签，select返回的是一个列表
#遍历所有章节超链接
for i in soup_html:
    href=i["href"]   #获取每个章节的超链接
    name=i.text #获取章节名
    if "/book/5611" in href:
        new_url=f"https://www.bg70.cc{href}"
        new_res=requests.get(url=new_url,headers=headers)
        new_soup=BeautifulSoup(new_res.text,"html.parser")
        div_id=new_soup.find("div",id="chaptercontent")
        with open(f"txt/{name}.txt",mode="a",encoding="utf-8") as f:
            print(f"正在下载：《{name}》,请稍后~")
            # f.write(div_id.text)
            for j in div_id:
                f.write(j.text+'\n')
            time.sleep(1.5)


    





















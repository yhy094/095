#1.pandas  可以处理海量数据，效率很高
# import pandas as pd

#pandas创建表格步骤
#1.创建dataframe对象
#2.将我们的dataframe对象转化为表格

#通过列创建表格(传入每一列的数据)传入字典每一个键值对是一列
# df=pd.DataFrame({
#     'name':['john','anna','peter'],
#     'age':[23,45,29],
#     'salary':[2000,6000,15000]
# }) 
#将dataframe对象转化为Excel表格
# df.to_excel("ouput.xlsx")  #注：括号中是表格的名称
#通过行来创建表格,传入列表，列表里面每一行是一个字典
# df=pd.DataFrame(
# [
#     {'aaa':123,'bbb':333},
#     {'aaa':2098,'bbb':471},
#     {'aaa':39123,'bbb':894}
# ]
# )
# #特殊的参数：header(行索引)=False(不显示)；
# #index(列索引)=False
# #sheet_name='名称' (表示将表格下方的工作表的表名进行修改)
# df.to_excel('dddda.xlsx',header=False,index=False)



#2.对抗反爬技术
# headers = {
#     'Accept':'application/json, text/plain, */*',
#     'Accept-Encoding':'gzip, deflate, br, zstd',
#     'Accept-Language':'zh-CN,zh;q=0.9',
#     'Connection':'keep-alive',
#     'Host':'yiqifu.baidu.com',
#     'Referer':'https://yiqifu.baidu.com/g/aqc/joblist?q=python',
#     'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
#     'Sec-Ch-Ua-Mobile':'?0',
#     'Sec-Ch-Ua-Platform':'"Windows"',
#     'Sec-Fetch-Dest':'empty',
#     'Sec-Fetch-Mode':'cors',
#     'Sec-Fetch-Site':'same-origin',
#     'X-Requested-With':'XMLHttpRequest',
#     'Cookie':'BIDUPSID=FFE582BA7343E4BDE8F2B0969587933A; PSTM=1701944630; BAIDUID=FFE582BA7343E4BDDB41B7BF2E661BA5:FG=1; BDUSS=NrUG9jTlVkRFBXa3V0bW5pNjNFUGdHaTdnc21rdXpkZUpvTU9nbFpaaGpVZEJsSVFBQUFBJCQAAAAAAAAAAAEAAABJQjjR0-nA1mNhcmV5eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPEqGVjxKhlc0; BDUSS_BFESS=NrUG9jTlVkRFBXa3V0bW5pNjNFUGdHaTdnc21rdXpkZUpvTU9nbFpaaGpVZEJsSVFBQUFBJCQAAAAAAAAAAAEAAABJQjjR0-nA1mNhcmV5eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPEqGVjxKhlc0; MCITY=-75%3A; H_WISE_SIDS_BFESS=40045_40166_40202_39662_40210_40216_40222; H_WISE_SIDS=39662_40210_40216_40222_40271_40294_40291_40289_40286_40317_40079; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39662_40210_40216_40222_40271_40294_40291_40289_40286_40317_40079_40364_40352_40301_40381_40366; BA_HECTOR=81ak8h048gak8ga1a485a1849i0vgo1iuja9s1t; ZFY=SJTaRNG4jPGf5XpXAboM31VLOh8ATplB5TW1u:Atu7Tk:C; BAIDUID_BFESS=FFE582BA7343E4BDDB41B7BF2E661BA5:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; clue_site=pc; clue_ext=%7B%22referer%22%3A%22www.baidu.com%22%2C%22ref_eqid%22%3A%22b9d3408400103e780000000665e9c22e%22%7D; log_guid=9c965543f29ee6e76083129d371aaa8a; log_first_time=1709818419524; Hm_lvt_37e1bd75d9c0b74f7b4a8ba07566c281=1709818420; Hm_lpvt_37e1bd75d9c0b74f7b4a8ba07566c281=1709818903; log_last_time=1709818910917',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
# }
# import requests
# from bs4 import BeautifulSoup
# headers = {
#     'Accept':'application/json, text/plain, */*',
#     'Accept-Encoding':'gzip, deflate, br, zstd',
#     'Accept-Language':'zh-CN,zh;q=0.9',
#     'Connection':'keep-alive',
#     'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
#     'Sec-Ch-Ua-Mobile':'?0',
#     'Sec-Ch-Ua-Platform':'"Windows"',
#     'Sec-Fetch-Dest':'empty',
#     'Sec-Fetch-Mode':'cors',
#     'Sec-Fetch-Site':'same-origin',
#     'X-Requested-With':'XMLHttpRequest',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
# }
# #基础反爬(需要在网址后添加header，相当于伪装身份)
# url='https://www.baidu.com/'
# res=requests.get(url,headers=headers)
# print(res.text)


#进阶反爬   （注意：高级反爬技术需要掌握JavaScript+密码学+js逆向==>vip）
import requests    #进行请求
from bs4 import BeautifulSoup    #解析请求后返回的代码
import json     #转换字符串为列表与字典
import time
import pandas as pd
#https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?q=ai&page=1&district=110000&salaryrange=
url="https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?"
# 寻找json接口(在复制中寻找复制url，就可以得到json接口)
headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'yiqifu.baidu.com',
    'Referer':'https://yiqifu.baidu.com/g/aqc/joblist?q=python',
    'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'X-Requested-With':'XMLHttpRequest',
    'Cookie':'BIDUPSID=FFE582BA7343E4BDE8F2B0969587933A; PSTM=1701944630; BAIDUID=FFE582BA7343E4BDDB41B7BF2E661BA5:FG=1; BDUSS=NrUG9jTlVkRFBXa3V0bW5pNjNFUGdHaTdnc21rdXpkZUpvTU9nbFpaaGpVZEJsSVFBQUFBJCQAAAAAAAAAAAEAAABJQjjR0-nA1mNhcmV5eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPEqGVjxKhlc0; BDUSS_BFESS=NrUG9jTlVkRFBXa3V0bW5pNjNFUGdHaTdnc21rdXpkZUpvTU9nbFpaaGpVZEJsSVFBQUFBJCQAAAAAAAAAAAEAAABJQjjR0-nA1mNhcmV5eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGPEqGVjxKhlc0; MCITY=-75%3A; H_WISE_SIDS_BFESS=40045_40166_40202_39662_40210_40216_40222; H_WISE_SIDS=39662_40210_40216_40222_40271_40294_40291_40289_40286_40317_40079; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39662_40210_40216_40222_40271_40294_40291_40289_40286_40317_40079_40364_40352_40301_40381_40366; BA_HECTOR=81ak8h048gak8ga1a485a1849i0vgo1iuja9s1t; ZFY=SJTaRNG4jPGf5XpXAboM31VLOh8ATplB5TW1u:Atu7Tk:C; BAIDUID_BFESS=FFE582BA7343E4BDDB41B7BF2E661BA5:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; clue_site=pc; clue_ext=%7B%22referer%22%3A%22www.baidu.com%22%2C%22ref_eqid%22%3A%22b9d3408400103e780000000665e9c22e%22%7D; log_guid=9c965543f29ee6e76083129d371aaa8a; log_first_time=1709818419524; Hm_lvt_37e1bd75d9c0b74f7b4a8ba07566c281=1709818420; Hm_lpvt_37e1bd75d9c0b74f7b4a8ba07566c281=1709818903; log_last_time=1709818910917',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

# #发送请求
# def send_get(page):
#     try:
#         params=f"q=python&page={page}&pagesize=20&district=110000&salaryrange="
#         res=requests(url,headers=headers,params=params) #注意：params是参数的意思,可以将参数传进到url中
#         res_loads=json.loads(res.text)  #将网页格式的字典（json）转换为python字典
#         res_list=res_loads["data"]["list"]
#         return res_list
#     except:
#         #如果请求失败，则返回空列表
#         return []
def send_get(page):
    try:
        params = f"q=python&page={page}&pagesize=20&district=110000&salaryrange="
        #params将上面参数传到url里
        res = requests.get(url,headers = headers, params=params)
        res_loads = json.loads(res.text)#将网页格式的字典(json)转化为python字典
        res_list = res_loads["data"]["list"]
        return res_list
    except:
        #如果请求失败
        return []
# def process_data(data):
#     #提取到想要的信息数据，存放到新的字典中
#     #https://yiqifu.baidu.com/m/jobDetail?bid=30184862322920&jobId=c0a35b7da4742684c30242853c445475
#     job_data={}
#     job_data["城市"] = data["city"]
#     job_data["公司名称"] = data["company"]
#     job_data["学历要求"] = data["edu"]
#     job_data["工作经验"] = data["exp"]
#     job_data["招聘岗位"] = data["jobName"]
#     job_data["薪资待遇"] = data["salary"]
#     jobId = data["jobId"]
#     bid = data["bid"]
#     job_url = f"https://yiqifu.baidu.com/g/aqc/jobDetail?bid={bid}&jobId={jobId}"
#     job_data["岗位职责"] = responsibility(job_url)
#     print(f"正在获取{job_data}")
#     return job_data
def process_data(data):
    #提取想要的数据，存放到新的字典中
    job_data = {}
    job_data["城市"] = data["city"]
    job_data["公司名称"] = data["company"]
    job_data["学历要求"] = data["edu"]
    job_data["工作经验"] = data["exp"]
    job_data["招聘岗位"] = data["jobName"]
    job_data["薪资待遇"] = data["salary"]
    #获取招聘详情的链接
    jobId = data["jobId"]
    bid = data["bid"]
    job_url = f"https://yiqifu.baidu.com/g/aqc/jobDetail?bid={bid}&jobId={jobId}"
    job_data["岗位职责"] = responsibility(job_url)
    print(f"正在获取{job_data}")
    return job_data
#获取岗位职责的模块    #可以先查看网页源代码提取出想要的代码，因为有些代码放在了js标签中，无法用requests，BeautifulSoup爬取
# def responsibility(job_url):
#     detail_res=requests.get(job_url,headers=headers)
#     bs=BeautifulSoup(detail_res.text,"html.parser")
#     scripts=bs.find_all("script")
#     text=""
#     for script in scripts:
#         if "window.pageData" in script.text:
#             text=script.text
#     start=text.find("window.pageDate = ")+len("window.pageDate = ")
#     end=text.find(" || {}")#find查找子字符串的索引位置
#     job_des=text[start:end]#字符串的切片
#     #将切割下来的字典字符串转换为python字典
#     data=json.loads(job_des)
#     time.sleep(1)
#     return data["desc"]
def while_data():
    #创建一个列表存放所有职位信息
    all_data=[]
    #循环获取数据
    for i in range(1,20):   #爬取1到19页码的数据
        data=send_get(i)
        #如果获取到数据则则开始处理
        if data:
            for item in data:
                try:
                    job=process_data(item)
                    all_data.append(job)
                except:
                    break
    return all_data       
def responsibility(job_url):
    detail_res = requests.get(job_url,headers=headers)
    bs = BeautifulSoup(detail_res.text,"html.parser")
    scripts = bs.find_all("script")#返回一个列表
    text = ""
    for script in scripts:
        if "window.pageData" in script.text:
            text = script.text
    start = text.find("window.pageData = ")+len("window.pageData = ")
    end = text.find(" || {}")#find查找子字符串的索引位置
    job_des = text[start:end]#字符串的切片

    #将切割下来的字典字符串转化为python字典
    data = json.loads(job_des)
    time.sleep(0.5)
    return data["desc"]   
total_data = while_data()
df = pd.DataFrame(total_data)
df.to_excel("job2.xlsx",index=False)












#3.百度照片招聘的爬虫









# open模式

# 模式
#w  写文本内容（没有该文件会新建该文件，有该文件会覆盖该文件的内容）
#r  读取文件的文本内容
#wb  写入二进制内容（没有该文件会新建该文件，有该文件会覆盖该文件的内容）
#rb  读取二进制文件的内容
#a   追加内容

# with open('1.text','w',encoding='utf-8') as f:
#     f.write('你好')

import requests
from bs4 import BeautifulSoup
url="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_10605437086296826007%22%7D&n_type=-1&p_from=-1"
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
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,"html.parser")
bs=soup.find_all("div",class_="_1NCGf")
print(bs)
# with open("texttext.png","wb")as f:
#     f.write(res.content)


#网上自动刷课
from selenium import webdriver
import time
# 下载浏览器的驱动的网址为：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH#downloads
#  学习有关selenium知识的网址：https://zhuanlan.zhihu.com/p/111859925
driver = webdriver.Edge()      # Edge浏览器

# driver = webdriver.Firefox()   # Firefox浏览器
# driver = webdriver.Firefox("驱动路径")

# driver = webdriver.Chrome()    # Chrome浏览器

# driver = webdriver.Ie()        # Internet Explorer浏览器

# driver = webdriver.Opera()     # Opera浏览器

# driver = webdriver.PhantomJS()   # PhantomJS

# 打开网页
url="https://www.baidu.com"
driver.get(url) # 打开url网页 比如 driver.get("http://www.baidu.com")
time.sleep(10)
# 控制浏览器操作
# 控制浏览器窗口大小
driver.set_window_size(480, 800)
# 浏览器后退，前进
# # 后退 driver.back()
# # 前进 driver.forward()
# 刷新
# driver.refresh() # 刷新


# 元素定位
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()
# 在element变成elements就是找所有满足的条件，返回数组。
# 一般我都自己采用 xpath 获取元素的，复制即可











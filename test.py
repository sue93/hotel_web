from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
# import time
option = webdriver.ChromeOptions()
# option.add_argument('-headless')
option.add_argument("--no-sandbox")
option.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=option)
browser.get('http://hotels.ctrip.com/hotel/wuhan477/')

box = browser.find_element_by_css_selector("[class='c_page_list layoutfix']")
global page_current
page_current = int(box.find_element_by_xpath('./a[1]').text)
page_max = int(box.find_element_by_xpath('./a[last()]').text)


while page_current<=page_max:
	print('当前页码:%d'%page_current)
	para={
		'cityName':'%25E6%25AD%25A6%25E6%25B1%2589',
		'StartTime':'2018-12-28',
		'DepTime':2018-12-29,
		'cityId':477,
		'page':page_current
	}
	r=requests.post('http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx',data=para)
	r.encoding='utf-8'
	result=r.json()["hotelPositionJSON"]
	rev=json.dumps(result,ensure_ascii=False) 
	path="D:/hotel/%d.txt"%page_current

	with open(path,"w+") as f:
		f.write(rev)
	page_current=page_current+1




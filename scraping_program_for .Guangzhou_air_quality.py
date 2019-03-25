# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import numpy as np
from bs4 import BeautifulSoup


from selenium.webdriver.firefox.options import Options

location_list=['白云石井','白云新市','麓湖','公园前','荔湾西村','黄沙路边站','荔湾芳村','杨箕路边站','海珠宝岗','海珠沙园',
'体育西','天河五山','海珠湖','大夫山','天河凤凰山','天河龙洞','奥体中心','萝岗西区','黄埔文冲','黄埔大沙地','亚运城','番禺南村',
'南沙街','海珠赤沙']

# define headless
options=Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)   # open firefox

driver.get("http://210.72.1.216:8080/gzaqi_new/RealTimeDate.html")
def onclick(driver,loaction):#to click
	driver.find_element_by_id("PM25").click()
	driver.find_element_by_id(loaction).click()
	time.sleep(3)
	html = driver.page_source
	return html

def extract_value(td):#to convert data
	tdh=td.prettify(formatter="html")
	vv=tdh.split()[3]
	return vv

def get_information(html):
	soup = BeautifulSoup(html, features='lxml')
	tr_1=soup.find(attrs={'id':'trpm25_value'})#hourly pm2.5 it's for selection
	td_1=tr_1.find(attrs={'id':'pmtow'})
	td_1_value=extract_value(td_1)
	tr_2=soup.find(attrs={'id':'trpm10_value'})#hour1y pm10
	td_2=tr_2.find(attrs={'id':'pmten'})
	td_2_value=extract_value(td_2)
	tr_3=soup.find(attrs={'id':'trso2_value'})#SO2
	td_3=tr_3.find(attrs={'id':'sotwo'})
	td_3_value=extract_value(td_3)
	tr_4=soup.find(attrs={'id':'trno2_value'})#NO2
	td_4=tr_4.find(attrs={'id':'notwo'})
	td_4_value=extract_value(td_4)
	tr_5=soup.find(attrs={'id':'tro31_value'})#o3
	td_5=tr_5.find(attrs={'id':'othree'})
	td_5_value=extract_value(td_5)
	td_total=td_1_value+' '+td_2_value+' '+td_3_value+' '+td_4_value+' '+td_5_value
	return td_total
	
def main():
	for k in location_list:
		html_example=onclick(driver,k)
		data=get_information(html_example)
		value=data.split(' ')
		print ('监测站:'+k+'\n')
		print('pm2.5='+str(value[0])+'微克/立方米')
		print('pm10='+str(value[1])+'微克/立方米')
		print('SO2='+str(value[2])+'微克/立方米')
		print('NO2='+str(value[3])+'微克/立方米')
		print('O3='+str(value[4])+'微克/立方米')
	
	
if __name__ == '__main__':
    main()
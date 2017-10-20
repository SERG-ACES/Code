#!/usr/bin/python
# -*- coding: UTF-8 -*-

#This code is used to obtain the annual average solar insolation and wind speed

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv

url1='https://eosweb.larc.nasa.gov/cgi-bin/sse/grid.cgi?&num=298128&lat='
url2='&submit=Submit&hgt=100&veg=17&sitelev=-999&email=skip@larc.nasa.gov&p=grid_id&p=swv_dwn&p=wspd50m&step=2&lon='

location = pd.read_csv('GRIDDATA.csv')
latitude=location['y']
longitude=location['x']
with open('grid_solar_and_wind.csv','a') as w:
	for i in range(len(longitude)-290):
			lon=longitude[i+290]
			lat=latitude[i+290]
			url=url1+str(lat)+url2+str(lon)
			print(url)
			bs = BeautifulSoup(urlopen(url),'lxml')
			swt = bs.find("table",{'summary':{'Monthly Averaged Insolation Incident On A Horizontal Surface '}})
			sweather=swt.findAll("tr")
			std=sweather[-1].findAll("td")
			solar=std[-1].get_text().replace(' ','')
			wwt = bs.find("table",{'summary':{'Monthly Averaged Wind Speed At 50 m Above The Surface Of The Earth '}})
			wweather=wwt.findAll("tr")
			wtd=wweather[-1].findAll("td")
			wind=wtd[-1].get_text().replace(' ','')
			w.write('%s,%s,%s,%s\n'%(lat,lon,solar,wind))
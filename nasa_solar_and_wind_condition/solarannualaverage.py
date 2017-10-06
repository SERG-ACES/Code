#!/usr/bin/python
# -*- coding: UTF-8 -*-

#This code is used to obtain the annual average solar insolation

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url1='https://eosweb.larc.nasa.gov/cgi-bin/sse/grid.cgi?&num=298128&lat='
url2='&submit=Submit&hgt=100&veg=17&sitelev=-999&email=skip@larc.nasa.gov&p=grid_id&p=swv_dwn&p=wspd50m&step=2&lon='

with open('province_location.csv', 'r') as f:
	with open('province_solar.csv','w') as w:
		location = csv.reader(f)
		for line in location:
			if line[0]!='地区':
				lat=line[2]
				lon=line[1]
				url=url1+str(lat)+url2+str(lon)
				bs = BeautifulSoup(urlopen(url),'lxml')
				wt = bs.find("table",{'summary':{'Monthly Averaged Insolation Incident On A Horizontal Surface '}})
				weather=wt.findAll("tr")
				td=weather[-1].findAll("td")
				x=td[-1].get_text().replace(' ','')
				w.write('%s,%s\n'%(line[0],x))
			else:
				w.write('%s,solar insolation\n'%line[0])
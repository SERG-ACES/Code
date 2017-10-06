#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

url1='https://eosweb.larc.nasa.gov/cgi-bin/sse/grid.cgi?&num=297130&lat='
url2='&submit=Submit&hgt=100&veg=17&sitelev=&email=zhenhuawan@gmail.com&p=grid_id&p=srf_dwn0&p=wspd50m0&step=2&lon='
lat=39.12
lon=117.2
url=url1+str(lat)+url2+str(lon)
bs = BeautifulSoup(urlopen(url),'lxml')
wt = bs.findAll("table",{'summary':{'Monthly Averaged Insolation Incident On A Horizontal Surface At Indicated GMT Times ','Monthly Averaged Wind Speed At 50 m Above The Surface Of The Earth For Indicated GMT Times '}})
for i in wt:
	weather=i.findAll("tr")
	for j in weather:
		td=j.findAll("td")
		for k in td:
			print(k.get_text().replace(' ',''),end=' ')
		print('')
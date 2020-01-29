from lxml import html
import requests
import time
import os

both_subs = []

def pewdsScraper():
	page = requests.get('https://socialblade.com/youtube/user/pewdiepie/realtime')
	tree = html.fromstring(page.content)
	subs = tree.xpath('//h5[@ class="odometer"]/text()')
	print ("pewdiepie has "+ subs[0] + " subscrbers")
	intsubs = int(subs[0].replace(',', ''))
	both_subs.append(intsubs)
	#print(both_subs)
	del subs[:]


def TseriesScraper():
	page = requests.get('https://socialblade.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA/realtime')


	tree = html.fromstring(page.content)
	subs = tree.xpath('//h5[@ class="odometer"]/text()')
	print ("T-series has "+ subs[0] + " subscrbers")
	intsubs = int(subs[0].replace(',', ''))
	both_subs.append(intsubs)
	#print(both_subs)
	del subs[:]

def math():
	#print(both_subs[:])
	first = both_subs[0]
	second = both_subs[1]
	total = int(first) - int(second)
	if total > 0:
		print("pewdiepie is ahead by " + str(total) + " Subscribers")
	else:
		print ("T-series is ahead by " + str(total* -1))
	del both_subs[:]	


while True:
	pewdsScraper()
	TseriesScraper()
	math()
	time.sleep(3)
	os.system('clear')
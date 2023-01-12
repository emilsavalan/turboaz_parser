import requests
from bs4 import BeautifulSoup
import csv

def get_ad(ad_id):
	html = requests.get("https://turbo.az/autos/" + str(ad_id))
	soup = BeautifulSoup(html.text, "html.parser")
	if not soup.find('div', class_="header-top-nav"):
		exit()

	exist = soup.find('ul', class_="product-properties")
	loan=0
	barter=0
	result = [ad_id, loan, barter]
	if not exist:
		return result

	massiv = soup.findAll('div', class_="product-properties-value")
	if len(massiv)-1>13:
		if massiv[14].get_text() == "Kreditdədir":
			loan=1
		if massiv[14].get_text() == "Barter mümkündür":
			barter=1

	if len(massiv)-1>14:
		if massiv[15].get_text() == "Kreditdədir":
			loan=1
		if massiv[15].get_text() == "Barter mümkündür":
			barter=1

	result = [ad_id, loan, barter]
	return result

with open('turboaz_00_cor.csv') as db:
	db_read = csv.reader(db)
	next(db_read)
	for ad_id in db_read:
		with open('turboaz_00_correcting.csv', mode='a', newline='', encoding='UTF-8') as ins:
			insert = csv.writer(ins, delimiter=',', quotechar='"')
			print("trying...."+str(ad_id[0]))
			ad_data=get_ad(ad_id[0])
			insert.writerow(ad_data)
			print("written")
import requests
from bs4 import BeautifulSoup
import csv
import time

with open('turboaz.csv', encoding='utf-8') as db:
	db_read = csv.reader(db)
	last_id = int(list(db_read)[-1][0])
print("The last ad's id is obtained")


def get_ad(aid):
	html = requests.get("https://turbo.az/autos/" + str(aid))
	soup = BeautifulSoup(html.text, "html.parser")
	
	if soup.find('div', class_="site-error"):
		return None

	if not soup.find('div', class_="header-top-nav"):
		exec(open("tplink.py").read())
		return 'IP'

	exist = soup.find('ul', class_="product-properties")

	if not exist:
		return None

	massiv = soup.findAll('div', class_="product-properties-value")
	# properties = [pt.get_text() for pt in massiv]

	region = massiv[0].get_text()
	make_id = massiv[1].get_text()
	model = massiv[2].get_text()
	year = massiv[3].get_text()
	ban = massiv[4].get_text()
	color = massiv[5].get_text()
	engine = massiv[6].get_text()[:-2]
	power = massiv[7].get_text()[:-5]
	fuel_type = massiv[8].get_text()
	mileage = massiv[9].get_text()[:-2].replace(' ', '')
	transmission = massiv[10].get_text()
	gear = massiv[11].get_text()

	if massiv[12].get_text() == "Bəli":
		new=1
	else:
		new=0

	if massiv[13].find('span').get_text() == "$":
		price = int(massiv[13].find('div').get_text()[:-1].replace(' ', ''))*1.7

	if massiv[13].find('span').get_text() == "AZN":
		price = int(massiv[13].find('div').get_text()[:-3].replace(' ', ''))

	if massiv[13].find('span').get_text() == "€":
		return None
		exit();

	loan=0
	barter=0
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

	extras = soup.findAll('p', class_="product-extras-i")

	ac=0
	leather=0
	sun_roof=0

	for extra in extras:
		if extra.get_text() == "Kondisioner":
			ac=1
		if extra.get_text() == "Lyuk":
			leather=1
		if extra.get_text() == "Dəri salon":
			sun_roof=1

	date = soup.findAll('div', class_="product-statistics")[0].findAll('p')[1].get_text()
	dates=date.split(" ")
	date_month = dates[2]
	date_year = dates[3]
	result = [aid, region, make_id, model, year, ban, color, engine, power, fuel_type, mileage, transmission, gear, new, price, loan, barter, ac, leather, sun_roof, date_year, date_month]
	return result



with open('turboaz.csv', mode='a', newline='', encoding='UTF-8') as ins:
	insert = csv.writer(ins, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	x=last_id+1
	while x<3669200:
		print("trying...."+str(x))
		ad_data=get_ad(x)
		if not ad_data:
			x=x+1
			continue
		if ad_data =='IP':
			time.sleep(60)
			continue
		insert.writerow(ad_data)
		print(str(x)+"th ad's data was written to file")
		x=x+1

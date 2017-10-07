import requests
import os
import json
import datetime

def current_weather():
	city = raw_input('\nEnter a city: ')
	url = 'http://api.openweathermap.org/data/2.5/weather?q='+str(city)+'&appid=fc8daefb1e89120464ca7213c044a694'
	response = requests.get(url)
	t = json.loads(response.text)
	try:
		temp = t['main']['temp']						#unit: Kelvin
		humidity = t['main']['humidity']				#unit: in %
		description = t['weather'][0]['description']
		pressure = t['main']['pressure']				#unit: hPa
		clouds = t['clouds']['all']						#unit: in %
		wind_speed = t['wind']['speed']					#unit: m/s
		wind_dir = t['wind']['deg']						#unit: degrees
		dt = t['dt']									#date in Unix, UTC
		city_id = t['id']
		city_name = t['name'] 

		date = (datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S'))

		print '\nWeather forecast of "'+city_name+'" as on '+str(date)+':'
		print 'Description 		: '+description
		# print '\nCity: '+city_name
		print 'Temperature 		: '+str(temp)+' Kelvin'
		print 'Pressure 		: '+str(pressure)+' hPa'
		print 'Humidity 		: '+str(humidity)+'%'
		print 'Cloudiness 		: '+str(clouds)+'%'
		print 'Wind speed 		: '+str(wind_speed)+' m/s at '+str(wind_dir)+' degrees'

	except KeyError:
		print "\nSorry, couldn't find data for '"+city+"'!\n"


def driver():
	current_weather()
	while(1>0):
		choice = raw_input('\nTo continue press 1 or press any key to exit: ')
		if(choice == '1'):
			current_weather()
		else:
			print '\nThank you for using!'
			break

driver()



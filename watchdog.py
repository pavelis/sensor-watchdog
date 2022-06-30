import os
import sys
import json
import requests
from dotenv import load_dotenv



load_dotenv()

try:
	sensor_user_name = os.environ['SENSOR_USER_NAME']
	sensor_password = os.environ['SENSOR_PASSWORD']
	sensor_id = os.environ['SENSOR_ID']
	sensor_url = os.environ['SENSOR_URL']
except KeyError as e:
	print("Environment variables not set")
	sys.exit(1)

data_url = f"https://data.sensor.community/airrohr/v1/sensor/{sensor_id}/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

try:
	response = requests.get(data_url, headers=headers)
	response.encoding = 'utf-8'
	if len(response.json()) == 0:
		try:
			basic = requests.auth.HTTPBasicAuth(sensor_user_name, sensor_password)
			print(f"Restarting...")
			response = requests.put(f"{sensor_url}reset", data={"submit":"Restart"}, headers=headers, auth=basic, timeout=2)
		except requests.exceptions.Timeout:
			pass
		except requests.exceptions.RequestException:
			print("Could not access sensor page")
except requests.exceptions.RequestException as e:
	print("Could not get data page")

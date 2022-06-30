# Watchdog for a sensor.community sensor

The script checks if the sensor doesn't send data to sensor.community website and restarts it.


## Installation

`git clone`

`cd sensor-watchdog`

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`


## Setting up

Rename `.env.example` file to `.env`

`mv .env.example .env`

Edit the file:

`
SENSOR_USER_NAME=""
SENSOR_PASSWORD=""
SENSOR_ID=""
SENSOR_URL="http://192.168.0.1/"
`

`SENSOR_USER_NAME` is a user name for sensor configuration (default is `admin`)

`SENSOR_PASSWORD` is a password for sensor configuration

By default, a sensor's authentication is disabled, thus these fields should be blank.

`SENSOR_ID` is a sensor's ID, as it shown on the map: https://maps.sensor.community/ after the `#` sign.

`SENSOR_URL` is a sensor's URL in a local network or accessible through the Internet.


## Scheduling




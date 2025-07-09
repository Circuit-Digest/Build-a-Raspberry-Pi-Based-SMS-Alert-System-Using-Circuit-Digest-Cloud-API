import time
import requests
import adafruit_dht
import board
import RPi.GPIO as GPIO
from datetime import datetime

# === USER CONFIGURATION ===
API_KEY = 'xxxxxxxxxx'      # Your API Key
TEMPLATE_ID = '102'
MOBILE_NUMBER = '91xxxxxxxxxx'  # Target Mobile Number
LOCATION = 'Home'
TEMP_THRESHOLD = 33             # °C: Trigger SMS if temp exceeds this
READ_INTERVAL = 10              # Seconds between sensor reads
COOLDOWN_TIME = 60              # Seconds to wait after sending SMS
API_URL = f'https://www.circuitdigest.cloud/send_sms?ID={TEMPLATE_ID}'

# === GPIO PINS ===
DHT_PIN = board.D4              # GPIO4 = Pin 7
GREEN_LED = 23                  # GPIO23 = Pin 16 (Success)
RED_LED = 24                    # GPIO24 = Pin 18 (Failure)

# === GPIO SETUP ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# === DHT11 SENSOR SETUP ===
dht = adafruit_dht.DHT11(DHT_PIN)

# === LED FEEDBACK FUNCTION ===
def led_feedback(success):
    if success:
        GPIO.output(GREEN_LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GREEN_LED, GPIO.LOW)
    else:
        GPIO.output(RED_LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RED_LED, GPIO.LOW)

# === SMS SEND FUNCTION ===
def send_sms(temp):
    current_time = datetime.now().strftime("%I:%M %p")
    var1 = f"{LOCATION} at {current_time}"
    var2 = f"{temp}C"

    payload = {
        "mobiles": MOBILE_NUMBER,
        "var1": var1,
        "var2": var2
    }

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"[OK] SMS sent: {var1}, Temp = {var2}")
            print("Response:", response.json())
            led_feedback(True)
        else:
            print(f"[ERROR] SMS failed. Status: {response.status_code}")
            print("Response:", response.text)
            led_feedback(False)
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)
        led_feedback(False)

# === MAIN LOOP ===
print("Monitoring temperature... (Press Ctrl+C to stop)")
try:
    while True:
        try:
            temperature = dht.temperature
            humidity = dht.humidity

            if temperature is not None:
                print(f"Temperature: {temperature}C | Humidity: {humidity}%")
                if temperature > TEMP_THRESHOLD:
                    send_sms(temperature)
                    time.sleep(COOLDOWN_TIME)  # Prevent repeated alerts
            else:
                print("Sensor read failed.")

        except Exception as sensor_error:
            print("Sensor error:", sensor_error)

        time.sleep(READ_INTERVAL)

except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    GPIO.cleanup()

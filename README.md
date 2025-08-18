# Raspberry Pi-Based SMS Alert System Using Circuit Digest Cloud API

A modern, Wi-Fi-based SMS alert system that monitors temperature using a DHT11 sensor and sends real-time alerts to your phone - no GSM modules or SIM cards required.

## 🚀 Project Overview

This project creates a [temperature monitoring system](https://circuitdigest.com/microcontroller-projects/raspberry-pi-based-sms-alert-system-using-cloud-api) using a Raspberry Pi that sends SMS alerts when temperature thresholds are exceeded. The system uses the Circuit Digest Cloud API to send messages over Wi-Fi, making it simple and cost-effective compared to traditional GSM-based solutions.

**Key Features:**
- Real-time temperature monitoring with DHT11 sensor
- Wi-Fi-based SMS alerts (no SIM card needed)
- Visual feedback with LED indicators
- Configurable temperature thresholds
- Anti-spam cooldown mechanism
- Easy setup and deployment

## 🛠️ Components Required

| Component | Quantity |
|-----------|----------|
| Raspberry Pi (any model 3,4,5) | 1 |
| DHT11 Temperature Sensor | 1 |
| 220Ω Resistors (for LEDs) | 1 |
| LEDs (Red, Green) | 2 |
| Breadboard & Jumper Wires | As needed |

## 📋 Prerequisites

### Raspberry Pi Setup
1. Install latest Raspberry Pi OS using the official Raspberry Pi Imager
2. Connect to internet (Wi-Fi or Ethernet)
3. Update system packages:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

### Python Library Installation

Due to PEP 668 restrictions on newer Raspberry Pi OS versions, you have two installation options:

**Option 1: Override system packages (quick but not recommended)**
```bash
sudo pip3 install --break-system-packages Adafruit_DHT requests
```

**Option 2: Virtual environment (recommended)**
```bash
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip install Adafruit_DHT requests
```

## 🔧 Circuit Digest Cloud Setup

### Account Registration
1. Visit [Circuit Digest Cloud](https://circuitdigest.cloud)
2. Click "Login" → "Register Now" for new users
3. Complete registration with email, username, and password
4. Log in with your credentials

### API Key Generation
1. Navigate to "My Account" in the top-right corner
2. Complete the captcha verification
3. Click "Generate API Key"
4. Copy your API key for use in the code

### Mobile Number Verification
**Important:** You must verify your mobile number using OTP authentication before receiving SMS alerts. This prevents spam and ensures authorized usage.

### API Usage Limits
- SMS API Keys: 100 requests per key
- Generate new keys when quota is exhausted
- Fair use policy applies

## 🔌 Hardware Wiring

### Pin Connections
- **DHT11 Sensor:** GPIO4 (Pin 7)
- **Green LED:** GPIO23 (Pin 16)
- **Red LED:** GPIO24 (Pin 18)
- **Ground:** Connect all ground pins to common ground rail


## 📝 SMS Templates

The system uses template ID `102` for temperature alerts:

**Template 102 - Temperature Alert:**
```
The temperature in {#var1#} has reached {#var2#}°C. Please take necessary action.
-- 
Powered by CircuitDigest for the Engineers and Makers of India. Visit www.circuitdigest.com.
```

Variables:
- `var1`: Location and timestamp (e.g., "Home at 02:45 PM")
- `var2`: Temperature value (e.g., "34")

## ⚙️ Configuration

Update the following variables in the code:

```python
API_KEY = 'your_api_key_here'           # Your Circuit Digest API Key
TEMPLATE_ID = '102'                     # Temperature alert template
MOBILE_NUMBER = '91xxxxxxxxxx'          # Target mobile number with country code
LOCATION = 'Home'                       # Location label for SMS
TEMP_THRESHOLD = 33                     # °C: Trigger SMS if temp exceeds this
READ_INTERVAL = 10                      # Seconds between sensor reads
COOLDOWN_TIME = 60                      # Seconds to wait after sending SMS
```

## 🚀 Running the System

1. **Navigate to project directory:**
   ```bash
   cd /path/to/your/project
   ```

2. **Activate virtual environment (if using):**
   ```bash
   source myenv/bin/activate
   ```

3. **Run the monitoring script:**
   ```bash
   python3 sms_alert_system.py
   ```

4. **Monitor output:**
   ```
   Monitoring temperature... (Press Ctrl+C to stop)
   Temperature: 25C | Humidity: 45%
   Temperature: 35C | Humidity: 50%
   [OK] SMS sent: Home at 02:45 PM, Temp = 35C
   ```

## 🔍 System Behavior

### Normal Operation
- Continuously monitors temperature every 10 seconds
- Displays temperature and humidity readings
- Green LED blinks when SMS is sent successfully
- Red LED blinks when SMS sending fails

### Alert Triggering
- SMS sent when temperature exceeds threshold (default: 33°C)
- 60-second cooldown prevents spam alerts
- Visual feedback via LED indicators

### Error Handling
- Sensor read failures are logged and retried
- Network connection errors trigger red LED
- Graceful shutdown with Ctrl+C

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| SMS not received | Ensure mobile number is verified in Circuit Digest account |
| Library install fails | Use `--break-system-packages` or create virtual environment |
| Network timeout | Check internet connection with `ping www.google.com` |
| GPIO pins don't respond | Verify pin numbers (BCM vs physical numbering) |
| Sensor read errors | Normal for DHT11 - system retries automatically |

## 📊 Testing

1. **Heat the sensor** with warm air or hair dryer
2. **Watch console output** for temperature readings
3. **Verify SMS delivery** when threshold is exceeded
4. **Check LED feedback** for success/failure indication


## 🤝 Contributing

We welcome contributions and would love to see how you use this system! Feel free to:
- Submit bug reports and feature requests
- Share your project implementations
- Suggest new SMS templates
- Improve documentation

**Happy Building!** 🎉

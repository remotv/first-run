# Critical bug in hostapd (the one bit of software for hosting networks) stops this project dead in its tracks until it's fixed.

# first-run
A simple wireless network and web server to help pre-built robots connect to the internet.

I'd like this to

1. Host a wireless hotspot with captive portal

2. In the portal, either a form with SSID and PSK or a dynamic list of all available connections ordered by connection strength

3. Stop the wireless server and attempt connection to the selected/entered network

4. Restart the server if it cannot connect.

## Installation
- Recommend using a virtualenvironment
- designed for python3

```
pip3 install -r requirements.txt
python3 app.py
```

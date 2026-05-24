#!/bin/bash
# ============================================================
# start-dashboard.sh
# Place at: /home/pi/start-dashboard.sh
# chmod +x /home/pi/start-dashboard.sh
#
# This script is called on boot via:
#   ~/.config/autostart/dashboard.desktop
# ============================================================

# Wait for desktop to fully load
sleep 5

# Start Flask in the background, log output to a file
python3 /home/pi/boat-dashboard/app.py >> /home/pi/dashboard.log 2>&1 &

# Wait for Flask to be ready before launching browser
sleep 3

# Hide the mouse cursor (install unclutter first: sudo apt install unclutter)
unclutter -idle 0 &

# Launch Chromium in kiosk mode — no address bar, no cursor, no popups
chromium-browser \
  --kiosk \
  --noerrdialogs \
  --disable-infobars \
  --no-first-run \
  --disable-translate \
  --disable-features=TranslateUI \
  --check-for-update-interval=31536000 \
  http://localhost:5000

"""
random: is to generate fake noise for simulation
math: is to be able to generate the sine wave for depth simulation
time: is for the clock and timestamps
threading: is so the sensor loop can be going in the background while Flask serves requests

"""
import random
import math
import time
import threading
import advisor

"""
sensor_data: is a dictionary that holds the "fake" sensor readings. In a real implementation, you'd update this with actual hardware readings.

"""

sensor_data = {
    "depth":      12.4,   # feet
    "speed":       0.0,   # mph
    "heading":     182,   # degrees 0-359
    "lat":       38.8977,
    "lon":      -77.0365,
    "water_temp": 68.2,   # °F
    "battery":    12.6,   # volts
    "timestamp":    "",
    "advisor":      {},
}

"""
_mock: The underscore means "internal use only". This is just used to make the fake valuyes move smoothly in between ticks

"""
_mock = {
    "speed_target":  4.0,
    "heading_drift": 0.0,
    "depth_base":   12.0,
}

"""
read_sensors: the main function that updates every key in sensor_data. 
"""
_last_advisor_update = 0
 
def read_sensors():
    """Update sensor_data with the latest readings."""

    # -- Speed: drift toward a slowly wandering target --
    _mock["speed_target"] += random.uniform(-0.3, 0.3)
    _mock["speed_target"]  = max(0.0, min(12.0, _mock["speed_target"]))
    sensor_data["speed"]   = round(
        sensor_data["speed"]
        + (_mock["speed_target"] - sensor_data["speed"]) * 0.1
        + random.uniform(-0.05, 0.05),
        1
    )

    # -- Heading: slow random drift --
    _mock["heading_drift"] += random.uniform(-1.5, 1.5)
    sensor_data["heading"]  = int(
        (sensor_data["heading"] + _mock["heading_drift"] * 0.2) % 360
    )

    # -- Depth: random walk + a gentle sine wave on top --
    _mock["depth_base"] += random.uniform(-0.1, 0.1)
    _mock["depth_base"]  = max(4.0, min(40.0, _mock["depth_base"]))
    sensor_data["depth"] = round(
        _mock["depth_base"] + math.sin(time.time() * 0.3) * 0.4,
        1
    )

    # -- GPS: tiny drift to simulate slow movement --
    sensor_data["lat"] += random.uniform(-0.00002, 0.00002)
    sensor_data["lon"] += random.uniform(-0.00002, 0.00002)

    # -- Water temp + battery: barely move --
    sensor_data["water_temp"] = round(
        sensor_data["water_temp"] + random.uniform(-0.05, 0.05), 1
    )
    sensor_data["battery"] = round(
        12.6 + random.uniform(-0.05, 0.05), 2
    )

    sensor_data["timestamp"] = time.strftime("%H:%M:%S")

    now = time.time()
    if now - _last_advisor_update >= 30:
        advice = advisor.get_advice(sensor_data)
        sensor_data["advisor"] = advice["advisor"]
        _last_advisor_update = now

"""
this loop runs infinietly. Calls the functions then waits half a second then calls again.
"""

def _loop():
    while True:
        read_sensors()
        time.sleep(0.5)

"""
New thread, only thing that is called from app.py
"""
def start():
    """Start the sensor background thread."""
    t = threading.Thread(target=_loop, daemon=True)
    t.start()
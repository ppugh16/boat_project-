"""
app.py
=======
Flask routes only. No sensor logic lives here.

Run:  python3 app.py
Open: http://localhost:5000
"""

from flask import Flask, render_template, Response, jsonify, request
import json
import time

import sensors

app = Flask(__name__)
sensors.start()

# ---------------------------------------------------------------------------
# DASHBOARD CONFIG
# ---------------------------------------------------------------------------

config = {
    "vessel_name": "MV MOCKINGBIRD",
    "species_list": [
        "Largemouth Bass",
        "Striped Bass",
        "Crappie",
        "Bluegill",
        "Catfish"
    ],
    "bait_list": [
        "Plastic Worm",
        "Spinnerbait",
        "Crankbait",
        "Jig",
        "Live Minnow"
    ]
}

# ---------------------------------------------------------------------------
# ROUTES
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html", config=config)


@app.route("/api/data")
def api_data():
    """JSON snapshot — open in browser to debug sensor values."""
    return jsonify(sensors.sensor_data)


@app.route("/api/log-catch", methods=["POST"])
def log_catch():
    """
    Receives a catch log from the dashboard form.
    Stores current GPS, depth, and water temperature alongside
    the selected species and bait.
    """
    body = request.form

    catch = {
        "timestamp":  time.strftime("%Y-%m-%d %H:%M:%S"),
        "species":    body.get("species", "Unknown"),
        "bait":       body.get("bait", "Unknown"),
        "lat":        sensors.sensor_data.get("lat"),
        "lon":        sensors.sensor_data.get("lon"),
        "depth":      sensors.sensor_data.get("depth"),
        "water_temp": sensors.sensor_data.get("water_temp"),
    }

    # TODO: Replace this with database storage later.
    print(f"CATCH LOGGED: {catch}")

    return jsonify({
        "status": "ok",
        "message": "Catch logged successfully.",
        "catch": catch
    })


@app.route("/stream")
def stream():
    """SSE — browser connects once, we push data every 500 ms."""
    def generate():
        while True:
            yield f"data: {json.dumps(sensors.sensor_data)}\n\n"
            time.sleep(0.5)

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
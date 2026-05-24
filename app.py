"""
Imports all necessary flask libraries
Imports sensors file 
"""

from flask import Flask, render_template, Response, jsonify
import json
import time

import sensors

"""
starts the background thread befores accpting any requests
"""
app = Flask(__name__)

sensors.start()

"""
HTML page when somone visits the URL 
"""

@app.route("/")
def home():
    return render_template("index.html")

"""
Returns the current sensor data
"""
@app.route("/api/data")
def api_data():
    """JSON snapshot of current readings. Handy for debugging in the browser."""
    return jsonify(sensors.sensor_data)


"""
"server-sent events": this route is used to real-time update the dashboard. It yields chunkks of data so that the connection can stay open and update whenever new data is ready
"""
@app.route("/stream")
def stream():
    def generate():
        while True:
            yield f"data: {json.dumps(sensors.sensor_data)}\n\n"
            time.sleep(0.5)

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control":    "no-cache",
            "X-Accel-Buffering": "no",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
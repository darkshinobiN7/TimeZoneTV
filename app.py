from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# Function to get formatted time for each timezone
def get_timezones():
    timezones = {
        "Dublin": "Europe/Dublin",
        "PST": "America/Los_Angeles",
        "EST": "America/New_York"
    }
    
    current_times = {
        tz: datetime.now(pytz.timezone(zone)).strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
        for tz, zone in timezones.items()
    }
    
    return current_times

@app.route("/")
def index():
    return render_template("index.html", times=get_timezones())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

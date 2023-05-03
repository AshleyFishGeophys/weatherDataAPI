import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pd.read_csv("")
    # temperature = df.station(date)
    temperature = 23
    return {"Station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    # Specifying the port allows multiple Flask apps to run at the same time.
    app.run(debug=True, port=5001)

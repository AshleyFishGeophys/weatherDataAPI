import pandas as pd
from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # zfill adds zeros before number, which is what we need for the correct format
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10
    return {"Station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    # Specifying the port allows multiple Flask apps to run at the same time.
    app.run(debug=True, port=5000)

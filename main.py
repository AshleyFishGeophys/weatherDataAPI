import pandas as pd
from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    # To convert the df to html, just use df.to_html()
    return render_template("home.html", data=stations.to_html())


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

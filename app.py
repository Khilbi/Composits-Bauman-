from flask import Flask, render_template,request
from preprocessing import get_prediction

app = Flask(__name__)


@app.route("/", methods=["get", "post"])  # 127.0.0.1:5000/
def index():
    message = "Здесь будут результаты прогноза"
    if request.method == "POST":
        plotnost = request.form.get("plotnost")
        
        
        modul_uprugosti = get_prediction(float(plotnostn))
        message = f"Модуль упругости при растяжении при заданных параметрах составит {modul_uprugosti} ГПа"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()


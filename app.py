import flask
from flask import Flask, render_template,request
from processing import get_prediction
import sklearn
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/", methods=["get", "post"])  # 127.0.0.1:5000/
def index():
    message = "Здесь будут результаты прогноза"
    if request.method == "POST":
        plotnost = request.form.get("plotnost")
        modulupr = request.form.get("modulupr")
        amount = request.form.get("amount")
        epoks = request.form.get("epoks")
        tepm = request.form.get("tepm")
        poverkhplotn = request.form.get("poverkhplotn")
        smol = request.form.get("smol")
        shag = request.form.get("shag")
        plotnostn = request.form.get("plotnostn")
        mat = request.form.get("mat")
        ugol = request.form.get("ugol")
        
        modul_uprugosti = get_prediction(float(plotnost),float(modulupr),float(amount),
                                         float(epoks),float(tepm),float(poverkhplotn),
                                         float(smol),float(shag),float(plotnostn),
                                         float(mat),float(ugol))
        message = f"Модуль упругости при растяжении при заданных параметрах составит {modul_uprugosti} ГПа"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()



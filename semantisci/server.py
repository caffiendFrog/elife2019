import os
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Guess what? Chicken butt.'

@app.route("/")
def index():
    return render_template("index.html",
                           id="PMC2902",
                           candidates=["monkey", "purple", "green"],
                           message="In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan), In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan) In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan)")

@app.route("hello")
def hello():


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
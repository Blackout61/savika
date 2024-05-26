from flask import Flask, render_template, redirect, session, url_for, request
import os
from myForms import *
from savikaResults import savika_results, model_giris_degerleri
import pandas as pd

app = Flask(__name__)

SECRET_KEY = os.urandom(24)

app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    return render_template("anasayfa.html")


@app.route("/sartname", methods=["GET", "POST"])
def sartname():
    form = MyForm()

    try:
        results = session['results']
        session.pop("results")
    except:
        results = []

    if request.method == 'POST':

        results.append(form.radio_btn.data)
        results.append(form.radio_btn_2.data)
        results.append(form.radio_btn_3.data)
        results.append(form.radio_btn_4.data)
        results.append(form.radio_btn_5.data)
        results.append(form.radio_btn_6.data)
        results.append(form.radio_btn_7.data)
        results.append(form.radio_btn_8.data)

        session["results"] = results
        if len(results) >= 0:
            with open("save_file.txt", "w", encoding="utf-8") as f:
                f.write(" \n".join(results))

        savika = savika_results(results)

        if len(savika) >= 0:
            with open("save_savika_file.txt", "w", encoding="utf-8") as f:
                f.write(" \n".join([value for value in savika.values()]))

        return redirect(url_for("sartnameSonuc", results=results))

    elif request.method == "GET":
        render_template("sartname.html", form=form, results=results)

    return render_template("sartname.html", form=form, results=results)


@app.route("/sartnameSonuc")
def sartnameSonuc():
    try:
        results = session["results"]
        savika = savika_results(results)
        res = model_giris_degerleri(savika)

        print("//////////////////////////////////////////")

        print("Response Log ***", res)
        print("//////////////////////////////////////////")
        df = pd.DataFrame(res)
        print("DF => ", df)

    except:
        results = []
        savika = {}
    return render_template("sartnameSonuc.html", results=results, res=res)


@app.route("/veriTabani")
def veriTabani():

    data = pd.read_excel("VeriSeti.xlsx")

    data = data.to_numpy()

    return render_template("veriTabani.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)

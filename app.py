from flask import Flask, render_template, redirect, session, url_for, request
import os
from savika.myForms import *
from savika.savikaResults import savika_results, model_giris_degerleri, model_sonuc
import time

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

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
        session['model_sonuc'] = res

    except:
        results = []
        savika = {}

    return render_template("sartnameSonuc.html", results=results, res=res)



@app.route("/modelSonuc", methods=["GET", "POST"])
def modelSonuc():

    time.sleep(6)
    secimler = session['model_sonuc']
    savika = session['results']
    results_ = savika_results(savika)
    results_ = list(results_.values())

    res = model_sonuc(secimler)

    del results_[0]
    del results_[5]

    param = [
        "Sınıf",
        "Özerk Yapı",
        "Kontrol Sistemi",
        "Faydalı Yük",
        "Motor",
        "Yönlendirme Sistemi",
        "Süspansiyon Sistemi",
        "Gövde Malzemesi",
        "Enerji Sistemi",
        "Güç Aktarma Sistemi",
        "Fren Sistemi",
        "Isı Yönetim Sistemi",
        "Elektrik Sistemi",
        "Elektronik Üniteler",
        "İntikal Konfigürasyonu",
        "Şasi"
    ]

    results_.insert(14, res)
    results_.insert(15, f"{res} Şasi")

    path2d = f"/imgs/2D/{results_[0][0]}{results_[14][0]}{results_[3][0]}.jpg"
    path3d = f"/imgs/3D/{results_[0][0]}{results_[14][0]}{results_[3][0]}.glb"

    session['model_sonuc2'] = results_

    rapor=[] + results_
    rapor.append(path2d)

    with open("savika_rapor.txt", "w", encoding="utf-8") as f:
        f.write(" \n".join([value for value in results_]))   

    session["savika_rapor"]=rapor

    return render_template(
        "modelSonuc.html",
        res=res,
        results_=results_,
        img_3=path3d,
        img_2=path2d,
        param=param,
    )


@app.route("/hakkinda")
def hakkinda():
    return render_template("hakkinda.html")

@app.route("/tanitim")
def tanitim():
    return render_template("tanitim.html")
    # session.clear()

@app.route("/yardim")
def yardim():
    return render_template("yardim.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

@app.route("/savikaRapor")
def savikaRapor():
    time.sleep(6)
    result=session["savika_rapor"]
    secimler= session["results"]
    return render_template("savikaRapor.html",result=result, secimler=secimler)

if __name__ == "__main__":
    app.run(debug=True, port=6161)

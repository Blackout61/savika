import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model  # type:ignore


class SavikaResults():

    def __init__(self, results):
        self.results = results

    def maliyet(self):
        pass

    def agirlikSinifi(self):
        pass

    def ozerkYapi(self):
        pass

    def kontrolSis(self):
        pass

    def faydaliYuk(self):
        pass

    def motor(self):
        pass

    def araziTipi(self):
        pass

    def yonlendirmeSis(self):
        pass

    def intikalKonfig(self):
        pass

    def suspansiyonSis(self):
        pass

    def enerjiSis(self):
        pass

    def gucAktarmaSis(self):
        pass

    def frenSis(self):
        pass

    def isiYonetimSis(self):
        pass

    def elektrikSis(self):
        pass

    def govdeMalzeme(self):
        pass

    def elektronikUnite(self):
        pass

    def sasi(self):
        pass


def savika_results(results):
    """
    Yapilan secimlere göre Makina öğrenmesi ve belli başlı parametrelerin
    belirlenmesi için kullanici secimlerinden anlamlı sonuçların cıkarılması işlemi

    """

    maliyet = ""
    agirlikSinifi = ""
    ozerkYapi = ""
    kontrolSis = ""
    faydaliYuk = ""
    motor = ""
    araziTipi = ""
    yonlendirmeSis = ""
    intikalKonfig = "Makina Öğrenmesi Sonra Hesaplanacak"
    suspansiyonSis = ""
    enerjiSis = ""
    gucAktarmaSis = ""
    frenSis = ""
    isiYonetimSis = ""
    elektrikSis = ""
    govdeMalzeme = ""
    elektronikUnite = ""
    sasi = "Makina Öğrenmesi Sonra Hesaplanacak"

    # 1 - Maliyet:
    maliyet = results[0]

    # 2 - Ağırlık Sınıfı:

    option_one = "Uzunluk: 0-1 m | Genişlik: 0-0.5 m | Yükseklik: 0-0.5 m | Dik Engel Aşma: 0-0.5 m | Hendek Aşma: 0-0.5 m | Eğim: 40-60% | Ağırlık: 0-200 kg"
    option_two = "Uzunluk: 1-3 m | Genişlik: 0.5-2 m | Yükseklik: 0.5-1 m | Dik Engel Aşma: 0-0.5 m | Hendek Aşma: 0-0.5 m | Eğim: 40-60% | Ağırlık: 200-1000 kg"
    option_three = "Uzunluk: 2-6 m | Genişlik: 1-3 m | Yükseklik: 1-2 m | Dik Engel Aşma: 0.5-1.5 m | Hendek Aşma: 0.5-1.5 m | Eğim: 40-60% | Ağırlık: 1000-15000 kg"
    option_four = "Uzunluk: 6+ m | Genişlik: 2+ m | Yükseklik: 2+ m | Dik Engel Aşma: 1.5+ m | Hendek Aşma: 1.5+ m | Eğim: 40-60% | Ağırlık: 15000+ kg"

    if (results[0] == "0-30000$" and results[1] == option_one):
        agirlikSinifi = "Hafif Sınıf"
    elif (results[0] == "0-30000$" and results[1] == option_two):
        agirlikSinifi = "Küçük Sınıf"
    elif (results[0] == '30000$-100000$' and results[1] == option_two):
        agirlikSinifi = "Küçük Sınıf"
    elif (results[0] == '0-30000$' and results[1] == option_three):
        agirlikSinifi = "Orta Sınıf"
    elif (results[0] == '30000$-100000$' and results[1] == option_three):
        agirlikSinifi = "Orta Sınıf"
    elif (results[0] == '100000$ +' and results[1] == option_three):
        agirlikSinifi = "Orta Sınıf"
    elif (results[0] == '30000$-100000$' and results[1] == option_four):
        agirlikSinifi = "Ağır Sınıf"
    elif (results[0] == '100000$ +' and results[1] == option_four):
        agirlikSinifi = "Ağır Sınıf"

    # 3 - Özerk Yapı

    if (results[2] == "1. Seviye"):
        ozerkYapi = "Manuel"
    elif (results[2] == "2. Seviye"):
        ozerkYapi = "Yarı-Otonom"
    elif (results[2] == "3. Seviye"):
        ozerkYapi = "Otonom"

    # 4 - Kontrol Sistemi

    if (results[3] == "x<2 km\u00B2"):
        kontrolSis = "RF Kumanda"
    elif (results[3] == "x<5 km\u00B2"):
        kontrolSis = "Uzaktan Kumanda Modulu"
    elif (results[3] == "x km\u00B2"):
        kontrolSis = "Uydu"

    # 5 - Faydalı Yük

    if ((agirlikSinifi == "Hafif Sınıf" or agirlikSinifi == "Küçük Sınıf" or agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and results[4] == "Keşif, Gözetleme ve İstihbarat"):
        faydaliYuk = "Gözetleme Sistemi"

    elif ((agirlikSinifi == "Hafif Sınıf" or agirlikSinifi == "Küçük Sınıf" or agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and results[4] == "Bomba İmha"):
        faydaliYuk = "Manipülatör Sistemi"

    elif ((agirlikSinifi == "Küçük Sınıf" or agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and results[4] == "Lojistik"):
        faydaliYuk = "Taşıyıcı Sistemi"

    elif ((agirlikSinifi == "Küçük Sınıf" or agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and results[4] == "Saldırı ve Geri Emniyet"):
        faydaliYuk = "Silah Sistemi"

    elif ((agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and results[4] == "Mayın ve Engel Temizleme"):
        faydaliYuk = "Mayın ve Engel Temizleme Sistemi"

    # 6 - Motor

    motor = results[5]

    # 7 - Arazi Tipi

    araziTipi = results[6]

    # 8 - Yönlendirme Sistemi

    if (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"

    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"

    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"

    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Ackerman Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"

    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"

    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"

    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Skid-Steer Yönlendirme Sistemi"

    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Düz-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Sert Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Geniş Dönüş Yarıçapı"):
        yonlendirmeSis = "4WS Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Orta Dönüş Yarıçapı"):
        yonlendirmeSis = "Aktif Dönüşlü Yönlendirme Sistemi"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and araziTipi == "Engebeli-Yumuşak Zemin" and results[7] == "Dar Dönüş Yarıçapı"):
        yonlendirmeSis = "Diferansiyel Yönlendirme Sistemi"

    # 9 - İntikal Konfigurasyonu
    # Makine öğrenmesinden gelen sonucu alicaz.

    # 10 -  Suspansiyon Sistemi

    if (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Diferansiyel Yönlendirme Sistemi" or yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "Skid-Steer Yönlendirme Sistemi")):
        suspansiyonSis = "Kauçuk-Elastomerik"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Diferansiyel Yönlendirme Sistemi" or yonlendirmeSis == "Ackerman Yönlendirme Sistemi" or yonlendirmeSis == "Skid-Steer Yönlendirme Sistemi")):
        suspansiyonSis = "Yay ve Amortisör Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Skid-Steer Yönlendirme Sistemi")):
        suspansiyonSis = "Yay ve Amortisör Sistemi"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "MacPherson"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Skid-Steer Yönlendirme Sistemi")):
        suspansiyonSis = "Yay ve Amortisör Sistemi"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Diferansiyel Yönlendirme Sistemi" or yonlendirmeSis == "Ackerman Yönlendirme Sistemi")):
        suspansiyonSis = "MacPherson"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Skid-Steer Yönlendirme Sistemi")):
        suspansiyonSis = "Burulabilen Mil"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "Çift Salıncaklı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "Katı Aks"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Diferansiyel Yönlendirme Sistemi")):
        suspansiyonSis = "Burulabilen Mil"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "Hidropnömatik"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Skid-Steer Yönlendirme Sistemi")):
        suspansiyonSis = "Burulabilen Mil"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin") and (yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "Çift Salıncaklı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "Katı Aks"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi")):
        suspansiyonSis = "Hidropnömatik"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Diferansiyel Yönlendirme Sistemi")):
        suspansiyonSis = "Burulabilen Mil"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and (araziTipi == "Düz-Sert Zemin" or araziTipi == "Düz-Yumuşak Zemin" or araziTipi == "Engebeli-Yumuşak Zemin" or araziTipi == "Engebeli-Sert Zemin") and (yonlendirmeSis == "Aktif Dönüşlü Yönlendirme Sistemi" or yonlendirmeSis == "4WS Yönlendirme Sistemi")):
        suspansiyonSis = "Hidropnömatik"

    # 11 - Enerji Sistemi:

    if (agirlikSinifi == "Hafif Sınıf" and motor == "0-20 kw - Elektrikli"):
        enerjiSis = "Pil"
    elif (agirlikSinifi == "Küçük Sınıf" and motor == "20-75 kw - Elektrikli"):
        enerjiSis = "Batarya"
    elif (agirlikSinifi == "Küçük Sınıf" and motor == "25-100 hp - Dizel"):
        enerjiSis = "Yakıt Tankı"
    elif (agirlikSinifi == "Küçük Sınıf" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        enerjiSis = "Yakıt Tankı"
    elif (agirlikSinifi == "Orta Sınıf" and motor == "75-300 kw - Elektrikli"):
        enerjiSis = "Yakıt Hücresi"
    elif (agirlikSinifi == "Orta Sınıf" and motor == "100-400 hp - Dizel"):
        enerjiSis = "Yakıt Tankı"
    elif (agirlikSinifi == "Orta Sınıf" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        enerjiSis = "Yakıt Tankı"
    elif (agirlikSinifi == "Ağır Sınıf" and motor == "300+ kw - Elektrikli"):
        enerjiSis = "Yakıt Hücresi"
    elif (agirlikSinifi == "Ağır Sınıf" and motor == "400+ hp -  Dizel"):
        enerjiSis = "Yakıt Tankı"
    elif (agirlikSinifi == "Ağır Sınıf" and motor == "400+ hp + 75+ kw Hibrit"):
        enerjiSis = "Yakıt Tankı"

    # 12 - Güç Aktarma Sistemi:

    if (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and motor == "0-20 kw - Elektrikli"):
        gucAktarmaSis = "Sabit Oranlı Transmisyon"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "20-75 kw - Elektrikli"):
        gucAktarmaSis = "Sabit Oranlı Transmisyon"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "20-75 kw - Elektrikli"):
        gucAktarmaSis = "Elektrikli Transmisyon"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "25-100 hp - Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "25-100 hp - Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "75-300 kw - Elektrikli"):
        gucAktarmaSis = "Elektrikli Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "75-300 kw - Elektrikli"):
        gucAktarmaSis = "Elektrikli Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "75-300 kw - Elektrikli"):
        gucAktarmaSis = "Elektrikli Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "100-400 hp - Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "100-400 hp - Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "100-400 hp - Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "300+ kw - Elektrikli"):
        gucAktarmaSis = "Elektrikli Transmisyon"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "300+ kw - Elektrikli"):
        gucAktarmaSis = "Elektrikli Transmisyon"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "400+ hp -  Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "400+ hp -  Dizel"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "400+ hp + 75+ kw Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "400+ hp + 75+ kw Hibrit"):
        gucAktarmaSis = "Değişken Oranlı Transmisyon"

    # 13 - Fren Sistemi:

    if (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and motor == "0-20 kw - Elektrikli"):
        frenSis = "Dinamik Frenleme"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "20-75 kw - Elektrikli"):
        frenSis = "Dinamik Frenleme"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "20-75 kw - Elektrikli"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "25-100 hp - Dizel"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "25-100 hp - Dizel"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        frenSis = "Rejenaratif Frenleme"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "75-300 kw - Elektrikli"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "75-300 kw - Elektrikli"):
        frenSis = "Rejenaratif Frenleme"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "75-300 kw - Elektrikli"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "100-400 hp - Dizel"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "100-400 hp - Dizel"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "100-400 hp - Dizel"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        frenSis = "Rejenaratif Frenleme"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "300+ kw - Elektrikli"):
        frenSis = "Rejenaratif Frenleme"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "300+ kw - Elektrikli"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "400+ hp -  Dizel"):
        frenSis = "ABS (Anti-Blokaj Fren Sistemi)"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "400+ hp -  Dizel"):
        frenSis = "EBS (Elektronik Fren Sistemi)"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "400+ hp + 75+ kw Hibrit"):
        frenSis = "Rejenaratif Frenleme"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "400+ hp + 75+ kw Hibrit"):
        frenSis = "EBS (Elektronik Fren Sistemi)"

    # 14 - Isı Yönetimi

    if (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$" and motor == "0-20 kw - Elektrikli"):
        isiYonetimSis = "Hava Soğutmalı"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "20-75 kw - Elektrikli"):
        isiYonetimSis = "Hava Soğutmalı"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "20-75 kw - Elektrikli"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "25-100 hp - Dizel"):
        isiYonetimSis = "Yağ Soğutmalı"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "25-100 hp - Dizel"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        isiYonetimSis = "Yağ Soğutmalı"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$" and motor == "25-100 hp + 0-20 kw - Hibrit"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "75-300 kw - Elektrikli"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "75-300 kw - Elektrikli"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "75-300 kw - Elektrikli"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "100-400 hp - Dizel"):
        isiYonetimSis = "Yağ Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "100-400 hp - Dizel"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "100-400 hp - Dizel"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        isiYonetimSis = "Yağ Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +" and motor == "100-400 hp + 20-75 kw - Hibrit"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "300+ kw - Elektrikli"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "300+ kw - Elektrikli"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "400+ hp -  Dizel"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "400+ hp -  Dizel"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$" and motor == "400+ hp + 75+ kw Hibrit"):
        isiYonetimSis = "Su Soğutmalı"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +" and motor == "400+ hp + 75+ kw Hibrit"):
        isiYonetimSis = "Su Soğutmalı"

# 15 - Elektrik Sistemi

    if (agirlikSinifi == "Hafif Sınıf" and (faydaliYuk == "Gözetleme Sistemi" or faydaliYuk == "Manipülatör Sistemi")):
        elektrikSis = "Aküsüz Sistem"
    elif (agirlikSinifi == "Küçük Sınıf" and (faydaliYuk == "Gözetleme Sistemi" or faydaliYuk == "Manipülatör Sistemi" or faydaliYuk == "Silah Sistemi" or faydaliYuk == "Taşıyıcı Sistemi")):
        elektrikSis = "12V-Akü"
    elif ((agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and (faydaliYuk == "Gözetleme Sistemi" or faydaliYuk == "Manipülatör Sistemi" or faydaliYuk == "Silah Sistemi" or faydaliYuk == "Mayın ve Engel Temizleme Sistemi")):
        elektrikSis = "28V-Akü"
    elif ((agirlikSinifi == "Orta Sınıf" or agirlikSinifi == "Ağır Sınıf") and faydaliYuk == "Taşıyıcı Sistemi"):
        elektrikSis = "24V-Akü"

# 16 - Gövde Malzemesi:

    if (agirlikSinifi == "Hafif Sınıf" and maliyet == "0-30000$"):
        govdeMalzeme = "Polimer Malzemeler"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "0-30000$"):
        govdeMalzeme = "Alüminyum Alaşımlar"
    elif (agirlikSinifi == "Küçük Sınıf" and maliyet == "30000$-100000$"):
        govdeMalzeme = "Kompozit Malzemeler"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "0-30000$"):
        govdeMalzeme = "Alüminyum Alaşımlar"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "30000$-100000$"):
        govdeMalzeme = "Alüminyum Alaşımlar"
    elif (agirlikSinifi == "Orta Sınıf" and maliyet == "100000$ +"):
        govdeMalzeme = "Çelik Alaşımlar"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "30000$-100000$"):
        govdeMalzeme = "Alüminyum Alaşımlar"
    elif (agirlikSinifi == "Ağır Sınıf" and maliyet == "100000$ +"):
        govdeMalzeme = "Çelik Alaşımlar"

# 17 - Elektronik Üniteler:

    elektronikUnite = "Sensörler | Kameralar | İşlemciler | Güç Dağıtım Üniteleri | Kablolar"

# 18 - Şasi:
# Makina Öğrenmesi sonrası gelecek.

    return {1: maliyet,
            2: agirlikSinifi,
            3: ozerkYapi,
            4: kontrolSis,
            5: faydaliYuk,
            6: motor,
            7: araziTipi,
            8: yonlendirmeSis,
            9: suspansiyonSis,
            10: govdeMalzeme,
            11: enerjiSis,
            12: gucAktarmaSis,
            13: frenSis,
            14: isiYonetimSis,
            15: elektrikSis,
            16: elektronikUnite,
            }


def model_giris_degerleri(sonuclar: dict) -> dict:

    input_arr = {}

    # Maliyet sayısal karşılığı

    if (sonuclar[1] == '0-30000$'):
        input_arr['maliyet'] = 1
    elif (sonuclar[1] == '30000$-100000$'):
        input_arr['maliyet'] = 2
    elif (sonuclar[1] == '100000$ +'):
        input_arr['maliyet'] = 3

    # Ağırlık sınıfı

    if (sonuclar[2] == 'Hafif Sınıf'):
        input_arr['agirlik_sinifi'] = 1
    elif (sonuclar[2] == 'Küçük Sınıf'):
        input_arr['agirlik_sinifi'] = 2
    elif (sonuclar[2] == 'Orta Sınıf'):
        input_arr['agirlik_sinifi'] = 3
    elif (sonuclar[2] == 'Ağır Sınıf'):
        input_arr['agirlik_sinifi'] = 4

    # Özerk Yapı

    if (sonuclar[3] == 'Manuel'):
        input_arr['ozerk_yapi'] = 1
    elif (sonuclar[3] == 'Yarı-Otonom'):
        input_arr['ozerk_yapi'] = 2
    elif (sonuclar[3] == 'Otonom'):
        input_arr['ozerk_yapi'] = 3

    # Kontrol Sistemi

    if (sonuclar[4] == 'RF Kumanda'):
        input_arr['kontrol_sis'] = 1
    elif (sonuclar[4] == 'Uzaktan Kumanda Modulu'):
        input_arr['kontrol_sis'] = 2
    elif (sonuclar[4] == 'Uydu'):
        input_arr['kontrol_sis'] = 3

    # Faydalı yük

    if (sonuclar[5] == 'Gözetleme Sistemi'):
        input_arr['faydali_yuk'] = 1
    elif (sonuclar[5] == 'Manipülatör Sistemi'):
        input_arr['faydali_yuk'] = 2
    elif (sonuclar[5] == 'Taşıyıcı Sistemi'):
        input_arr['faydali_yuk'] = 3
    elif (sonuclar[5] == 'Silah Sistemi'):
        input_arr['faydali_yuk'] = 4
    elif (sonuclar[5] == 'Mayın ve Engel Temizleme Sistemi'):
        input_arr['faydali_yuk'] = 5

    # Motor

    if (sonuclar[6] == '0-20 kw - Elektrikli'):
        input_arr['motor'] = 1
    elif (sonuclar[6] == '20-75 kw - Elektrikli'):
        input_arr['motor'] = 2
    elif (sonuclar[6] == '75-300 kw - Elektrikli'):
        input_arr['motor'] = 3
    elif (sonuclar[6] == '300+ kw - Elektrikli'):
        input_arr['motor'] = 4
    elif (sonuclar[6] == '25-100 hp - Dizel'):
        input_arr['motor'] = 5
    elif (sonuclar[6] == '100-400 hp - Dizel'):
        input_arr['motor'] = 6
    elif (sonuclar[6] == '400+ hp -  Dizel'):
        input_arr['motor'] = 7
    elif (sonuclar[6] == '25-100 hp + 0-20 kw - Hibrit'):
        input_arr['motor'] = 8
    elif (sonuclar[6] == '100-400 hp + 20-75 kw - Hibrit'):
        input_arr['motor'] = 9
    elif (sonuclar[6] == '400+ hp + 75+ kw Hibrit'):
        input_arr['motor'] = 10

    # Arazi Tipi

    if (sonuclar[7] == 'Düz-Sert Zemin'):
        input_arr['arazi_tipi'] = 1
    elif (sonuclar[7] == 'Düz-Yumuşak Zemin'):
        input_arr['arazi_tipi'] = 2
    elif (sonuclar[7] == 'Engebeli-Sert Zemin'):
        input_arr['arazi_tipi'] = 3
    elif (sonuclar[7] == 'Engebeli-Yumuşak Zemin'):
        input_arr['arazi_tipi'] = 4

    # Yönlendirme Sistemi

    if (sonuclar[8] == 'Ackerman Yönlendirme Sistemi'):
        input_arr['yonlendirme_sis'] = 1
    elif (sonuclar[8] == 'Diferansiyel Yönlendirme Sistemi'):
        input_arr['yonlendirme_sis'] = 2
    elif (sonuclar[8] == '4WS Yönlendirme Sistemi'):
        input_arr['yonlendirme_sis'] = 3
    elif (sonuclar[8] == 'Skid-Steer Yönlendirme Sistemi'):
        input_arr['yonlendirme_sis'] = 4
    elif (sonuclar[8] == 'Aktif Dönüşlü Yönlendirme Sistemi'):
        input_arr['yonlendirme_sis'] = 5

    # Süspansiyon Sistemi

    if (sonuclar[9] == 'Kauçuk-Elastomerik'):
        input_arr['suspansiyon_sis'] = 1
    elif (sonuclar[9] == 'Yay ve Amortisör Sistemi'):
        input_arr['suspansiyon_sis'] = 2
    elif (sonuclar[9] == 'MacPherson'):
        input_arr['suspansiyon_sis'] = 3
    elif (sonuclar[9] == 'Çift Salıncaklı'):
        input_arr['suspansiyon_sis'] = 4
    elif (sonuclar[9] == 'Burulabilen Mil'):
        input_arr['suspansiyon_sis'] = 5
    elif (sonuclar[9] == 'Katı Aks'):
        input_arr['suspansiyon_sis'] = 6
    elif (sonuclar[9] == 'Hidropnömatik'):
        input_arr['suspansiyon_sis'] = 7

    # Gövde Malzemesi

    if (sonuclar[10] == 'Polimer Malzemeler'):
        input_arr['govde_malzemesi'] = 1
    elif (sonuclar[10] == 'Kompozit Malzemeler'):
        input_arr['govde_malzemesi'] = 2
    elif (sonuclar[10] == 'Alüminyum Alaşımlar'):
        input_arr['govde_malzemesi'] = 3
    elif (sonuclar[10] == 'Çelik Alaşımlar'):
        input_arr['govde_malzemesi'] = 4

    # Enerji Sistemleri

    if (sonuclar[11] == 'Pil'):
        input_arr['enerji_sis'] = 1
    elif (sonuclar[11] == 'Batarya'):
        input_arr['enerji_sis'] = 2
    elif (sonuclar[11] == 'Yakıt Hücresi'):
        input_arr['enerji_sis'] = 3
    elif (sonuclar[11] == 'Yakıt Tankı'):
        input_arr['enerji_sis'] = 4

    # Güç Aktarma Sistemi

    if (sonuclar[12] == 'Sabit Oranlı Transmisyon'):
        input_arr['guc_aktarma'] = 1
    elif (sonuclar[12] == 'Elektrikli Transmisyon'):
        input_arr['guc_aktarma'] = 2
    elif (sonuclar[12] == 'Değişken Oranlı Transmisyon'):
        input_arr['guc_aktarma'] = 3

    # Fren Sistemi

    if (sonuclar[13] == 'Dinamik Frenleme'):
        input_arr['fren_sistemi'] = 1
    elif (sonuclar[13] == 'EBS (Elektronik Fren Sistemi)'):
        input_arr['fren_sistemi'] = 2
    elif (sonuclar[13] == 'ABS (Anti-Blokaj Fren Sistemi)'):
        input_arr['fren_sistemi'] = 3
    elif (sonuclar[13] == 'Rejenaratif Frenleme'):
        input_arr['fren_sistemi'] = 4

    # Isı Yönetim Sistemi

    if (sonuclar[14] == 'Hava Soğutmalı'):
        input_arr['isi_yonetim'] = 1
    elif (sonuclar[14] == 'Yağ Soğutmalı'):
        input_arr['isi_yonetim'] = 2
    elif (sonuclar[14] == 'Su Soğutmalı'):
        input_arr['isi_yonetim'] = 3

    # Elektrik Sistemi

    if (sonuclar[15] == 'Aküsüz Sistem'):
        input_arr['elektrik_sistemi'] = 1
    elif (sonuclar[15] == '12V-Akü'):
        input_arr['elektrik_sistemi'] = 2
    elif (sonuclar[15] == '24V-Akü'):
        input_arr['elektrik_sistemi'] = 3
    elif (sonuclar[15] == '28V-Akü'):
        input_arr['elektrik_sistemi'] = 4

    # Elektronik Ünite

    input_arr['elektronik_unite'] = 1

    return input_arr


def model_sonuc(inputs) -> str:

    with open('ML/encoder2', 'rb') as f:
        oneHotEncoder = pickle.loads(f)

    model = load_model("ML/ysa_sgd_tanh2.keras")

    inputs = pd.DataFrame(inputs, index=[0])

    inputs = inputs.iloc[0].values

    inputs = inputs[:15].reshape(1, -1)

    encoded = oneHotEncoder.transform(inputs).toarray()

    predictions = model.predict(encoded)

    predictions = predictions > 0.5

    if (predictions[0][0] == True):
        return "2 Tekerlekli"

    elif (predictions[0][1] == True):
        return "4 Tekerlekli"

    elif (predictions[0][2] == True):
        return "6 Tekerlekli"

    elif (predictions[0][3] == True):
        return "8 Tekerlekli"

    elif (predictions[0][4] == True):
        return "Paletli"

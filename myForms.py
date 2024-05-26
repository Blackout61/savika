from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired


class MyForm(FlaskForm):
    radio_btn = RadioField(validators=[InputRequired(), DataRequired()],
                           choices=[('0-30000$', '0-30000$'), ('30000$-100000$', '30000$-100000$'), ('100000$ +', '100000$ +')], default="")

    radio_btn_3 = RadioField(validators=[InputRequired()],
                             choices=[("1. Seviye", "1. Seviye"), ("2. Seviye", "2. Seviye"), ("3. Seviye", "3. Seviye")])

    radio_btn_4 = RadioField(validators=[InputRequired(), DataRequired()],
                             choices=[("x<2 km\u00B2", "x<2 km\u00B2"), ("x<5 km\u00B2", "x<5 km\u00B2"), ("x km\u00B2", "x km\u00B2")])

    option_one = "Uzunluk: 0-1 m | Genişlik: 0-0.5 m | Yükseklik: 0-0.5 m | Dik Engel Aşma: 0-0.5 m | Hendek Aşma: 0-0.5 m | Eğim: 40-60% | Ağırlık: 0-200 kg"
    option_two = "Uzunluk: 1-3 m | Genişlik: 0.5-2 m | Yükseklik: 0.5-1 m | Dik Engel Aşma: 0-0.5 m | Hendek Aşma: 0-0.5 m | Eğim: 40-60% | Ağırlık: 200-1000 kg"
    option_three = "Uzunluk: 2-6 m | Genişlik: 1-3 m | Yükseklik: 1-2 m | Dik Engel Aşma: 0.5-1.5 m | Hendek Aşma: 0.5-1.5 m | Eğim: 40-60% | Ağırlık: 1000-15000 kg"
    option_four = "Uzunluk: 6+ m | Genişlik: 2+ m | Yükseklik: 2+ m | Dik Engel Aşma: 1.5+ m | Hendek Aşma: 1.5+ m | Eğim: 40-60% | Ağırlık: 15000+ kg"
    radio_btn_2 = RadioField(validators=[InputRequired(), DataRequired()],
                             choices=[(option_one, option_one), (option_two, option_two), (option_three, option_three), (option_four, option_four)])

    radio_btn_5 = RadioField(validators=[InputRequired(), DataRequired()],
                             choices=[("Keşif, Gözetleme ve İstihbarat", "Keşif, Gözetleme ve İstihbarat"), ("Bomba İmha", "Bomba İmha"), ("Lojistik", "Lojistik"), ("Saldırı ve Geri Emniyet", "Saldırı ve Geri Emniyet"), ("Mayın ve Engel Temizleme", "Mayın ve Engel Temizleme")])

    option_1 = "0-20 kw - Elektrikli"
    option_2 = "20-75 kw - Elektrikli"
    option_3 = "75-300 kw - Elektrikli"
    option_4 = "300+ kw - Elektrikli"
    option_5 = "25-100 hp - Dizel"
    option_6 = "100-400 hp - Dizel"
    option_7 = "400+ hp -  Dizel"
    option_8 = "25-100 hp + 0-20 kw - Hibrit"
    option_9 = "100-400 hp + 20-75 kw - Hibrit"
    option_10 = "400+ hp + 75+ kw Hibrit"
    radio_btn_6 = RadioField(validators=[InputRequired(), DataRequired()],
                             choices=[(option_1, option_1), (option_2, option_2), (option_3, option_3), (option_4, option_4), (option_5, option_5), (option_6, option_6), (option_7, option_7), (option_8, option_8), (option_9, option_9), (option_10, option_10)])

    radio_btn_7 = RadioField(validators=[InputRequired(), DataRequired()],
                             choices=[("Düz-Sert Zemin", "Düz-Sert Zemin"), ("Düz-Yumuşak Zemin", "Düz-Yumuşak Zemin"), ("Engebeli-Sert Zemin", "Engebeli-Sert Zemin"), ("Engebeli-Yumuşak Zemin", "Engebeli-Yumuşak Zemin")])

    options = ["Geniş Dönüş Yarıçapı",
               "Orta Dönüş Yarıçapı", "Dar Dönüş Yarıçapı"]
    radio_btn_8 = RadioField(validators=[InputRequired(), DataRequired()],
                             choices=[(options[0], options[0]), (options[1], options[1]), (options[2], options[2])])

    submit = SubmitField("Seçimleri Onayla")

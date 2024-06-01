from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf import FlaskForm


class MyRecursive1 (FlaskForm):

    radio_btn = RadioField(
        validators=[InputRequired(), DataRequired()],
        choices=[
            ("Gözetleme Sistemi", "Gözetleme Sistemi"),
            ("Manipülatör Sistemi", "Manipülatör Sistemi"),
            ("Taşıyıcı Sistem", "Taşıyıcı Sistem"),
            ("Silah Sistemi", "Silah Sistemi"),
        ]
    )

    btn_sub_1 = SubmitField("Sonuçları Göster")


class MyRecursive2 (FlaskForm):

    radio_btn = RadioField(
        validators=[InputRequired(), DataRequired()],
        choices=[
            ("Gözetleme Sistemi", "Gözetleme Sistemi"),
            ("Manipülatör Sistemi", "Manipülatör Sistemi"),
            ("Taşıyıcı Sistem", "Taşıyıcı Sistem"),
            ("Silah Sistemi", "Silah Sistemi"),
            ("Mayın ve Engel Temizleme Sistemi",
             "Mayın ve Engel Temizleme Sistemi")
        ]
    )

    btn_sub_2 = SubmitField("Sonuçları Göster")

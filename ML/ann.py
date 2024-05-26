import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense, Dropout  # type: ignore


def data_preprocessing():

    data = pd.read_excel("VeriSeti_4.xlsx")

    X = data.iloc[:, :16]
    y = data.iloc[:, 16:]

    X = pd.get_dummies(X, columns=['Maliyet', 'Ağırlık Sınıfı', 'Özerk Yapı', 'Kontrol Sistemi',
                                   'Faydalı Yük', 'Motor', 'Arazi Tipi', 'Yönlendirme Sistemi',
                                   'Süspansiyon Sistemi', 'Gövde Malzemesi', 'Enerji Sistemi',
                                   'Güç Aktarma Sistemi', 'Fren Sistemi', 'Isı Yönetim Sistemi',
                                   'Elektrik Sistemi', 'Elektronik Üniteler'])

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, shuffle=True)
    x_train, x_valid, y_train, y_valid = train_test_split(
        x_train, y_train, test_size=0.3, random_state=42, shuffle=True)

    return x_train, y_train, x_valid, y_valid, x_test, y_test


def creating_model():
    model = Sequential()

    model.add(Dense(128, activation="relu", input_shape=(None, 67)))
    model.add(Dropout(0.5))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(5, activation="softmax"))

    model.compile(loss="binary_crossentropy",
                  optimizer="adam", metrics=["accuracy"])

    return model


def train_model(model, x_train, y_train, x_valid, y_valid):
    model.fit(x_train,
              y_train,
              verbose=1,
              epochs=50,
              batch_size=32,
              validation_data=(x_valid, y_valid)
              )
    return model


def test_model(model, x_test, y_test):
    predict = model.predict(x_test)
    predict = (predict > 0.5)*1
    acc = accuracy_score(predict, y_test)
    return acc


def plot_model_result(model):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].plot(model.history.history['accuracy'],
                 model.history.history['val_accuracy'])

    axes[0].set_title('Model accuracy')
    axes[0].set_ylabel('accuracy')
    axes[0].set_xlabel('epoch')

    axes[1].plot(model.history.history['loss'],
                 model.history.history['val_loss'])

    axes[1].set_title('Model loss')
    axes[1].set_ylabel('loss')
    axes[1].set_xlabel('epoch')

    axes[0].legend()
    axes[1].legend()

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    model = creating_model()
    x_train, y_train, x_valid, y_valid, x_test, y_test = data_preprocessing()
    model_trained = train_model(model, x_train, y_train, x_valid, y_valid)
    acc = test_model(model_trained, x_test, y_test)
    print('Sonuclar:ACC = ', acc)
    plot_model_result(model)

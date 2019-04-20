import pandas as pd # Dataframe, series
import numpy as np # Scientific computing packages - Array
from pandas import Series, DataFrame
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.model_selection import train_test_split


data = pd.read_csv('symptoms.csv')
data.describe()

data.head()

clf = tree.DecisionTreeClassifier()
train, test = train_test_split(data, test_size = 0.15)


attributes = ["Fever", "Bilsters in the mouth and on feet", "Drop in milk production", "Weight loss", "Loss of appetite", "blisters on teats", "Lameness", "intermittent fever", "anaemia", "oedema", "lacrimation", "Lymph nodes", "Abortion", "Infertility", "emaciation", "Calf dropping the head", "Dull and depressed", "High temperature", "Heavy breathing", "Nasal discharge", "Coughing", "Stillbirth", "Weak calf born", "Retention of fetal membranes", "infection in the membranes", "Swollen testicles in bulls", "Watery Milk", "heat", "Swollen udder", "Pain in udder", "Hardness of the teats", "reduction in milk ", "anorexia", "corneal opacity", "diarrhoea", "milky eye and white gums"]
x_train = train[attributes]
y_train = train["Diseases"]

x_test = test[attributes]
y_test = test["Diseases"]


clf = clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

score = accuracy_score(y_test, y_pred)


def predict():
    data = pd.read_csv('data.csv')

    X = data[attributes]
    #Y = data.Diseases

    iris_data = DataFrame(X, columns=["Fever", "Bilsters in the mouth and on feet", "Drop in milk production", "Weight loss", "Loss of appetite", "blisters on teats", "Lameness", "intermittent fever", "anaemia", "oedema", "lacrimation", "Lymph nodes", "Abortion", "Infertility","emaciation", "Calf dropping the head", "Dull and depressed", "High temperature", "Heavy breathing", "Nasal discharge", "Coughing", "Stillbirth", "Weak calf born", "Retention of fetal membranes", "infection in the membranes", "Swollen testicles in bulls", "Watery Milk", "heat", "Swollen udder", "Pain in udder", "Hardness of the teats", "reduction in milk ", "anorexia", "corneal opacity", "diarrhoea", "milky eye and white gums"])
    #iris_target = DataFrame(Y, columns=["Diseases"])

    predicted = clf.predict(iris_data)

    #expected = iris_target
    # print(metrics.accuracy_score(expected, predicted)*100, "%")
    return predicted


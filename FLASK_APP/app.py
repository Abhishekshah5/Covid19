import requests
from flask import Flask ,render_template, request

app= Flask(__name__)
@app.route("/india")
def india():
    x = requests.get("https://api.covid19india.org/data.json")
    data=x.json()
    state=data["statewise"]
    head=data["statewise"][0]
    return render_template("district.html", datas=state, head=head)
@app.route("/news")
def news():
    y = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=7545ad19923446e88cf8f8de65cb4d88")
    data=y.json()
    head=data["articles"]
    return render_template("news.html", heads=head)

@app.route("/")
def world():
    x = requests.get("https://api.covid19api.com/summary")
    data=x.json()
    state=data["Countries"]
    ste=data["Global"]
    time=state[77]

    return render_template("index.html", datas=state,loves=ste, times=time)





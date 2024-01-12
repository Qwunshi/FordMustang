from flask import Flask, render_template

app = Flask(__name__)
nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "История", "URL": "/page1" },
    { "title": "Галерея", "URL": "/page2" },
    { "title": "Будущее поколение", "URL": "/page3"}
]

@app.context_processor
def global_context():
    return{
        "nav": nav
    }

@app.route("/")
def hello_world():
    return render_template("glav.html", name="Главная")

@app.route("/page1")
def page1_view():
    return render_template("page1.html", name="История")

@app.route("/page2")
def page2_view():
    return render_template("page2.html", name="Галерея")

@app.route("/page3")
def page3_view():
    return render_template("page3.html", name="Будущее поколение")
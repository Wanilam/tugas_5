from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def departemen():
    return render_template("departemen.html")

@app.route("/gajii")
def gaji():
    return render_template("gaji.html")

@app.route("/karyawan")
def karyawan():
    return render_template("karyawan.html")

@app.route("/proyek")
def proyek():
    return render_template("proyek.html")
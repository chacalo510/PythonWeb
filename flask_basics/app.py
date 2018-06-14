# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/") #decorador (investigar)
def index():
    return "Esto es una página Index"

@app.route("/info")
def info():
    return "Info page"

@app.route("/practica1")
def practica1():
    return "Esto es una práctica"

@app.route("/practica2")
def practica2():
    return "Esto es otra práctica"
        
# Guard (investigar)
if __name__ == '__main__':
    app.run(debug=True)

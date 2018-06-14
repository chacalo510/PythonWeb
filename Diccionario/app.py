# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Jinja
    palabra = "Panegírico"
    definición = "Discurso en el que se alaba a alguien. Ejemplo: Madura es extremadamente panegírico en relación a Chávez"
    return render_template('index.html', palabra=palabra, definición=definición)

    # También se puede hacer así:
    #def index():
    #palabra = "Pletórico"
    #definición = "Esto es una definición"

    #@context = {
        #'palabra' : palabra
        #'definición': definiciónote
    #}
    #return render_template('index.html', **context)


@app.route('/word')
def word():
    headers_value = {
        "app_id" : "7611c71d",
        "app_key" : "0da35fb6262f148d00eca1e7b5427cab"
    }

    result = requests.get('https://od-api.oxforddictionaries.com/api/v1/entries/es/idioma', headers=headers_value)
    print(result.json())
    if result.status_code !=200:
        print("hubo un problema: ", result.json)

    data = result.json()

    print
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

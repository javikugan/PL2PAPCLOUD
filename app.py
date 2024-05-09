import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import psycopg2
import json

app = Flask(__name__)

def conectar():
    try:
        server = 'pruebapl2bbdd.postgres.database.azure.com'
        conn = psycopg2.connect(database="pl2papjp",
                        host=server,
                        user="roma",
                        password="mRjCr28a54FAeM#f#b",
                        port="5432")        
        return conn
    except Exception as e:
        print("Error connecting to the database: ", e)
        return None

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/publish", methods=['POST'])
def publish():
    try:
        nombre = request.form['nombre']
        puntuacion = request.form['puntuacion']
        fecha = request.form['fecha']
        tiempo = request.form['tiempo']
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO resultados(nombre, puntuacion, fecha, tiempo) VALUES (?, ?, ?, ?);"
        params = (nombre, puntuacion, fecha, tiempo)
        cursor.execute(query, params)
        cursor.execute(query)
        conn.commit()
        return "RESULTADOS GUARDADOS"
    except Exception as e:
        return str(e)

@app.route("/retrieve")
def retrieve():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resultados")
        cadena = cursor.fetchall()
        return json.dumps(cadena)
    except Exception as e:
        return e



if __name__ == '__main__':
   app.run()

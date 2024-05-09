import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import pyodbc
import json

app = Flask(__name__)

def conectar():
    try:
        server = 'bbddserverpl2.database.windows.net'
        database = 'PL2_PAP_BBDD'
        username = 'pl2'
        password = 'mRjCr28a54FAeM#f#b'
        driver= '{ODBC Driver 17 for SQL Server}'
        connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        return e

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
        query = f"INSERT INTO resultados(nombre, puntuacion, fecha, tiempo) VALUES ('{nombre}', {puntuacion}, '{fecha}', {tiempo});"
        cursor.execute(query)
        conn.commit()
        return "RESULTADOS GUARDADOS"
    except Exception as e:
        return str(e)
@app.route("/retrieve")
def retrieve():
    try:
        # Mock data for testing
        mock_data = [
            {"nombre": "John Doe", "puntuacion": 5000, "fecha": "2021-07-21", "tiempo": 360},
            {"nombre": "Jane Smith", "puntuacion": 6000, "fecha": "2021-07-22", "tiempo": 300}
        ]
        return json.dumps(mock_data)
    except Exception as e:
        return str(e), 500



if __name__ == '__main__':
   app.run()

"""@app.route("/retrieve")
def retrieve():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resultados")
        cadena = cursor.fetchall()
        return json.dumps(cadena)
    except Exception as e:
        return e"""
import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import pyodbc
import psycopg2
import json

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
def retrieve():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM resultados")
        cadena = cursor.fetchall()
        print(cadena)
        return json.dumps(cadena)
    except Exception as e:
        return e

    
conectar()
print(retrieve())

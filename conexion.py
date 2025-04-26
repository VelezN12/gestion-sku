import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Conexion():
    def __init__(self):
        try:
            self.con = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_DATABASE"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT"),
                sslmode=os.getenv("DB_SSLMODE")
            )
            
            self.crearTablas()
        except Exception as ex:
            print("Error al conectar con la base de datos:", ex)

    def crearTablas(self):
        sql_create_table1 = """ 
        CREATE TABLE IF NOT EXISTS skus (
            id_sku TEXT PRIMARY KEY,
            nombre_etiqueta TEXT NOT NULL,
            guia1 TEXT,
            guia2 TEXT,
            guia3 TEXT,
            placa TEXT,
            pisador TEXT
        );"""
        
        try:
            cur = self.con.cursor()
            cur.execute(sql_create_table1)
            self.con.commit()
            cur.close()
        except Exception as ex:
            print("Error al crear tablas:", ex)

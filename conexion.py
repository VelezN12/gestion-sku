import psycopg2
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class Conexion():
    def __init__(self):
        try:
            self.con = psycopg2.connect(
                host=st.secrets["database"]["DB_HOST"],
                database=st.secrets["database"]["DB_NAME"],
                user=st.secrets["database"]["DB_USER"],
                password=st.secrets["database"]["DB_PASSWORD"],
                port=st.secrets["database"]["DB_PORT"],
                sslmode="require"  # importante para conexión segura
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

import pandas as pd
from conexion import Conexion

# Ruta al archivo Excel
ruta_excel = "datosdeprueba.xlsx"

try:
    # Leer la hoja "BaseDatos"
    df = pd.read_excel(ruta_excel, 
                       sheet_name='BaseDatos', 
                       dtype={
                           'SKU': str,
                           'NOMBRE ': str,
                           'GUIA 1 ': str,
                           'GUIA 2 ': str,
                           'GUIA 3': str,
                           'PLACA ': str,
                           'PISADOR ': str
                       })

    # Renombrar columnas
    df = df.rename(columns={
        'SKU': 'id_sku',
        'NOMBRE ': 'nombre_etiqueta',
        'GUIA 1 ': 'guia1',
        'GUIA 2 ': 'guia2',
        'GUIA 3': 'guia3',
        'PLACA ': 'placa',
        'PISADOR ': 'pisador'
    })

    print("Columnas encontradas en el Excel:", df.columns.tolist())

    # Validar columnas requeridas
    columnas_requeridas = ['id_sku', 'nombre_etiqueta', 'guia1', 'guia2', 'guia3', 'placa', 'pisador']
    if not all(col in df.columns for col in columnas_requeridas):
        raise ValueError("❌ El archivo no contiene todas las columnas requeridas.")

    # Conexión a la base de datos Neon
    conexion = Conexion()
    con = conexion.con
    cur = con.cursor()

    # Reemplazar NaN con vacío
    df = df[columnas_requeridas].fillna('')

    # Insertar los datos
    for _, fila in df.iterrows():
        try:
            cur.execute("""
                INSERT INTO skus (id_sku, nombre_etiqueta, guia1, guia2, guia3, placa, pisador)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id_sku) DO NOTHING;
            """, tuple(fila))
        except Exception as ex:
            print(f"❌ Error al insertar fila {fila['id_sku']}: {ex}")

    con.commit()
    cur.close()
    print("✅ ¡Datos importados exitosamente a Neon!")

except Exception as e:
    print("❌ Error general:", e)

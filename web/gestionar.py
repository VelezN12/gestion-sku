import streamlit as st
import pandas as pd
from conexion import Conexion
from streamlit_extras.stylable_container import stylable_container

def mostrar_gestionar():
    st.title("Gestión de SKUs")

    # Conexión a la base de datos y consulta
    con = Conexion().con
    cursor = con.cursor()
    cursor.execute("SELECT * FROM skus WHERE id_sku IS NOT NULL AND TRIM(id_sku) != '' ORDER BY id_sku ASC;")
    rows = cursor.fetchall()
    cursor.close()

    # Crear DataFrame
    df_skus = pd.DataFrame(rows, columns=['ID SKU', 'Nombre Etiqueta', 'Guía 1', 'Guía 2', 'Guía 3', 'Placa', 'Pisador'])

    col1, col2 = st.columns([4, 1])  # El buscador ocupa 4 partes, el botón 1 parte
    # Filtro de búsqueda
    with col1:
        busqueda = st.text_input("🔎 Buscar por SKU o Nombre", "")
        if busqueda:
            busqueda = busqueda.lower()
            df_skus = df_skus[
                df_skus['ID SKU'].astype(str).str.lower().str.contains(busqueda) |
                df_skus['Nombre Etiqueta'].astype(str).str.lower().str.contains(busqueda)
            ]
    
    with col2:
        with stylable_container(
                key="btn_volver_inicio",
                css_styles=[ # Estilos del botón de volver
                    """
                    button[data-testid="stBaseButton-secondary"] {
                        background: linear-gradient(to bottom right, #ff6f61, #ff8e87);
                        border: 2px solid #58564f;
                        color: white;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 10px 20px;
                        border-radius: 15px;
                        transition: background-color 0.2s ease-in-out;
                        left: 327px !important;
                        top: 29px !important;
                        width: 150px !important;
                        max-width: 300px;
                    """,
                    """
                    button[data-testid="stBaseButton-secondary"]:hover {
                        background: linear-gradient(to bottom right, #d75955, #e47e76) !important;
                        color: white;
                    }
                    """,
                    """
                    button[data-testid="stBaseButton-secondary"]:active {
                        background: #fae37c;
                        color: white;
                    }
                    """,
                    """
                    button[data-testid="stBaseButton-secondary"]:focus {
                        background: #fae37c;
                        color: white !important;
                    }
                    """,
                ]
            ):
                if st.button("Volver a Inicio"):
                    st.session_state.update(page="Inicio")  # O la página que tú quieras volver
                    st.rerun()
    

    # Definir los encabezados de las columnas
    headers = ['SKU', 'Etiqueta', 'Guía 1', 'Guía 2', 'Guía 3', 'Placa', 'Pisador', 'Acción']

    st.markdown("""
            <style>
            /* Fondo general más elegante */
            .stApp {
                background: linear-gradient(135deg, #5a5024 0%, #efdfa6 100%);
                color: #ffffff;
            }

            /* Encabezado de la tabla */
            .table-header {
                font-weight: bold;
                background-color: #333333aa;
                padding: 8px;
                border-radius: 5px;
                text-align: center;
                color: white;
                top: -10px !important;
            }

            /* Celdas de la tabla */
            .table-cell {
                background-color: #ffffff20;
                padding: 8px;
                border-radius: 5px;
                text-align: center;
                color: white;
                max-width: 100%;  /* Asegura que la celda no se expanda más de lo necesario */
            }

            /* Botones de edición */
            div.stButton > button {
                width: 100%;  /* Ajusta el tamaño del botón al 100% de la celda */
                background-color: #ffffff88;
                color: #333;
                border: none;
                padding: 6px 0;  /* Ajusta el padding para que sea uniforme */
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
                text-align: center; /* Centra el texto del botón */
                top: -15px;
            }

            div.stButton > button:hover {
                background-color: #ffffffcc;
                color: black;
            }
            
            .id-sku-col {
                width: 100px !important;
                max-width: 300px;
                overflow-wrap: break-word;
                white-space: normal;
                margin-right: 40px;
                position: relative;
                left: -325px; /* Mueve el elemento 10px a la izquierda */
            }
            
            .wide-col {
                width: 400px !important;
                max-width: 400px;
                overflow-wrap: break-word;
                white-space: normal;
                margin-right: 40px;
                position: relative;
                left: -280px; /* Mueve el elemento 10px a la izquierda */
            }
            
            .id-guia-col {
                width: 150px !important;
                max-width: 300px;
                overflow-wrap: break-word;
                white-space: normal;
                margin-right: 40px;
                position: relative;
            }
            
            .id-btn-col {
                width: 80px !important;
                max-width: 300px;
                overflow-wrap: break-word;
                white-space: normal;
                margin-right: 40px;
                position: relative;
            }
            
            .id-guia-col1 {
                left: -110px; /* Mueve el elemento 10px a la izquierda */
            }
            .id-guia-col2 {
                left: -15px; /* Mueve el elemento 10px a la izquierda */
            }
            .id-guia-col3 {
                left: +80px; /* Mueve el elemento 10px a la izquierda */
            }
            .id-guia-col4 {
                left: +175px; /* Mueve el elemento 10px a la izquierda */
            }
            .id-guia-col5 {
                left: +270px; /* Mueve el elemento 10px a la izquierda */
            }
            .id-guia-col6 {
                left: +365px; /* Mueve el elemento 10px a la izquierda */
            }
            button[kind="secondary"] {
                width: 80px !important;
                max-width: 300px;
                overflow-wrap: break-word;
                white-space: normal;
                margin-right: 40px;
                position: relative;
                left: +365px; /* Mueve el elemento 10px a la izquierda */
            }
            
            
            
            </style>
        """, unsafe_allow_html=True)

    
    # Mostrar el encabezado de la tabla
    cols = st.columns([1, 4, 1, 1, 1, 1, 1, 2])


    for i, header in enumerate(headers):
        if i == 0:
            cols[i].markdown(f"<div class='table-header id-sku-col'>{header}</div>", unsafe_allow_html=True)
        elif i == 1:
            cols[i].markdown(f"<div class='table-header wide-col'>{header}</div>", unsafe_allow_html=True)
        elif i == 2:
            cols[i].markdown(f"<div class='table-header id-guia-col id-guia-col1'>{header}</div>", unsafe_allow_html=True)
        elif i == 3:
            cols[i].markdown(f"<div class='table-header id-guia-col id-guia-col2'>{header}</div>", unsafe_allow_html=True)
        elif i == 4:
            cols[i].markdown(f"<div class='table-header id-guia-col id-guia-col3'>{header}</div>", unsafe_allow_html=True)
        elif i == 5:
            cols[i].markdown(f"<div class='table-header id-guia-col id-guia-col4'>{header}</div>", unsafe_allow_html=True)
        elif i == 6:
            cols[i].markdown(f"<div class='table-header id-guia-col id-guia-col5'>{header}</div>", unsafe_allow_html=True)
        elif i == 7:
            cols[i].markdown(f"<div class='table-header id-btn-col id-guia-col6'>{header}</div>", unsafe_allow_html=True)
        else:
            cols[i].markdown(f"<div class='table-header'>{header}</div>", unsafe_allow_html=True)

    # Mostrar las filas de datos con los botones de acción
    for i, row in df_skus.iterrows():
        cols = st.columns([1, 4, 1, 1, 1, 1, 1, 2])  # Puedes ajustar pesos aquí si lo necesitas

        for j, value in enumerate(row):
            valor_mostrar = value if pd.notna(value) and str(value).strip() != '' else '--'
            
            if j == 0:
                cols[j].markdown(f"<div class='table-cell id-sku-col'>{valor_mostrar}</div>", unsafe_allow_html=True)
            elif j == 1:
                cols[j].markdown(f"<div class='table-cell wide-col'>{valor_mostrar}</div>", unsafe_allow_html=True)
            elif j == 2:
                cols[j].markdown(f"<div class='table-cell id-guia-col id-guia-col1'>{valor_mostrar}</div>", unsafe_allow_html=True)
            elif j == 3:
                cols[j].markdown(f"<div class='table-cell id-guia-col id-guia-col2'>{valor_mostrar}</div>", unsafe_allow_html=True)
            elif j == 4:
                cols[j].markdown(f"<div class='table-cell id-guia-col id-guia-col3'>{valor_mostrar}</div>", unsafe_allow_html=True)
            elif j == 5:
                cols[j].markdown(f"<div class='table-cell id-guia-col id-guia-col4'>{valor_mostrar}</div>", unsafe_allow_html=True)
            elif j == 6:
                cols[j].markdown(f"<div class='table-cell id-guia-col id-guia-col5'>{valor_mostrar}</div>", unsafe_allow_html=True)
            else:
                cols[j].markdown(f"<div class='table-cell'>{valor_mostrar}</div>", unsafe_allow_html=True)

        with cols[7]:
            cols[7].markdown("""
                <style>
                .editar-btn {
                    position: relative;
                    left: +365px; /* Mover 10px a la izquierda */
                    background-color: blue;
                    border: none;
                    border-radius: 5px;
                    padding: 6px 12px;
                    cursor: pointer;
                }
                </style>
            """, unsafe_allow_html=True)
            if st.button(f"✏️ Editar", key=f"editar_{row['ID SKU']}"):
                st.session_state.update(page="Editar")
                st.session_state.sku_para_editar = row['ID SKU']
                st.rerun()


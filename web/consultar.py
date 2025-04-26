import streamlit as st
from conexion import Conexion
from streamlit_extras.stylable_container import stylable_container

def mostrar_consultar():
    if "mostrar_error" not in st.session_state:
        st.session_state.mostrar_error = False
    if "sku_no_encontrado" not in st.session_state:
        st.session_state.sku_no_encontrado = ""
    if "mostrar_detalles_sku" not in st.session_state:
        st.session_state.mostrar_detalles_sku = True  # Estado para mostrar/ocultar detalles del SKU

    st.title("Consultar SKU")

    # Crear el formulario
    with st.form("form_consultar_sku"):
        id_sku_input = st.text_input("Ingrese el SKU")
        
        col1, col2, col3 = st.columns([8, 16, 16])
        with col1:
            with stylable_container(
                key="btn_consultar_sku",
                css_styles=[ # Estilos del botón de consultar
                    """
                    button {
                        background: linear-gradient(to bottom right, #53aee8, #9fd4f6);
                        border: 2px solid #58564f;
                        color: white;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 10px 20px;
                        border-radius: 15px;
                        transition: background-color 0.2s ease-in-out;
                    }
                    """,
                    """
                    button:hover {
                        background: linear-gradient(to bottom right, #74a2c0, #2c87c3);
                    }
                    """,
                    """
                    button:active {
                        background: #fae37c;
                        color: white;
                    }
                    """,
                ]
            ) :
                consultar = st.form_submit_button("Consultar")
            
        with col2:
            # Botón de Volver
            with stylable_container(
                key="btn_volver_inicio",
                css_styles=[ # Estilos del botón de volver
                    """
                    button {
                        background: linear-gradient(to bottom right, #ff6f61, #ff8e87);
                        border: 2px solid #58564f;
                        color: white;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 10px 20px;
                        border-radius: 15px;
                        transition: background-color 0.2s ease-in-out;
                    }
                    """,
                    """
                    button:hover {
                        background: linear-gradient(to bottom right, #d75955, #e47e76);
                    }
                    """,
                    """
                    button:active {
                        background: #fae37c;
                        color: white;
                    }
                    """,
                ]
            ):
                if st.form_submit_button("Volver"):
                    st.session_state.update(page="Inicio")
                    st.rerun() # Vuelve al inicio de la app o recarga la página
        with col3:
            st.empty()


    # Si el botón de consulta es presionado
    if consultar:
        if not id_sku_input.strip():  # Validación: si no se ingresó SKU
            st.markdown(""" 
                <div style="background-color:#fdecea; padding: 20px; border-radius: 8px; border: 1px solid #f5c6cb; color: #721c24; font-weight: bold;">
                    ⚠️ <strong>Por favor ingresa un SKU válido.</strong>
                </div>
            """, unsafe_allow_html=True)
        else:
            conexion = Conexion()
            cur = conexion.con.cursor()
            cur.execute("SELECT id_sku, nombre_etiqueta, guia1, guia2, guia3, placa, pisador FROM skus WHERE id_sku = %s", (id_sku_input,))
            resultado = cur.fetchone()

            if resultado:
                st.markdown("## Detalles del SKU")
                # Mostrar formulario con detalles solo si se ha solicitado
                
                if st.session_state.mostrar_detalles_sku:
                    with st.form(key="detalles_sku_form"):
                        campos = ["ID SKU", "Nombre Etiqueta", "Guía 1", "Guía 2", "Guía 3", "Placa", "Pisador"]
                        valores = resultado
                        for nombre, valor in zip(campos, valores):
                            st.text_input(nombre, valor or "", disabled=True)
                    
                        col1, col2, col3 = st.columns([9, 8, 5])
                        with col1:
                            st.empty()
                        with col2:
                            with stylable_container(
                                key="Ocultar",
                                css_styles=[ # Estilos del botón de ocultar
                                    """
                                    button {
                                        background: linear-gradient(to bottom right, #53aee8, #9fd4f6);
                                        border: 2px solid #58564f;
                                        color: white;
                                        font-weight: bold;
                                        font-size: 16px;
                                        padding: 10px 20px;
                                        border-radius: 15px;
                                        transition: background-color 0.2s ease-in-out;
                                    }
                                    """,
                                    """
                                    button:hover {
                                        background: linear-gradient(to bottom right, #74a2c0, #2c87c3);
                                    }
                                    """,
                                    """
                                    button:active {
                                        background: #fae37c;
                                        color: white;
                                    }
                                    """,
                                ]):
                                if st.form_submit_button("Ocultar"):  # Cambiar la visibilidad al presionar el botón
                                    st.session_state.mostrar_detalles_sku = True  # Ocultar detalles
                                    st.rerun()  # Recargar la app para aplicar los cambios

                    with col3:
                        st.empty()
            else:
                st.session_state.mostrar_error = True
                st.session_state.sku_no_encontrado = id_sku_input
                st.rerun()

    # 🔴 Modal si no se encuentra el SKU
    if st.session_state.mostrar_error:
        sku = st.session_state.sku_no_encontrado

        st.markdown(
            f"""
            <div style="
                position: fixed;
                top: 40%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: #ffe6e6;
                padding: 30px 50px;
                border: 2px solid #cc0000;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                z-index: 9999;
                text-align: center;
            ">
                <h3 style="color: #cc0000;">❌ SKU no encontrado</h3>
                <p style="color: #000000;">No se encontró ningún registro con el ID: <strong>{sku}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col0, col1, col2, col3 = st.columns([8,6,6, 8])
        with col0:
            st.empty()
        with col1:
            with stylable_container(
                key="btn_aceptar_no_encontrado",
                css_styles=[  # Estilos del botón de aceptar
                    """
                    button {
                        background: linear-gradient(to bottom right, #e85553, #f29594);
                        border: 2px solid #58564f;
                        color: white;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 10px 20px;
                        border-radius: 15px;
                        transition: background-color 0.2s ease-in-out;
                        margin-top: 20px;
                    }
                    """,
                    """
                    button:hover {
                        background: linear-gradient(to bottom right, #bf2e2d, #ca6e6d);
                        border: 2px solid black !important;
                        color: white!important;
                    }
                    """,
                    """
                    button:active {
                        background: #fae37c;
                        border: 2px solid black !important;
                        color: white!important;
                    }
                    """,
                    """
                    button:focus {
                        background: #fae37c;
                        border: 2px solid black !important;
                        color: white!important;
                    }
                    """,
                ]
            ):
                if st.button("Aceptar", key="btn_aceptar_modal_consultar"):
                    st.session_state.mostrar_error = False
                    st.session_state.sku_no_encontrado = ""
                    st.rerun()
        with col2:
            # Nuevo botón para registrar el SKU
            with stylable_container(
                key="btn_registrar_sku",
                css_styles=[  # Estilos del botón de registrar SKU
                    """
                    button {
                        background: linear-gradient(to bottom right, #4CAF50, #8BC34A);
                        border: 2px solid #58564f;
                        color: white;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 10px 20px;
                        border-radius: 15px;
                        transition: background-color 0.2s ease-in-out;
                        margin-top: 20px;
                    }
                    """,
                    """
                    button:hover {
                        background: linear-gradient(to bottom right, #3b976a, #82d9ae);
                        border: 2px solid black !important;
                        color: white!important;
                    }
                    """,
                    """
                    button:active {
                        background: #fae37c;
                        border: 2px solid black !important;
                        color: white!important;
                    }
                    """,
                    """
                    button:focus {
                        background: #fae37c;
                        border: 2px solid black !important;
                        color: white!important;
                    }
                    """,
                ]
            ):
                if st.button("Registrar SKU", key="btn_registrar_modal_consultar"):
                    # Redirigir a la página de agregar SKU
                    st.session_state.sku_no_encontrado = sku
                    st.session_state.update(page="Agregar")
                    st.session_state.mostrar_error = False
                    st.session_state.sku_no_encontrado = "" # Asegúrate de que el valor 'Agregar' esté configurado correctamente
                    st.rerun()  # Recargar para aplicar los cambios

        with col3:
            st.empty()

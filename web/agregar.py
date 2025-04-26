import streamlit as st
from conexion import Conexion
from streamlit_extras.stylable_container import stylable_container

def mostrar_agregar():
        
    if "mostrar_modal" not in st.session_state:
        st.session_state.mostrar_modal = False

    if "form_guardado" not in st.session_state:
        st.session_state.form_guardado = False
        
    if "mostrar_error" not in st.session_state:
        st.session_state.mostrar_error = False

    # Mostrar el modal si fue agregado correctamente
    if st.session_state.mostrar_modal:
        
        st.markdown(
            """
            <div class="espacioblanco">
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div style="
                position: fixed;
                top: 40%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: #e6ffe6;
                padding: 30px 50px;
                border: 2px solid #00cc66;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                z-index: 9999;
                text-align: center;
            ">
                <h3 style="color: #007f33;">✅ SKU agregado correctamente</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        

        # Solo mostrar el botón Aceptar
        col1, col2, col3 = st.columns([4,3,2.5])
        
        with col1:
                st.empty()
        with col2:
            with stylable_container(
                key="btn_aceptar_modal",
                css_styles=["""
                    button {
                        background: linear-gradient(to bottom right, #61bf92, #a1efc9);
                        border: 2px solid #39a06e;
                        color: black;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 10px 20px;
                        border-radius: 15px;
                        transition: background-color 0.2s ease-in-out;
                    }
                    """,
                    """
                    button:hover {
                        background: linear-gradient(to bottom right, #4dda96, #a1efc9);
                        color: white;
                        font-weight: bold;
                        border: 2px solid #39a06e;
                    }
                    """
                    ,
                    """
                    button:active {
                        background: #50f8a7;
                        color: white;
                        font-weight: bold;
                        border: 2px solid #39a06e;
                    }
                    """,
                    ]
                ):
                if st.button("Aceptar", key="btn_aceptar_modal"):
                    st.session_state.mostrar_modal = False
                    st.session_state.form_guardado = False
                    st.rerun()
            with col3:
                st.empty()

        return # 🔥 Detener aquí para que no muestre el formulario
    
    if st.session_state.mostrar_error:
        
        mensaje_error = st.session_state.get("error_mensaje", "Ha ocurrido un error desconocido.")

        st.markdown(
            """
            <div class="espacioblanco">
            </div>
            """,
            unsafe_allow_html=True
        )

        html_modal_error = f"""
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
                <h3 style="color: #cc0000;">❌ Error</h3>
                <p style="color: #000000;">{mensaje_error}</p>
            </div>
        """

        st.markdown(html_modal_error, unsafe_allow_html=True)

        # Solo mostrar el botón Aceptar
        col1, col2, col3 = st.columns([4,3,2.5])
        
        with col1:
                st.empty()
        with col2:
            with stylable_container(
                key="btn_volver_modal",
                css_styles=["""
                    button {
                        background: linear-gradient(to bottom right, #e85553, #f29594);
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
                        background: linear-gradient(to bottom right, #bf2e2d, #ca6e6d);
                        color: white;
                        font-weight: bold;
                        border: 2px solid #58564f;
                    }
                    """
                    ,
                    """
                    button:active {
                        background: #fae37c;
                        color: white;
                        font-weight: bold;
                        border: 2px solid #58564f;
                    }
                    """,
                    ]
                ):
                if st.button("Volver", key="btn_volver_modal"):
                    st.session_state.mostrar_error = False
                    st.session_state.form_guardado = False
                    st.rerun()
            with col3:
                st.empty()

        return

    st.title("Agregar SKU")

    with st.form("form_agregar_sku"):
        id_sku = st.text_input("SKU")
        nombre_etiqueta = st.text_input("Nombre Etiqueta")
        guia1 = st.text_input("Guía 1")
        guia2 = st.text_input("Guía 2")
        guia3 = st.text_input("Guía 3")
        placa = st.text_input("Placa")
        pisador = st.text_input("Pisador")
        
         # Crear las columnas para los botones
        col1, col2, col3 = st.columns([2, 4, 4])  # Tres columnas para centrar los botones
        
        with col1:
            st.empty()  # Espacio vacío en la columna izquierda
        with col2:
            with stylable_container(
                key="Guardar",
                css_styles=["""
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
                        color: white;
                        font-weight: bold;
                        border: 2px solid #58564f;
                    }
                    """
                    ,
                    """
                    button:active {
                        background: #fae37c;
                        color: white;
                        font-weight: bold;
                        border: 2px solid #58564f;
                    }
                    """,
                    ]
                ):
                guardar = st.form_submit_button("Guardar")
        with col3:
            with stylable_container(
            key="Volver",
                css_styles=["""
                    button {
                        background: linear-gradient(to bottom right, #e85553, #f29594);
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
                        background: linear-gradient(to bottom right, #bf2e2d, #ca6e6d);
                        color: white;
                        font-weight: bold;
                        border: 2px solid #58564f;
                    }
                    """
                    ,
                    """
                    button:active {
                        background: #fae37c;
                        color: white;
                        font-weight: bold;
                        border: 2px solid #58564f;
                    }
                    """,
                    ]
                ):
                volver = st.form_submit_button("Volver")
        

        if guardar:
            con = Conexion().con
            cursor = con.cursor()
            try:
                cursor.execute("""
                    INSERT INTO skus (id_sku, nombre_etiqueta, guia1, guia2, guia3, placa, pisador)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (id_sku, nombre_etiqueta, guia1, guia2, guia3, placa, pisador))
                con.commit()
                st.session_state.mostrar_modal = True
                st.session_state.form_guardado = True
                st.rerun()  # 🔄 Rerenderiza la app para mostrar el modal
            except Exception as e:
                error_msg = str(e)
                if "duplicate key value violates unique constraint" in error_msg:
                    st.session_state.error_mensaje = "Ya existe un SKU con ese código."
                else:
                    st.session_state.error_mensaje = "Error al guardar el SKU." 
                            
                st.session_state.mostrar_error = True
                
                st.session_state.form_guardado = True
                st.rerun()
                #st.error(f"❌ Error al agregar: {e}")
        
        if volver:
            st.session_state.update(page="Inicio")
            st.session_state.form_guardado = False
            # Aquí evitamos que se recargue innecesariamente y vamos directamente a la página de inicio
            st.rerun()
    
    
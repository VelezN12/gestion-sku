import streamlit as st
from conexion import Conexion
from streamlit_extras.stylable_container import stylable_container
import time

def mostrar_editar():
    
    if "mostrar_modal" not in st.session_state:
        st.session_state.mostrar_modal = False
    
    id_sku_editar = st.session_state.get("sku_para_editar")

    if not id_sku_editar:
        st.error("❌ No hay SKU seleccionado para editar.")
        return
    
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
                <h3 style="color: #007f33;">✅ SKU actualizado correctamente.</h3>
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
                    st.session_state.update(page="Gestionar")
                    st.rerun()
            with col3:
                st.empty()

        return # 🔥 Detener aquí para que no muestre el formulario

    # Obtener los datos del SKU
    con = Conexion().con
    cursor = con.cursor()
    cursor.execute("SELECT * FROM skus WHERE id_sku = %s", (id_sku_editar,))
    sku = cursor.fetchone()

    if not sku:
        st.error("❌ El SKU no fue encontrado.")
        return

    st.title("Editar SKU")

    # Obtener los campos
    id_sku, nombre_etiqueta, guia1, guia2, guia3, placa, pisador = sku

    with st.form("form_editar_sku"):
        nuevo_nombre_etiqueta = st.text_input("Nombre Etiqueta", value=nombre_etiqueta)
        nueva_guia1 = st.text_input("Guía 1", value=guia1)
        nueva_guia2 = st.text_input("Guía 2", value=guia2)
        nueva_guia3 = st.text_input("Guía 3", value=guia3)
        nueva_placa = st.text_input("Placa", value=placa)
        nuevo_pisador = st.text_input("Pisador", value=pisador)

        col1, col2, col3 = st.columns([2, 4, 4])
        with col1:
            st.empty()
        with col2:
            with stylable_container(
                key="btn_guardar_editar",
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
                            ]):  # Puedes reutilizar los estilos anteriores
                guardar = st.form_submit_button("Guardar")
        with col3:
            with stylable_container(
                key="btn_volver_editar",
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
                    ]):  # Puedes reutilizar los estilos anteriores
                volver = st.form_submit_button("Volver")

        if guardar:
            with st.spinner("Actualizando SKU..."):
                time.sleep(1.5)  # Simula el proceso
                try:
                    cursor.execute("""
                        UPDATE skus 
                        SET nombre_etiqueta=%s, guia1=%s, guia2=%s, guia3=%s, placa=%s, pisador=%s
                        WHERE id_sku=%s
                    """, (nuevo_nombre_etiqueta, nueva_guia1, nueva_guia2, nueva_guia3, nueva_placa, nuevo_pisador, id_sku))
                    con.commit()
                    st.success("✅ SKU actualizado correctamente.")
                    time.sleep(1)  # Para que se vea el mensaje un segundo
                    st.session_state.update(page="Gestionar")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error al actualizar: {e}")

        if volver:
            st.session_state.update(page="Gestionar")
            st.rerun()

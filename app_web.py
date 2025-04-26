import streamlit as st
from web.agregar import mostrar_agregar
from web.consultar import mostrar_consultar
from web.gestionar import mostrar_gestionar
from web.editar import mostrar_editar
from streamlit_extras.stylable_container import stylable_container

# Inicializar el estado de la página
if 'page' not in st.session_state:
    st.session_state.page = "Inicio"

# Cargar estilos
with open("estilos.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Funciones para cambiar de página (sin doble clic)
def ir_a(pagina):
    st.session_state.page = pagina

# Caja principal
with st.container():
    if st.session_state.page == "Inicio":
        st.markdown("""
                <div class="titulo1">
                    PRE ALISTAMIENTO CAFO<br>TROQUELADO
                </div>
                """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            with stylable_container(
                key="logo1_image",
                css_styles=["""
                img {
                display: flex;
                justify-content: center; /* Centrado horizontal */
                align-items: center;     /* Centrado vertical */
                height: 100vh;           /* Alto total de la ventana */
                }
                """,
                """
                img {
                width: 100px;
                height: 100px;
                }""",]):
                st.image("utils/logo1.png")
        with col2:
            with stylable_container(
                key="logo2_image",
                css_styles="""
                img { 
                    
                    padding: 20px;
                    
                    }"""):
                st.image("utils/logo2.png")
        with col3:
            with stylable_container(
                key="logoabinbev_image",
                css_styles=["""
                img {
                
                justify-content: center; /* Centrado horizontal */
                align-items: flex-end;     /* Centrado vertical */
                height: 100vh;
                 /* Alto total de la ventana */
                }
                """,
                """
                img {
                margin-top: 70px;
                width: 100px;
                height: 20px;
                }""",]):
                st.image("utils/logoabinbev.png")
        
        st.markdown("""
                <div class="cajon1">
                    <div class="titulo2">¿Qué desea hacer?</div>     
                </div
    """, unsafe_allow_html=True)
        
        col0, col1, col2, col3, col4 = st.columns([1.5, 2, 2, 2, 1])
        with col1:
            with stylable_container(
                key="btn_agregar",
                css_styles=["""
                    button {
                        background: linear-gradient(to bottom right, #dad3b4, #faf3d3);
                        border: 2px solid #58564f;
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
                        background: linear-gradient(to bottom right, #9c9780, #c1bba0);
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
                st.button("Agregar", on_click=ir_a, args=("Agregar",), key="btn_agregar")
        with col2:
            with stylable_container(
                key="btn_consultar",
                css_styles=["""
                    button {
                        background: linear-gradient(to bottom right, #dad3b4, #faf3d3);
                        border: 2px solid #58564f;
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
                        background: linear-gradient(to bottom right, #9c9780, #c1bba0);
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
                st.button("Consultar", on_click=ir_a, args=("Consultar",), key="btn_consultar")
        with col3:
            with stylable_container(
                key="btn_gestionar",
                css_styles=["""
                    button {
                        background: linear-gradient(to bottom right, #dad3b4, #faf3d3);
                        border: 2px solid #58564f;
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
                        background: linear-gradient(to bottom right, #9c9780, #c1bba0);
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
                st.button("Gestionar", on_click=ir_a, args=("Gestionar",), key="btn_gestionar")    
        
    else:
  
        if st.session_state.page == "Agregar":
            mostrar_agregar()
        elif st.session_state.page == "Consultar":
            mostrar_consultar()
        elif st.session_state.page == "Gestionar":
            mostrar_gestionar()
        elif st.session_state.page == "Editar":
            mostrar_editar()

import os
import sys

def obtener_ruta_recurso(rel_path):
    """Obtiene la ruta absoluta para recursos, compatible con PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

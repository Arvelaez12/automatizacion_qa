import json
import logging
from playwright.sync_api import Page
from pages.recuperar_page import RecuperarPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_recuperacion_leyendo_json(page: Page):
    """
    Caso de Prueba Avanzado: Validar flujo de recuperación combinando 
    el patrón arquitectónico POM con carga dinámica de datos desde JSON.
    """
    
    # 1. CARGA DE DATOS: Abrimos y decodificamos el archivo externo
    logging.info("Cargando variables dinámicas desde datos_prueba.json...")
    with open("datos_prueba.json", "r") as archivo:
        datos = json.load(archivo)
        
    # 2. ARQUITECTURA: Inicializamos nuestro Page Object
    pantalla_recuperar = RecuperarPage(page)
    
    # 3. PROCESO: Navegamos y accionamos usando el diccionario 'datos'
    logging.info("Abriendo la URL extraída del JSON...")
    page.goto(datos["url_recuperar"])
    
    logging.info(f"Enviando la información del correo: {datos['correo_repaso']}")
    pantalla_recuperar.ejecutar_recuperacion(datos["correo_repaso"])
    
    # 4. INSPECTOR DE CALIDAD: Validación final
    texto_real = pantalla_recuperar.extraer_texto_de_respuesta()
    assert "Server" in texto_real
    logging.info("🏆 [ASSERT PASSED] - Prueba Data-Driven finalizada con éxito absoluto.")
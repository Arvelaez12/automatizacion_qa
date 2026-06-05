import json
import logging
from playwright.sync_api import Page
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_login_leyendo_datos_externos(page: Page):
    """
    Caso de Prueba: Validar inicio de sesión extrayendo la URL 
    y las credenciales desde un archivo JSON externo.
    """
    
    # 1. Cargamos y leemos el archivo JSON de datos
    logging.info("Cargando credenciales desde el archivo datos_prueba.json...")
    with open("datos_prueba.json", "r") as archivo:
        datos = json.load(archivo)
    
    # 2. Inicializamos el Page Object tradicional
    login_page = LoginPage(page)
    
    # 3. Ejecutamos las acciones usando las variables del JSON en vez de texto fijo
    logging.info("Abriendo la URL externa...")
    page.goto(datos["url_login"])
    
    logging.info(f"Iniciando sesión con el usuario: {datos['usuario_valido']}")
    login_page.login(datos["usuario_valido"], datos["password_valido"])
    
    # 4. Verificación de QA
    mensaje = login_page.obtener_mensaje_alerta()
    assert "You logged into a secure area!" in mensaje
    logging.info("🏆 [PASSED] - Autenticación exitosa utilizando datos centralizados en JSON.")
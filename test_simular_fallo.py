import logging
from playwright.sync_api import Page
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_verificar_comportamiento_en_fallo(page: Page):
    """
    Caso de Prueba Diseñado para Fallar: Validar que el sistema 
    capture el error y lo asocie al reporte HTML.
    """
    login_page = LoginPage(page)
    
    logging.info("Abriendo la web de login...")
    login_page.navegar()
    
    logging.info("Enviando credenciales correctas...")
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    mensaje = login_page.obtener_mensaje_alerta()
    
    logging.info("Forzando aserción falsa para simular un fallo real de la aplicación...")
    # Buscaremos una palabra que NO está en el mensaje para obligar a PyTest a marcarlo en rojo
    assert "ESTO VA A FALLAR" in mensaje
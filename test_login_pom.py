import logging
from playwright.sync_api import Page
# Importamos nuestra clase desde la carpeta pages
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_login_con_patron_pom(page: Page):
    """
    Caso de Prueba: Verificar autenticación utilizando la arquitectura
    profesional Page Object Model (POM).
    """
    # 1. Inicializamos el objeto de la página pasando el control del navegador
    login_page = LoginPage(page)
    
    # 2. Ejecutamos las acciones leyendo el script casi como lenguaje natural
    logging.info("Abriendo pantalla de login...")
    login_page.navegar()
    
    logging.info("Enviando credenciales de usuario mediante POM...")
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    # 3. Validamos el resultado final
    mensaje = login_page.obtener_mensaje_alerta()
    
    assert "You logged into a secure area!" in mensaje
    logging.info("🏆 [PASSED] - Prueba completada con arquitectura POM exitosamente.")
import logging
from playwright.sync_api import Page
# Importamos explícitamente nuestra clase desde su carpeta
from pages.recuperar_page import RecuperarPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_recuperacion_con_arquitectura_pom(page: Page):
    """
    Caso de Prueba: Validar flujo de recuperación de accesos 
    utilizando el patrón arquitectónico Page Object Model (POM).
    """
    # 1. Inicializamos el objeto pasándole el control de la pestaña activa
    pantalla_recuperar = RecuperarPage(page)
    
    # 2. Ejecutamos los pasos leyendo el script casi en lenguaje natural
    logging.info("Abriendo interfaz mediante POM...")
    pantalla_recuperar.navegar_a_la_pantalla()
    
    logging.info("Inyectando credenciales usando métodos encapsulados...")
    pantalla_recuperar.ejecutar_recuperacion("alberto.pom@test.com")
    
    # 3. Validación de QA mediante el Inspector de Calidad
    texto_real = pantalla_recuperar.extraer_texto_de_respuesta()
    
    assert "Server" in texto_real
    logging.info("🏆 [ASSERT PASSED] - Suite validada con arquitectura profesional POM.")
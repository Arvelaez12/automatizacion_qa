import logging
from playwright.sync_api import Page

# Configuramos los logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_inicio_sesion_exitoso(page: Page):
    """
    Caso de Prueba: Verificar el login exitoso en el portal seguro.
    Nota: PyTest nos regala el objeto 'page' automáticamente, ya no necesitamos 
    escribir 'with sync_playwright()' ni levantar el navegador a mano.
    """
    
    logging.info("Navegando al portal de login...")
    page.goto("https://the-internet.herokuapp.com/login")
    
    logging.info("Ingresando credenciales...")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    
    logging.info("Enviando formulario...")
    page.locator("button[type='submit']").click()
    
    # Capturamos el texto del mensaje
    texto_mensaje = page.locator("#flash").inner_text()
    
    # LA ASERCIÓN (La verificación real de QA)
    # Si la frase de la izquierda está dentro de 'texto_mensaje', la prueba pasa. 
    # Si no, PyTest la marca como FALLIDA de inmediato.
    assert "You logged into a secure area!" in texto_mensaje
    logging.info("🏆 Verificación exitosa del caso de prueba.")
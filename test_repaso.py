import logging
# Importamos el tipo de objeto "Page" para que el editor sepa qué comandos sugerirnos
from playwright.sync_api import Page

# Configuramos los logs para que nos muestren la hora y el texto en la terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_mi_primer_formulario_analizado(page: Page):
    """
    Caso de Prueba: Entrar a una pantalla de prueba, escribir el correo 
    usando su ID, avanzar y validar el resultado con un Assert.
    """
    
    # 1. NAVEGACIÓN
    logging.info("Iniciando el robot y navegando a la página de pruebas...")
    page.goto("https://the-internet.herokuapp.com/forgot_password")
    
    # 2. LOCALIZACIÓN Y ACCIÓN
    logging.info("Buscando el campo de correo mediante su ID '#email'...")
    # Buscamos el elemento <input id="email"> e inyectamos el texto
    page.locator("#email").fill("alberto.qa@testing.com")
    
    logging.info("Haciendo clic en el botón de recuperar usando su ID '#form_submit'...")
    # Buscamos el botón <button id="form_submit"> y lo presionamos
    page.locator("#form_submit").click()
    
    # 3. EL INSPECTOR DE CALIDAD (ASSERT)
    logging.info("Esperando la respuesta del servidor para validar...")
    
    # Supongamos que si funciona, la web nos muestra un texto en pantalla que dice "Internal Server Error" o similar.
    # Vamos a extraer el texto del cuerpo entero de la página web (la etiqueta <body>)
    texto_pantalla = page.locator("body").inner_text()
    
    # Afirmamos que la palabra "Error" o "Server" debe estar presente en la respuesta
    assert "Server" in texto_pantalla
    logging.info("🏆 [ASSERT PASSED] - La prueba se completó y la validación fue exitosa.")
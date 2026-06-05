import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_validacion_profunda_json():
    """
    Caso de Prueba Backend Avanzado: Validar el código de estado 
    y auditar que los datos internos del JSON correspondan a la URL esperada.
    """
    url_servidor = "https://httpbin.org/get"
    
    # 1. Enviamos la petición GET
    respuesta = requests.get(url_servidor)
    
    # 2. Convertimos el JSON de la API en un diccionario de Python fácil de leer
    datos_recibidos = respuesta.json()
    
    # 3. INSPECTOR DE CALIDAD 1: Código de estado 200
    assert respuesta.status_code == 200
    logging.info("🏆 [ASSERT 1 PASSED] - Código 200 OK verificado.")
    
    # 4. INSPECTOR DE CALIDAD 2: Validar el contenido interno del JSON
    # Vamos a meternos dentro de la clave 'url' del JSON y verificar su valor
    url_interna_json = datos_recibidos["url"]
    logging.info(f"Auditanado la URL interna devuelta por el servidor: {url_interna_json}")
    
    assert url_interna_json == "https://httpbin.org/get"
    logging.info("🏆 [ASSERT 2 PASSED] - Los datos internos del servidor son correctos y coinciden con la petición.")
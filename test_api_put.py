import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_modificacion_usuario_put():
    """
    Caso de Prueba Backend: Modificar los datos de un usuario existente 
    usando PUT y validar que el servidor guarde los cambios.
    """
    url_servidor = "https://httpbin.org/put"
    
    # LÓGICA DE PYTHON: Definimos los datos ya modificados.
    # El usuario mantiene su nombre, pero cambió de puesto y herramientas.
    datos_actualizados = {
        "nombre": "Alberto",
        "puesto": "QA Automation Engineer (¡Ascendido!)",
        "herramientas": ["Python", "Playwright", "Git", "Requests"]
    }
    
    logging.info("Enviando petición PUT para modificar el registro...")
    
    # SINTAXIS: Usamos requests.put() y le pasamos los datos actualizados en el parámetro json
    respuesta = requests.put(url_servidor, json=datos_actualizados)
    
    # 1. VALIDACIÓN FÍSICA: Código de estado 200 OK
    assert respuesta.status_code == 200
    logging.info("🏆 [ASSERT 1 PASSED] - El servidor aceptó la actualización.")
    
    # Traducimos a diccionario para auditar las entrañas del JSON
    datos_servidor = respuesta.json()
    
    # 2. VALIDACIÓN DE LÓGICA: Verificamos si el puesto cambió de verdad
    puesto_recibido = datos_servidor["json"]["puesto"]
    logging.info(f"Auditanado nuevo puesto en el servidor: {puesto_recibido}")
    
    assert puesto_recibido == "QA Automation Engineer (¡Ascendido!)"
    logging.info("🏆 [ASSERT 2 PASSED] - Los datos se actualizaron correctamente en el Backend.")
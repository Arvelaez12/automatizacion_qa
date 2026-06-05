import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_creacion_usuario_post():
    """
    Caso de Prueba Backend: Enviar datos de un nuevo usuario 
    usando POST y validar que el servidor los reciba correctamente.
    """
    url_servidor = "https://httpbin.org/post"
    
    # LÓGICA DE PYTHON: Creamos un diccionario con los datos que queremos enviar
    # Esto simula lo que el usuario escribiría en un formulario web
    nuevo_prospecto = {
        "nombre": "Alberto",
        "puesto": "QA Automation Jr",
        "herramientas": ["Python", "Playwright", "Git"]
    }
    
    logging.info("Enviando petición POST con el cuerpo de datos (Creando registro)...")
    
    # Enviamos el POST. Fíjate que usamos el parámetro json= para adjuntar nuestra caja de datos
    respuesta = requests.post(url_servidor, json=nuevo_prospecto)
    
    # 1. VALIDACIÓN FISICA: Verificamos que el servidor responda con éxito
    # En creación, los servidores suelen responder con 200 OK o 201 Created. Httpbin responde 200.
    assert respuesta.status_code == 200
    logging.info("🏆 [ASSERT 1 PASSED] - Servidor procesó el POST con éxito.")
    
    # Traducimos la respuesta a un diccionario de Python para auditarlo
    datos_servidor = respuesta.json()
    
    # 2. VALIDACIÓN DE LÓGICA INTERNA:
    # Httpbin guarda lo que le enviaste dentro de una clave llamada "json".
    # Vamos a extraer el nombre que el servidor recibió para ver si se corrompió en el camino.
    nombre_recibido = datos_servidor["json"]["nombre"]
    logging.info(f"Auditanado nombre guardado en el servidor: {nombre_recibido}")
    
    # Aplicamos el inspector de calidad
    assert nombre_recibido == "Alberto"
    logging.info("🏆 [ASSERT 2 PASSED] - El servidor guardó el nombre correcto sin corrupción de datos.")
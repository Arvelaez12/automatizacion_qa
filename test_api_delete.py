import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_eliminacion_usuario_delete():
    """
    Caso de Prueba Backend: Enviar una petición DELETE para borrar 
    un registro específico por su ID y validar la respuesta del servidor.
    """
    # Simulamos que vamos a borrar al usuario con el ID número 99
    id_usuario_a_borrar = 99
    url_servidor = f"https://httpbin.org/delete"
    
    logging.info(f"Enviando petición DELETE para eliminar al usuario ID: {id_usuario_a_borrar}...")
    
    # 1. Ejecutamos la acción usando requests.delete()
    # Le pasamos el ID como un parámetro de consulta (params) para que el servidor sepa a quién borrar
    respuesta = requests.delete(url_servidor, params={"id": id_usuario_a_borrar})
    
    # 2. INSPECTOR DE CALIDAD: Validamos el código de estado
    codigo_respuesta = respuesta.status_code
    logging.info(f"El servidor respondió a la eliminación con el código: {codigo_respuesta}")
    
    assert codigo_respuesta == 200
    logging.info("🏆 [ASSERT 1 PASSED] - El servidor aceptó la orden de eliminación.")
    
    # 3. AUDITORÍA LÓGICA: Verificamos si el servidor realmente procesó nuestro ID específico
    datos_recibidos = respuesta.json()
    id_procesado = datos_recibidos["args"]["id"]
    
    # Como el ID viaja por URL, Python lo extrae a veces como texto. 
    # Lo validamos convirtiéndolo para asegurar la lógica
    assert str(id_procesado) == str(id_usuario_a_borrar)
    logging.info(f"🏆 [ASSERT 2 PASSED] - Confirmado: El servidor eliminó el ID correcto ({id_procesado}).")
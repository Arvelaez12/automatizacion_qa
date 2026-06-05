import logging
from playwright.sync_api import Page

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_manejo_checkboxes_y_captura(page: Page):
    """
    Caso de Prueba: Interactuar con elementos tipo Checkbox 
    y guardar una captura de pantalla como evidencia de QA.
    """
    
    logging.info("Navegando a la página de Checkboxes...")
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    
    # 1. Localizamos los dos checkboxes de la página.
    # Como hay dos elementos iguales, usamos .nth(0) para el primero y .nth(1) para el segundo.
    checkbox_1 = page.locator("input[type='checkbox']").nth(0)
    checkbox_2 = page.locator("input[type='checkbox']").nth(1)
    
    # 2. Validación inicial: Verificamos el estado de fábrica de las casillas
    logging.info(f"¿El Checkbox 1 está marcado inicialmente?: {checkbox_1.is_checked()}")
    logging.info(f"¿El Checkbox 2 está marcado inicialmente?: {checkbox_2.is_checked()}")
    
    # 3. Acción: Marcamos el Checkbox 1 (que viene desmarcado) usando .check()
    logging.info("Marcando el Checkbox 1 de forma automatizada...")
    checkbox_1.check()
    
    # 4. Aserción de QA: Comprobamos que ahora SÍ esté marcado de verdad
    assert checkbox_1.is_checked() == True
    logging.info("🏆 [PASSED] - El Checkbox 1 se marcó correctamente.")
    
    # 5. EL TRUCO DE HOY: Tomar captura de pantalla de evidencia
    logging.info("Tomando captura de pantalla de la interfaz...")
    page.screenshot(path="evidencia_checkboxes.png")
    logging.info("📸 Captura guardada con éxito como 'evidencia_checkboxes.png'.")


def test_manejo_listas_desplegables(page: Page):
    """
    Caso de Prueba: Interactuar con un menú desplegable (Dropdown)
    y validar que la opción seleccionada sea la correcta.
    """
    
    logging.info("Navegando a la página de Dropdowns...")
    page.goto("https://the-internet.herokuapp.com/dropdown")
    
    # 1. Localizamos el elemento select en el HTML usando su ID
    menu_desplegable = page.locator("#dropdown")
    
    # 2. Acción: Seleccionamos la 'Option 2' usando el texto visible (label)
    logging.info("Seleccionando la 'Option 2' de la lista...")
    menu_desplegable.select_option(label="Option 2")
    
    # Un pequeño tiempo de espera fijo de 2 segundos SOLO para que alcances a ver 
    # visualmente el cambio en la pantalla en el modo headed
    page.wait_for_timeout(2000)
    
    # 3. Validación de QA: Verificamos qué opción quedó activa en la interfaz
    # Buscamos la opción que tiene el atributo 'selected' dentro del menú
    opcion_activa = page.locator("#dropdown option[selected='selected']")
    texto_seleccionado = opcion_activa.inner_text()
    
    logging.info(f"Opción que quedó seleccionada en la web: {texto_seleccionado}")
    
    # Aserción final
    assert texto_seleccionado == "Option 2"
    logging.info("🏆 [PASSED] - El Dropdown cambió de opción correctamente.")

def test_manejo_alertas_javascript(page: Page):
    """
    Caso de Prueba: Detectar, leer el texto y aceptar una alerta 
    nativa de JavaScript de forma automatizada.
    """
    
    logging.info("Navegando a la página de Alertas de JavaScript...")
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # 1. Definimos el "escuchador" (Listener) antes de abrir la alerta.
    # Le decimos al navegador qué hacer cuando el evento 'dialog' ocurra.
    def manejar_alerta(dialog):
        logging.info(f"💬 Alerta detectada con el mensaje: '{dialog.message}'")
        # Validamos que el texto dentro de la alerta sea el esperado
        assert dialog.message == "I am a JS Alert"
        # Hacemos clic automáticamente en el botón 'Aceptar' de la alerta
        dialog.accept()

    # Activamos el escuchador en la página actual
    page.on("dialog", manejar_alerta)
    
    # 2. Acción: Hacemos clic en el primer botón que detona la alerta
    logging.info("Haciendo clic en el botón que activa la alerta nativa...")
    page.locator("button[onclick='jsAlert()']").click()
    
    # 3. Validación de QA: Verificamos que la página registre que aceptamos la alerta
    texto_resultado = page.locator("#result").inner_text()
    logging.info(f"Resultado en la interfaz web: {texto_resultado}")
    
    assert texto_resultado == "You successfully clicked an alert"
    logging.info("🏆 [PASSED] - Alerta procesada y aceptada con éxito.")   

def test_carga_de_archivos(page: Page):
    """
    Caso de Prueba: Seleccionar un archivo del sistema local 
    y subirlo a la plataforma web de forma automatizada.
    """
    
    logging.info("Navegando a la página de carga de archivos...")
    page.goto("https://the-internet.herokuapp.com/upload")
    
    # 1. Definimos la ruta del archivo que queremos subir.
    # Usaremos la imagen 'evidencia_checkboxes.png' que ya existe en tu carpeta.
    ruta_archivo = "evidencia_checkboxes.png"
    
    # 2. Localizamos el botón de entrada de archivos en el HTML usando su ID
    boton_seleccionar_archivo = page.locator("#file-upload")
    
    # 3. Acción: Le inyectamos el archivo directamente al elemento
    logging.info(f"Subiendo el archivo '{ruta_archivo}' al servidor de pruebas...")
    boton_seleccionar_archivo.set_input_files(ruta_archivo)
    
    # 4. Hacemos clic en el botón de 'Upload' para enviar el formulario
    logging.info("Haciendo clic en el botón de cargar (Upload)...")
    page.locator("#file-submit").click()
    
    # 5. Validación de QA: Verificamos si la página muestra el mensaje de éxito
    texto_confirmacion = page.locator("h3").inner_text()
    logging.info(f"Respuesta del servidor: {texto_confirmacion}")
    
    assert texto_confirmacion == "File Uploaded!"
    logging.info("🏆 [PASSED] - Archivo cargado y validado con éxito de punta a punta.")     
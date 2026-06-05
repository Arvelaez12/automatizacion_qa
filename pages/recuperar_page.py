from playwright.sync_api import Page

class RecuperarPage:
    def __init__(self, page: Page):
        """
        El Constructor: Aquí es donde inicializamos el control de la pestaña 
        y definimos de forma centralizada todos los selectores HTML.
        """
        self.page = page
        
        # CENTRALIZACIÓN DE LOCALIZADORES (El plano de la pantalla)
        self.input_correo = page.locator("#email")
        self.boton_enviar = page.locator("#form_submit")
        self.cuerpo_pagina = page.locator("body")

    # ACCIONES MECÁNICAS (Los movimientos del robot)
    def navegar_a_la_pantalla(self):
        self.page.goto("https://the-internet.herokuapp.com/forgot_password")

    def ejecutar_recuperacion(self, correo_usuario):
        # Usamos las variables que definimos arriba en el constructor
        self.input_correo.fill(correo_usuario)
        self.boton_enviar.click()

    def extraer_texto_de_respuesta(self):
        return self.cuerpo_pagina.inner_text()
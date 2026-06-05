from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        # Le damos el control del navegador a nuestra clase
        self.page = page
        
        # DEFINICIÓN DE LOCALIZADORES (Si cambian en la web, solo se tocan aquí)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")
        self.message_flash = page.locator("#flash")

    # ACCIONES DE LA PÁGINA
    def navegar(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, usuario, password):
        self.username_input.fill(usuario)
        self.password_input.fill(password)
        self.submit_button.click()

    def obtener_mensaje_alerta(self):
        return self.message_flash.inner_text()
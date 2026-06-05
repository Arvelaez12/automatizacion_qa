import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        html = item.config.pluginmanager.getplugin("html")
        if html is not None:
            page = item.funcargs.get("page")
            if page is not None:
                # Tomamos la captura en base64
                screenshot = page.screenshot(type="png")
                import base64
                encoded = base64.b64encode(screenshot).decode("utf-8")
                
                # Creamos el bloque HTML de la imagen
                imagen_html = f'<div><img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:600px;height:auto;" /></div>'
                
                # Inyectamos de forma segura usando una lista limpia sin llaves ni paréntesis raros
                if not hasattr(report, "extra"):
                    report.extra = []
                report.extra.append(html.extras.html(imagen_html))
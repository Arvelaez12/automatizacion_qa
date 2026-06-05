# Definimos la lista del menú web
menu_web = ["Inicio", "Tienda", "Nosotros", "Contacto"]

print("--- ESCANEO AUTOMÁTICO DE MENÚ ---")

# Iniciamos el bucle: 'opcion' guardará un elemento a la vez en cada vuelta
for opcion in menu_web:
    print("Analizando elemento visual: " + opcion)
    
    # Dentro del bucle podemos meter un condicional IF
    if opcion == "Contacto":
        print("   🎯 ¡ÉXITO! Encontramos el botón de Contacto en el código.")
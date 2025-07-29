# principal.py

# Variables globales para guardar el estado de la aplicación.
# Son "globales" porque su valor puede cambiar en diferentes partes del programa
# y necesitamos que esos cambios se mantengan.
usuario_actual = None
# color_detectado será un diccionario fijo para "Azul Turquesa"
color_detectado = {
    "nombre": "Azul Turquesa",
    "mezcla_instrucciones": "Base Blanca (2L) + Tinte Azul (0.8L) + Tinte Verde (0.2L)"
}
cantidad_pintura = None
nombre_proyecto_actual = None

# --- Funciones de Simulación ---

def simular_inicio_sesion():
    """
    Simula la acción de iniciar sesión.
    Pedirá al usuario un email y una contraseña para simular la interacción.
    """
    print("\n--- INICIO DE SESIÓN ---")
    print("Por favor, ingresa tus credenciales para simular el acceso.")
    email = input("Correo Electrónico: ")
    contrasena = input("Contraseña: ")

    # En una aplicación real, aquí validarías contra una base de datos.
    # Para esta simulación, cualquier entrada es válida para avanzar.
    print(f"\nSimulando verificación de credenciales para '{email}'...")
    print("¡Inicio de sesión exitoso!")
    return True # Siempre retorna True para que el programa avance

def simular_detectar_color():
    """
    Simula la detección de un color, fijándolo siempre a "Azul Turquesa".
    """
    print("\n--- DETECTAR COLOR ---")
    print("Imagina que aquí subes una foto o apuntas con la cámara.")
    print(f"\n¡Color Detectado Exitosamente!")
    print(f"  Color: {color_detectado['nombre']}")
    print(f"  **Instrucciones de Mezcla para {color_detectado['nombre']}:**")
    print(f"    {color_detectado['mezcla_instrucciones']}")
    return color_detectado

def simular_color_en_espacio(datos_color, cantidad):
    """
    Simula la aplicación de un color detectado en un espacio.
    """
    print("\n--- SIMULAR COLOR EN ESPACIO ---")
    print("Imagina que aquí subes una foto de la pared que quieres pintar.")
    nombre_espacio = input("¿Cómo se llama el espacio donde quieres simular el color? (ej. 'sala', 'habitación'): ")

    color_nombre = datos_color["nombre"]
    
    print(f"\nSimulando... ¡Visualiza tu '{nombre_espacio}' pintada de '{color_nombre}'!")
    print(f"  Necesitarías aproximadamente {cantidad} litros de pintura para este espacio.")
    print("\n(Aquí iría una representación visual del color en la pared en una aplicación real.)")

def simular_generar_instrucciones(color_info, cantidad):
    """
    Genera y muestra instrucciones detalladas de pintado
    para el color y la cantidad especificados.
    """
    print("\n--- GENERAR INSTRUCCIONES ---")
    print(f"**Instrucciones Detalladas para tu Proyecto '{color_info['nombre']}'**")
    print(f"\nColor Final Deseado: {color_info['nombre']}")
    print(f"Cantidad Estimada Necesaria: {cantidad} Litros")
    print(f"\nInstrucciones de Mezcla: {color_info['mezcla_instrucciones']}")
    print("\nPasos para la Preparación:")
    print("1. Asegúrate de que la superficie esté limpia y seca.")
    print("2. Protege las áreas que no deseas pintar (cinta, plásticos).")
    print("\nPasos para la Aplicación:")
    print("1. Mezcla bien la pintura antes de usarla.")
    print("2. Aplica la primera capa de manera uniforme.")
    print("3. Deja secar completamente antes de aplicar capas adicionales.")
    print("4. Limpia tus herramientas inmediatamente después de usarlas.")

def simular_guardar_proyecto(nombre_proyecto, color_info, cantidad):
    """
    Simula el guardado de un proyecto.
    """
    print("\n--- GUARDAR PROYECTO ---")
    print(f"¡Proyecto '{nombre_proyecto}' guardado exitosamente!")
    print(f"  Detalles: Color {color_info['nombre']}, {cantidad} Litros.")
    return True

def simular_compartir_proyecto(nombre_proyecto):
    """
    Simula la acción de compartir un proyecto.
    """
    print("\n--- COMPARTIR PROYECTO ---")
    print(f"¡Proyecto '{nombre_proyecto}' listo para compartir!")
    print("Selecciona cómo te gustaría compartirlo: (Simulación)")
    print("  - Por WhatsApp")
    print("  - Por Correo Electrónico")
    print("  - Copiar Enlace")
    print("\n(Imagina que aquí el sistema abriría las opciones para compartir de tu dispositivo.)")

# --- Fin de Funciones de Simulación ---


def mostrar_menu_principal():
    """
    Muestra el menú principal de la aplicación PINTUBOL
    y maneja la elección del usuario.
    """
    global cantidad_pintura, nombre_proyecto_actual

    while True:
        print("\n--- PINTUBOL: Panel Principal ---")
        print("1. Detectar Color")
        print("2. Simular Color en Espacio (en una imagen de tu pared)")
        print("3. Generar Instrucciones de Pintado")
        print("4. Guardar Proyecto")
        print("5. Compartir Proyecto")
        print("6. Salir de la aplicación")

        opcion = input("Por favor, elige una opción (1-6): ")

        if opcion == '1':
            simular_detectar_color()
            print(f"Color activo: {color_detectado['nombre']}")
            
        elif opcion == '2':
            if not cantidad_pintura:
                 cantidad_pintura = input("¿Cuántos litros de pintura necesitas para simular? ")
            simular_color_en_espacio(color_detectado, cantidad_pintura)
            

        elif opcion == '3':
            if not cantidad_pintura:
                print("Primero especifica la cantidad de pintura en la opción '2. Simular Color en Espacio'.")
            else:
                simular_generar_instrucciones(color_detectado, cantidad_pintura)

        elif opcion == '4':
            if cantidad_pintura:
                nombre_proyecto = input("Dale un nombre a tu proyecto (ej. 'Mi Sala Azul'): ")
                if simular_guardar_proyecto(nombre_proyecto, color_detectado, cantidad_pintura):
                    nombre_proyecto_actual = nombre_proyecto
            else:
                print("No hay un proyecto completo para guardar. Necesitas especificar la cantidad de pintura en la opción '2'.")

        elif opcion == '5':
            if nombre_proyecto_actual:
                simular_compartir_proyecto(nombre_proyecto_actual)
            else:
                print("No hay un proyecto guardado para compartir. Guarda uno primero (opción '4').")

        elif opcion == '6':
            print("¡Gracias por usar PINTUBOL! ¡Hasta la próxima!")
            break
        
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 6.")

# Este es el punto de inicio de tu programa.
if __name__ == "__main__":
    print("--- Bienvenido a PINTUBOL ---")
    # Llama a la simulación de inicio de sesión.
    # Si esta simulación es "exitosa", entonces muestra el menú principal.
    if simular_inicio_sesion():
        mostrar_menu_principal()
# PINTUBOL - Aplicación de Consola

Este es un prototipo básico en consola de la aplicación "PINTUBOL", desarrollado en Python. Simula las funcionalidades clave de un asistente de pintura, incluyendo la detección de color, simulación en un espacio, generación de instrucciones, y la capacidad de guardar y compartir proyectos.

**¿Qué hace esta aplicación?**

* **Simulación de Inicio de Sesión:** Antes de acceder al menú principal, el sistema simula un proceso de login con entrada de usuario y contraseña.
* **Detectar Color (Simulado):** Identifica un color predefinido ("Azul Turquesa") a partir de una "imagen de referencia" simulada. Proporciona instrucciones de mezcla específicas para este color.
* **Simular Color en Espacio:** Simula cómo se vería el color "Azul Turquesa" en un espacio de tu elección (se te pedirá un nombre de espacio y la cantidad de pintura necesaria).
* **Generar Instrucciones:** Muestra instrucciones detalladas para la preparación, mezcla y aplicación del color "Azul Turquesa", basándose en la cantidad de pintura especificada.
* **Guardar Proyecto:** Permite "guardar" los detalles del proyecto (color y cantidad) con un nombre que tú elijas.
* **Compartir Proyecto:** Simula la acción de compartir un proyecto previamente guardado, mostrando opciones genéricas de plataforma.

---

### **Cómo Ejecutar la Aplicación:**

1.  **Asegúrate de tener Python instalado:**
    * Puedes verificarlo abriendo tu terminal/CMD y escribiendo `python --version` (o `python3 --version`). Necesitas Python 3.x.
    * Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2.  **Abre el Proyecto en Visual Studio Code:**
    * Navega a la carpeta `pintubol_app` en tu computadora.
    * Abre Visual Studio Code.
    * Ve a `Archivo > Abrir Carpeta...` y selecciona `pintubol_app`.

3.  **Ejecuta el Programa:**
    * Abre la terminal integrada en VS Code: Ve a `Terminal > Nueva Terminal` (o presiona `Ctrl + J` / `Cmd + J`).
    * Asegúrate de estar en la carpeta raíz del proyecto (`pintubol_app`). Si no lo estás, usa `cd pintubol_app` (o el nombre de tu carpeta).
    * Ejecuta el programa con el siguiente comando:
        ```bash
        python principal.py
        ```
    * La aplicación se iniciará en la consola, primero pidiéndote que simules el inicio de sesión.

---

### **Interacción con la Aplicación:**

* Al iniciar, se te pedirá un correo electrónico y una contraseña para simular el login.
* Una vez dentro, verás el menú principal. Sigue las instrucciones que aparecen en la consola.
* Cuando se te pida, ingresa números del 1 al 6 para elegir las opciones del menú.
* Ingresa texto cuando se te pida (ej. el nombre del espacio, la cantidad de pintura o el nombre del proyecto).

**Nota Importante:** Esta es una implementación simulada para demostrar el flujo de usuario. No procesa imágenes reales, ni realiza cálculos complejos, ni guarda datos de forma persistente (a menos que añadas esa funcionalidad más adelante). La detección de color está fijada al "Azul Turquesa" para simplificar el prototipo.
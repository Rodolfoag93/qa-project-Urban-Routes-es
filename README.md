# Urban Routes Test Automation

Este proyecto automatiza pruebas de interfaz gráfica para la aplicación **Urban Routes** utilizando Python y Selenium.

## Características

- Automatización de flujo completo de usuario:
  - Selección de ruta
  - Selección de tarifa
  - Autenticación por SMS
  - Agregado de método de pago
  - Selección de extras como helado, manta, pañuelos, etc.
- Validaciones con `assert` para confirmar comportamiento esperado
- Uso de `WebDriverWait` para condiciones dinámicas

## Requisitos

- Python 3.8+
- Google Chrome y ChromeDriver
- Paquetes de Python:

```bash
pip install -r requirements.txt
Contenido de requirements.txt (ejemplo):

txt
Copiar
Editar
selenium>=4.10.0
Uso
Ejecuta las pruebas con:

bash
Copiar
Editar
pytest main.py
O directamente:

bash
Copiar
Editar
python main.py
Estructura del proyecto
plaintext
Copiar
Editar
urban-routes-qa/
│
├── main.py                  # Contiene las pruebas
├── page_objects.py          # Clase PageObject con métodos de interacción
├── data.py                  # Datos de prueba como rutas, teléfonos, etc.
├── configuration.py         # URLs y endpoints
├── README.md                # Este archivo
└── requirements.txt         # Dependencias
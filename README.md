
# Automatizacion

Prueba Practica de automatizacion.

# Información del aspirante

- **Nombre:** Jacobo Ordoñez
- **Prueba:** Softesting – automatización de formulario web
- **Repositorio:** <https://github.com/jigat2/P1>

# Herramientas

| Herramienta | Uso |
|---|---|
| Python 3.10+ | Lenguaje |
| Selenium WebDriver | Automatización del navegador |
| Google Chrome + ChromeDriver | Navegador (Selenium Manager descarga el driver automáticamente) |
| VS Code | Editor |
| Git / GitHub | Control de versiones |

## Gestor de dependencias y librerías

- **Gestor:** `pip` (con entorno virtual `venv`)
- **Librerías:**
  - `selenium` (clases `webdriver`, `By`, `Keys`, `WebDriverWait`, `expected_conditions`)
  - Librerías estándar: `os`, `time`, `datetime`

Instalación:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install selenium
```

## Estructura

```
Softesting/
├── main.py            # Script principal del robot
├── Entrada.py         # Datos de entrada (nombre, email, género, etc.)
├── JOT FOTO.jpeg      # Imagen que se carga en "Select picture"
└── README.md
```

## Ejecución

Desde la carpeta del proyecto, con el entorno virtual activo:

```powershell
python main.py
```

El robot abre Chrome, entra a DemoQA, completa los campos (nombre, apellido, email, género, móvil, fecha de nacimiento, materias, hobbies y foto) y deja el navegador abierto unos segundos.

# Configuración de datos

Edita [Entrada.py](./Entrada.py) para cambiar los valores:

```python
NAME = "..."
LASTNAME = "..."
EMAIL = "..."
GENDER = "Male"            
MOBILE = "..."             
DATE_OF_BIRTH = "DD-MM-YYYY"
SUBJECTS = ["Maths", "Physics"]
HOBBIES = "Music"          
```



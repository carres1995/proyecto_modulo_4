Carlos Andres Restrepo Yepes
Proyecto de certificacion - Modulo 4
Python Full Stack Developer

Este es el proyecto generado en el modulo 4 el cual se le aplicaron las siguientes mejoras:


-  **Validaciones centralizadas** para entradas de usuario mediante funciones en "utils/validators.py"
-  **Manejo de errores con decoadores ("@manejar_errores")** para simplificar el uso de "try/except" y mantener el codigo mas limpio
-  **Modulacion escalable** dividiendo la logica en capas:
  - "model/" = modelos ORM
  - "crud/" = funciones de acceso a base de datos
  - "services/" = logica de negocio
  - "view/" = presentacion (PrettyTable, impresion)
  - "main_t/" = menus interactivos
  - "utils/" = funcionalidades de errores, validaciones, logs
  - "data/" = Inicializacion y logica de la base de datos.
  
-  **Limpieza de pantalla automatica** al navegar entre menus
-  **transicion completa a SQLAlchemy** para manjo de base de datos relacional
-  **Creacion de entorno virtual ("venv")** para aislar las dependencias del proyecto
-  **Archivo "requirements.txt"** generado para registrar y actualizar dependencias facilmente



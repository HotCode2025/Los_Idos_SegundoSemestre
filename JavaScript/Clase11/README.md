**Clase 11 Cosas importantes en JavaScript -> Tarea**

1. **FUNCIONES TIENEN QUE VER CON LA MANIPULACIÓN DE DATOS**

**calculateTotalPrice()**
Significado: calcular el precio total
Qué hace:
• 	Suma precios individuales (por ejemplo, de productos en un carrito).
• 	Puede incluir impuestos, descuentos o envíos.
• 	Devuelve un número: el total final a pagar.
**_Punto clave:_** útil en e-commerce, facturación o presupuestos.

**FormatUserInput()**
Significado: formatear la entrada del usuario
Qué hace:
• 	Limpia y ajusta lo que el usuario escribe (por ejemplo, eliminar espacios, convertir a minúsculas, etc.).
• 	Previene errores o inconsistencias antes de guardar o procesar datos.
**_Punto clave:_** mejora la calidad de los datos y evita errores en formularios.

**validateEmailAddress()**
Significado: validar dirección de correo electrónico
Qué hace:
• 	Verifica si el email tiene un formato correcto (usuario@dominio.com).
• 	Puede usar expresiones regulares para detectar errores.
**_Punto clave:_** evita guardar correos inválidos y mejora la comunicación con el usuario.

**convertToCamelCase()**
Significado: convertir a formato camelCase
Qué hace:
• 	Transforma cadenas como “nombre completo” en “nombreCompleto”.
• 	Útil para generar nombres de variables o claves en objetos.
**_Punto clave:_** estandariza nombres en código, especialmente en JavaScript.

**filterActiveUser()**
Significado: filtrar usuarios activos
Qué hace:
• 	Recorre una lista de usuarios y devuelve solo los que están activos (isActive === true).
• 	Puede usarse en paneles de administración, dashboards o reportes.
**_Punto clave:_** permite mostrar o procesar solo los datos relevantes.


2. **EVENTOS O INTERACCIÓN**

**handleButtonClick()**
Significado: manejar el clic en un botón
Qué hace:
• 	Se ejecuta cuando el usuario hace clic en un botón.
• 	Puede disparar acciones como abrir un modal, enviar datos, cambiar estilos, etc.
**_Punto clave:_** conecta la interacción del usuario con la lógica del programa.

**onFormSubmit()**
Significado: al enviar el formulario
Qué hace:
• 	Se activa cuando el usuario envía un formulario (<form>).
• 	Valida datos, previene el comportamiento por defecto (event.preventDefault()), y envía la info al servidor o la procesa localmente.
**_Punto clave:_** controla el flujo de datos del formulario y evita errores.

**toggleDarkMode()**
Significado: alternar el modo oscuro
Qué hace:
• 	Cambia entre modo claro y oscuro en la interfaz.
• 	Suele modificar clases CSS o guardar la preferencia en localStorage.
**_Punto clave:_** mejora la experiencia visual y permite personalización.

**updateProgressBar()**
Significado: actualizar la barra de progreso
Qué hace:
• 	Modifica el estado visual de una barra de progreso (por ejemplo, carga de archivos o pasos completados).
• 	Puede cambiar el ancho, color o texto según el avance.
**_Punto clave:_** da feedback visual al usuario sobre el estado de una tarea.

**initializeApp()**
Significado: inicializar la aplicación
Qué hace:
• 	Configura todo lo necesario al arrancar la app: carga datos, configura eventos, prepara el entorno.
• 	Se ejecuta al principio del ciclo de vida de la app.
**_Punto clave:_** es el punto de entrada que pone todo en marcha.


3. **OPERACIONES CRUD**

**createNewUser()**
Significado: crear un nuevo usuario
Qué hace:
• 	Recibe datos como nombre, email, contraseña.
• 	Los guarda en una base de datos o sistema.
• 	Puede incluir validaciones y envío de email de bienvenida.
**_Puntos clave:_**
• 	Se usa en el registro de usuarios.
• 	Debe validar que el usuario no exista previamente.
• 	Suele conectarse con formularios y APIs.

**fetchUserData()**
Significado: obtener datos del usuario
Qué hace:
• 	Recupera información de un usuario desde una base de datos o API.
• 	Puede incluir nombre, email, preferencias, historial, etc.
**_Puntos clave:_**
• 	Se usa al iniciar sesión o cargar un perfil.
• 	Suele usar fetch() o axios para hacer la solicitud.
• 	Debe manejar errores si el usuario no existe o hay problemas de red.

**updateUserProfile()**
Significado: actualizar el perfil del usuario
Qué hace:
• 	Modifica datos como nombre, foto, contraseña, preferencias.
• 	Guarda los cambios en el sistema.
**_Puntos clave:_**
• 	Requiere validación de datos.
• 	Puede incluir confirmación visual o notificación.
• 	Suele protegerse con autenticación.

**deleteUserAccount()**
Significado: eliminar la cuenta del usuario
Qué hace:
• 	Borra la cuenta y todos los datos asociados.
• 	Puede pedir confirmación antes de ejecutar.
• 	A veces se hace una "desactivación" en lugar de borrado total.
**_Puntos clave:_**
• 	Es una acción crítica, debe estar protegida.
• 	Puede tener implicancias legales (protección de datos).
• 	Suele incluir un mensaje de despedida o encuesta de salida.


4. **UTILIDADES**

**generateRandomId()**
Significado: generar un ID aleatorio
Qué hace:
• 	Crea un identificador único (por ejemplo, para usuarios, productos, sesiones, etc.).
• 	Puede usar funciones como  MathRandom() o cripto.RandomUUID() .
**_Puntos clave:_**
• 	Útil para evitar colisiones de datos.
• 	Se usa en bases de datos, formularios, tokens, claves únicas.
• 	En sistemas críticos, conviene usar generadores más seguros como crypto.

**FormatCurrency()**
Significado: formatear como moneda
Qué hace:
• 	Convierte un número en un string con formato monetario.
• 	Ejemplo:  formatcurrency(1234.5)→ ”1234.50 ARS”  (según configuración regional).
**_Puntos clave:_**
• 	Usa  Intl.NumberFormat para adaptar a la moneda y región.
• 	Mejora la presentación de precios en interfaces de usuario.
• 	Evita errores de interpretación por formato decimal o separadores.

**DebounceSearch()**
Significado: desacelerar la búsqueda (con debounce)
Qué hace:
• 	Retrasa la ejecución de una función (como una búsqueda) hasta que el usuario deja de escribir por un tiempo.
• 	Evita hacer muchas llamadas a la API mientras el usuario escribe.
**_Puntos clave:_**
• 	Mejora el rendimiento y reduce llamadas innecesarias.
• 	Se implementa con  setTimeout y clearTimeout .
• 	Ideal para buscadores en tiempo real o filtros dinámicos.

**SanitizeInput()**
Significado: sanear la entrada del usuario
Qué hace:
• 	Limpia el texto ingresado por el usuario para eliminar caracteres peligrosos o no deseados.
• 	Previene ataques como XSS (Cross-Site Scripting).
**_Puntos clave:_**
• 	Fundamental para la seguridad de aplicaciones web.
• 	Puede eliminar etiquetas HTML, scripts, caracteres especiales.
• 	Se usa antes de guardar o mostrar datos ingresados por el usuario.

**CheckPermissions()**
Significado: verificar permisos
Qué hace:
• 	Revisa si un usuario tiene permiso para realizar cierta acción (ver, editar, eliminar, etc.).
• 	Puede comparar roles, tokens o reglas de acceso.
**_Puntos clave:_**
• 	Esencial para controlar el acceso a funciones sensibles.
• 	Se usa en sistemas con autenticación y roles (admin, usuario, invitado).
• 	Mejora la seguridad y evita accesos no autorizados.

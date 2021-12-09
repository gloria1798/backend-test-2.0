# Nombre Proyecto: Google App Engine (GAE) Python Clean Architecture

### Descripción

Plantilla base de un App Engine escrito con Python utilizando Flask, SQL Alchemy, tratando de seguir las convenciones de Clean Architecture.

En este ejemplo, la aplicación contiene dos secciones: una llamada "greeting", que es simplemente un endpoint que retorna un saludo indicando el número del visitante, el cual se obtiene desde un caché, y la otra es "books", que consiste en un CRUD de libros, los cuales son guardados en una base de datos, ya sea en MySQL o en Firestore.

Al ser un proyecto en Python, se siguen las siguientes convenciones:

- Identación de cuatro espacios (no tabulación), incluso en archivos que no son `.py`.
- Nombres de clases en `UpperCamelCase`.
- Métodos, funciones y variables en `snake_case`.
- Nombres de módulos (archivos `.py`) en `snake_case`.
- Nombres de paquetes (carpetas) en `lowercase`, sin guiones bajos incluso si contienen más de una palabra (por ejemplo, "usecases" en vez de "use_cases").
- Usar importaciones absolutas dentro de lo posible.

### Construcción 🛠️
* **Lenguaje:** Python 3
* **Framework:** Flask, SQL Alchemy

### Pre-requisitos 📋

- Docker.

### Instalación 🔧

- Clonar proyecto.
- Crear archivo `.env` en la carpeta raíz. Se incluye archivo `.env.example` como referencia, que se puede usar tal cual como está.
- Ejecutar `docker-compose build` para construir las imágenes de Docker. Sólo es necesario hacerlo una vez.
- Ejecutar `docker-compose up` para levantar los servicios. Es probable que la primera vez la aplicación Flask arroje excepción, debido a que tratará de conectarse con el servicio MySQL que aún está inicializándose por primera vez; en este caso esperar a que MySQL se inicialice completamente primero y luego ejecutar el comando `docker-compose restart $NAME_SERVICE` en otro terminal para reiniciar el servicio caído.

### Despliegue 📦


### Pruebas ⚙️

Para ejecutar pruebas manuales se incluye el archivo `req.http` con las solicitudes a localhost. Instalar `REST Client` para Visual Studio Code o `RESTer HTTP Client` para Sublime Text para poder realizar las solicitudes del archivo desde el mismo editor de texto.

Para ejecutar los tests:

- Tener los servicios corriendo usando `docker-compose up`.
- En otra consola, ejecutar `docker-compose exec gae-service python -m pytest -rP`.

La bandera `-rP` es opcional, y sirve para mostrar en consola los `print()` hechos durante las pruebas, de lo contrario `pytest` los ocultará, sólo mostrándolos en caso de que la prueba haya fallado.

Los tests de los repositorios escriben datos en las bases de datos de los contenedores, pero los escriben en tablas o colecciones temporales con el sufijo "\_test" que se eliminan una vez finalizados, para así no pasar a llevar los datos reales. Tener en cuenta que para el caso de Firestore no hay persistencia de datos aún; si el servicio se baja y se levanta de nuevo, los datos anteriores se pierden.

### Autores ✒️

* **Autor:** Hans Auzian C., hans.auzian@enviame.io
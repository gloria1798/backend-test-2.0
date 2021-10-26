# Prueba backend 2.0

Problema

- Crear Ecommerce, que permita a un administrador crear sellers y productos
    - CRUD sellers
    - CRUD products
- La idea es crear una API que permita generar una compra de estos productos indicando (compras de productos de diferentes sellers)
    - SKU
    - cantidad
    - Direccion de destino (para el despacho)
    - Nombre del comprador
- Cuando se realice una compra queda en estado LOADED, mediante API pasar esta compra de LOADED a CREATED y que esta acción llame al servicio de envios
- Crear Servicio de envios,
    - Servicio debe generar una OT
    - Este servicio debe recibir la orden y responder con tiempos aleatorios entre 2 y 10 min.
        - cuando se responde a Ecommerce la compra debe guardar la OT y pasar al estado "IN_TRANSIT"
    - API que permita cambiar estado en servico de envios y que estos se reflejen en el servico de Ecommerce
- En  Ecommerce
    - Crear API que permita listar las compras de un seller, se considera la compra de un seller si alguno de los productos esta en una compra

Requerimiento

- Crear servicios en diferentes proyectos dockerizados
    - Cada proyecto debe tener su propia base de datos
    - Generar documentación de la solución
    - El cambio de estado de LOADED a CREATED debe responder lo mas rapido posible (async)
    - Proveer un mecanismo para cargar un set de datos a las base de datos
    - Cada compra debe persistir en su base de datos
    - Autenticación
    - Inventar algo para trabajar con muchos datos
    - Entregar un docker con un set de datos para la BD
        - modelo Incompleto y darle la opción de que pueda extender el modelo si necesita ejemplo autenticación
    - Hacerlo elegir entre opciones
        - ej: base de datos
        
    - 
    
- Que evaluar ?
    - calidad de codigo
    - Logica
    - Como piensa
    - Que funcione
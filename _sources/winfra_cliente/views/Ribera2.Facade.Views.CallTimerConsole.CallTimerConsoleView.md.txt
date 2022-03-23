
# Seguimiento de las conexiones

## Conexiones locales

Muestra en tiempo real el trafico de datos entre el cliente y servidor.
El ultimo comando ejecutado aparece como primero en la lista.

Los datos presentados en la pantalla:

 * **Id** - identificador del hilo (ThreadId) que esta ejecutando la petición.
El id agrupa los comandos que se están ejecutando en la misma operación.
El sistema automáticamente reutiliza los hilos, así que varias operaciones pueden
acabar con el mismo id.
 * **Comando** - nombre completo de comando ejecutado
 * **Tamaño** - tamaño de la respuesta. Esta en Bytes si no se indica nada o KB o MB si esta indicado junto con el valor
 * **Petición** - tiempo de comprimir la petición y subirla al servidor.
 * **Procesamiento en servidor** - tiempo que tarda la aplicación de Winfra3 en el servidor procesar la petición y preparar
la respuesta.

El tiempo incluye: descomprimir los datos (unzip), decodificar los datos transmitidos (json decode), ejecutar el comando,
consultar la base de datos y gestionar la transacción (SQL), generar la respuesta (DTOs), codificar los datos para la transmisión
(json encode), comprimir los datos (zip)

El tiempo no incluye creación de la respuesta en wsgi app (flask) y procesamiento en servidor web (apache) ej. cifrar en las conexiones HTTPS.

 * **Procesamiento local y descarga** - tiempo que tarda en recibir la respuesta, descifrar y descomprimirla en el cliente.
 * **Tiempo total** - total del tiempo que tarda el comando sumando petición, servidor y descarga.
 * **Error** - muestra si ha ocurrido un error en la conexión. Solo aparecen los errores que Winfra detecta y automáticamente
re-intenta la comunicación (estados http ConnectFailure, ConnectionClosed, KeepAliveFailure)

```{note}
No esta incluido en los tiempos la codificación/decodificación de los datos (json encode/decode) en el cliente y la actualización de la pantalla.
```
En caso de listados y cuadriculas con muchos registros puede ser significante, pero depende solamente del rendimiento del ordenador del cliente.

## Actividad de servidor

Muestra el gráfico de peticiones servidas por el servidor para todos los usuarios (no tiene en cuenta las tareas como informes etc.).

Cada barra vertical representa el numero de peticiones realizadas en un minuto. Todas las barras representas últimos 60 minutos de actividad.

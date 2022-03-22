title: Ribera2.Printing.Views.PrintServiceConfigView.md
=== Configuración del servicio de impresión

Permite configurar el servicio de impresión - enlace entre las colas de winfra y las colas de windows instaladas en la maquina.

La configuración permite configurar múltiples colas de winfra con una o varias colas de windows.
La cola de winfra solo puede aparecer una vez.

== Configuración de servicio

 * **Habilitar impresión** - indica si la impresión esta habilitada. Sirve para poder parar la impresión del servicio por completo.
 * **Intervalo** - intervalo en segundos entre las comprobaciones de la cola.

 !! El servicio comprueba si hay nuevos documentos en la cola de winfra según el intervalo indicado.
Por lo tanto, el intervalo es el máximo tiempo entre agregar un nuevo documento a la cola y el inicio de la impresión.
Si el tiempo es demasiado corto (menor que 15 segundos) puede sobrecargar el equipo de servidor.

== Inicio de sesión automático

Permite configurar un usuario y contraseña para iniciar la sesión automáticamente después de lanzar la aplicación.
Si el inicio no esta configurado hay que logearse para poder imprimir.

 !! Para el inicio automático hay que utilizar usuario solo con la rol **Impresora** para evitar acceso a otras partes de la aplicación.

== Colas de impresión

Añade la configuración de la cola de winfra y su correspondiente cola de windows o puerto de serie.

 * **Cola de impresión** - cola de winfra desde cual se va a imprimir
 * **Tipo de proceso** - indica el tipo de impresión que se va a utilizar. El valor por defecto es **Cola de windows**.

Utiliza la opción **Cola de windows** si la impresora esta configurada en los *Dispositivos e impresoras* como una cola de windows.
Esto se aplica a todas las impresoras conectadas por USB, con impresión por IP o las impresoras conectadas a otros equipos
y compartidas a través de la red.

La opción de **Puerto de serie** se utiliza para impresoras conectadas directamente a los puertos de serie.
Esto es aplicable a algunas antiguas impresoras matriciales.

La opción de **Export a Excel** (opcionalmente sin formato) permite definir una carpeta a la que exportar automáticamente
los documentos agregados a la cola. No hay que indicar la impresora, papel etc.

 ! Si el documento (o informe) incluye un nombre de fichero se va crear con el mismo nombre indicado y con las subcarpetas si se han indicado.
Si el documento ya existe lo sobrescribe.

 ! Si el documento no tiene el nombre de fichero se utilizara la descripción del documento y si el nombre ya existe se añade
un contador.

 * **Impresora** - nombre de la impresora - utiliza el dialogo de selección de impresora para elegir el nombre.
 Si el tipo de proceso es **Puerto de serie** escriba el nombre y numero de puerto ej.: **LTP1** o **COM1**.

 * **Configuración genérica** - utiliza la configuración genérica (por defecto) de la impresora de windows en lugar
de utilizar la configuración del usuario desde *Dispositivos e impresoras*.

 * **Tamaño de papel** - indica el tamaño de papel utilizado por la impresora. El dato es opcional, si no se indica, la impresora
utiliza el papel por defecto.
La opción tiene uso para papeles de tamaños personalizados para impresoras matriciales o para impresión de etiquetas etc.

 * **Copias en blanco y negro** - indica si las copias de los documentos se deben imprimir en una escala de grises.
El documento original se imprime en color. Esto es aplicable a los documentos de venta.

**Color** - valor por defecto, imprime las copias en color

**EscalaGrises** - imprime las copias a escala de grises. No cambia el modo de impresión de la propia impresora, modifica
el documento y convierte las paginas correspondientes a las copias a escala de grises.

**EscalaGrises_SepararPaginas** - imprimir las copias a escala de grises. Separa las paginas en documentos individuales.

**EscalaGrises_Ticket** - imprime las copias a escala de grises. Imprime en un documento único pero genera el ticket de impresión para cada página.

 !! La mejor opción para imprimir en escala de grises es **EscalaGrises_Ticket**. Si no funciona prueba con **EscalaGrises_SepararPaginas** pero suele
ser mucho mas lenta. La **EscalaGrises** es rápida pero no garantiza que se va a utilizar solo tóner negro.


 * **Ruta raíz para los procesos de exportación** indica la ruta raíz para la exportación, ej.: C:\export\
La opción solo es válida para los tipos de proceso **Export a Excel**


 * **Código inicialización puerto serie** indica una secuencia de bytes que se añade delante de cada documento enviado a
puerto de serie. Escribe el valor en el formato hexadecimal de los bytes, ejemplo **1DFF04**.
Esto se utiliza para configurar la impresora matricial con un tamaño de letra, modo de impresión (draft) etc.
El código depende del modelo de la impresora

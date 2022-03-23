
# Configuración de los perfiles de impresión de venta

La pantalla permite definir perfiles de impresión para los documentos de venta.
Cada perfil representa un conjunto de colas de impresión y diseños de los documentos que se utilizan en un contexto.
Ej.: impresión de los documentos para repartidores, envío por correo electrónico,
pre-visualización de los documentos en la pantalla etc.

Dentro de cada perfil aplicamos una serie de filtros para distinguir como se va a imprimir cada documento.

## Campos de filtros
 * **Tipo** - filtra por tipo de documento. El tipo indicado agrupa varios tipos del documento para simplificar
la configuración ej. Albaranes, Pedidos, Facturas etc. y además distingue otras propiedades ej.
Albarán de intermediación, Albarán no valorado etc. El tipo es obligatorio y solo se puede repetir si hay otro filtro definido.
 * **Proveedor** - filtra el proveedor de intermediación. Si no se indica el proveedor, la definición se aplicara a todos.
Esto permite definir una impresora, papel o diseño especifico para un proveedor. Ej.: diseño con logos de proveedor.
El campo solo es aplicable al tipo de albarán de intermediación.
 * **Serie** - filtra los documentos por la serie.
 * **Tipo facturación** - filtra los documentos por tipo de facturación

## Campos de definición de la impresión
 * **Cola de impresión** - nombre de la cola de winfra3 en la que se van a enviar los documentos.
 * **Diseño** - nombre de diseño que se va a utilizar para imprimir el documento
 * **Desglose de los albaranes** - indica como se van a desglosar los albaranes en la impresión de las facturas
 * **Impresión línea caja promoción** - indica como hay que imprimir la caja de regalo y/o información de la línea.
Si no se indica ningún valor se utiliza la configuración por defecto de los datos generales.
 * **Agrupar regalo** - Indica si hay que agrupar las lineas de regalo al final de documento. Solo tiene efecto si se imprime Cargo y Regalo o Entrega y Regalo.
 * **Grupo regalo** - Indica el nombre de cabecera de grupo de regalos si esta marcado Agrupar regalo. Ej. 'Productos regalados'
 * **Agrupar clave abono** - Indica si hay que agrupar las lineas de abono al final de documento según la clave de abono.
 * **Marca de agua** - permite indicar un texto que aparece como marca de agua en la impresión de los documentos.
Puede indicar varios textos separados por **;** (punto-coma) para indicar el texto en la primera, segunda, tercera etc. impresión.
Marca de agua solo se aplica si el número de copias es mayor que 1.

Ejemplo:

copias: 2, marca: "COPIA", imprime 2 documentos, primero sin marca y segundo con "COPIA"

copias: 2, marca: "ORIGINAL;COPIA", imprime 2 documentos, primero con "ORIGINAL" y segundo con "COPIA"

 * **Número de copias** - indica el número de veces que se va imprimir el documento.
 * **Intercalación** - indica el orden en el que se imprimen las copias de los documentos.
Si la intercalación es **Sí** se imprime todo el documento original y a continuación la copia.
Si la intercalación es **No** se imprime la pagina 1 del original, luego página 1 de la copia. A continuación página 2 del
original y página 2 de la copia etc.
 * **Tamaño de lote** - para optimizar la impresión de gran cantidad de documentos es posible juntar los documentos en lotes
y enviar así a la impresora múltiples documentos como un trabajo de impresión.
El tamaño adecuado puede variar entre 50 y 200 documentos y depende de la impresora utilizada.
Para los envíos por correo electrónico el tamaño de lote tiene que ser 1.
 * **Lote en doble cara** - indicar si el documento si la impresora va imprimir en doble cara.
Si esta marcado **Sí** rellenamos el lote de documentos con paginas vacías para evitar imprimir diferentes documentos en la misma hoja.

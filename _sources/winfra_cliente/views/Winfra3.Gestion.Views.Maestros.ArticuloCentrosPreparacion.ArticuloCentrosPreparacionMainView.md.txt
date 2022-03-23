
# Centros de preparación

Define los centros para identificar los procesos de preparación de carga de los artículos.

## Procesos

 * **Contar** - proceso por defecto. Indica que después de preparar la carga hay que contar
la cantidad total de la hoja de carga
 * **Empaquetar** - proceso para preparar las cajas de mercancía individualmente para los clientes.
Permite impresión de la etiquetas.
 * **Pesar** - proceso para preparar cada pieza individualmente para los clientes para poder indicar el peso.
 Permite impresión de las etiquetas con peso.

Para los procesos de **Empaquetar** y **Pesar** es importante indicar el tamaño de la caja y la opción
de preparar cajas por cliente.

 * **Tamaño de la caja** - indica el tamaño máximo de la caja. Pedidos de mayor tamaño se separarán en
múltiples cajas.
 * **Cajas por cliente** - indica si hay que separar las cajas por cada cliente. Si es negativo el winfra intenta
combinar los pedidos en cajas para no llevar las cajas casi vacías, pero a la vez para que el repartidor
no tenga que abrir demasiadas cajas en la entrega.

Ejemplos de la configuración (cajas por cliente, tamaño de la caja):

```
No cajas por cliente, tamaño 6
```

Prepara botellas en cajas de 6 optimizando el reparto. El repartidor tendrá que abrir las cajas y sacar las botellas
correspondientes.

```
No cajas por cliente, tamaño 999
```

Prepara todos los azucarillos etc. en una caja, repartidor coge lo que necesita según el albarán.

```
Sí cajas por cliente, tamaño 999
```

Prepara una bolsa sin limite del tamaño con toda la mercancía para un cliente.

## Impresoras

Si utiliza el almacén mecanizado (tablets) indica las impresoras en las que imprimir las hojas y las etiquetas.

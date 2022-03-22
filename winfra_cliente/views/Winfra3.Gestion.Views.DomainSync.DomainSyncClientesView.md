title: Winfra3.Gestion.Views.DomainSync.DomainSyncClientesView.md
=== Actualizar clientes entre dominios

La pantalla permite enlazar, copiar y crear nuevos cliente entre dos dominios.

La operativa depende como esta configurada la conexión entre los dominios.
El parámetro **Actualizar clientes** de la configuración.
El dominio que permite actualizar clientes trae los clientes del dominio conectado y los enlaza o crea clientes en local.

== Operaciones Actualizar clientes = Sí

**Enlazar cliente** - enlaza el cliente externo con el cliente para enlazar.
El cliente para enlazar esta preseleccionado basándose en identificación fiscal, numero de referencia de proveedor o parecido del nombre.
La columna de coincidencia indica la fiabilidad de la selección automática.

**Desenlazar cliente** - elimina el enlace

**Actualizar clientes** - para todos los clientes enlazados copia los datos del dominio remoto al local. Datos incluyen nombre, las direcciones, punto de venta etc.
Esta operación no es necesaria pero permite mantener los clientes actualizados.

**Crear clientes** - crea un nuevo cliente local desde el cliente remoto y lo enlaza.

**Crear condiciones** - crea una nueva condición para el proveedor indicado en la configuración.
Las condiciones se crean automáticamente al crear o enlazar el cliente.
Esta operación es útil si añadimos segunda configuración y los clientes ya estan creados/enlazados.

== Operaciones Actualizar clientes = No

El dominio sirve como origen de los clientes - nunca los actualizamos aquí.

**Copiar enlaces** - copia los enlaces creados en el dominio remoto al dominio local. Esta operación se hace automáticamente al sincronizar la venta.
Esto es útil para comprobar la configuración y diagnostico. No tiene uso una vez puesto en marcha.

**Crear condiciones todos** - crear las condiciones de venta del proveedor configurado para todos los clientes (no solo enlazados).
La operación se utiliza en la venta externa o intermediación. El dominio que es el origen de venta es a la vez origen de los clientes.
Pero cliente necesitan la condición de venta para el proveedor que esta configurado en la conexión para crear la venta de intermediación.

Esta operación genera las condiciones para todos los clientes que
 * estan de alta
 * tengan punto de venta
 * punto de venta esta de alta
 * no tienen la condición del proveedor ya creada y activa (según las fecha de inicio y fin)

Al dar de alta un nuevo cliente, es posible crear la condición de venta manualmente o volver o ejecutar esta operación.

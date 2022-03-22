title: Winfra3.Gestion.Views.VentaMobile.MobileUserDetailView.md
=== Configuración del usuario móvil

Permite configurar el usuario para la aplicación de ventas en los dispositivos móviles

== Campos
 * **Personal** - indica el personal relacionado - vendedor o repartidor
 * **Nombre** - nombre o descripción tal como aparece en el dispositivo móvil
 * **Tipo** - el tipo de operativa del dispositivo
 * **Clave** - indica la clave personal de usuario. Hay que indicar la clave en los ajustes del venta móvil
(en el telefono/tablet) para poder cargar este usuario.
 * **BloquearConfiguracion** - Bloquea el acceso al Configuración y Herramientas en las pdas.
 * **Cargar todas las rutas** - Solo aplicable a tipo **Venta**.
 La carga incluye todas las rutas de venta definidas en la empresa. La opción sirve para inspectores o vendedores de apoyo.
 * **Baja** - no se preparan cargas para usuarios dados de baja
 * **Rutas de reparto** - Solo aplicable a tipo **Venta**.
 Indica las rutas de reparto relacionadas con el vendedor.

== Tipos de operativa
 * **Venta** - la carga preparada incluye todas las rutas de venta donde el usuario esta como responsable.
 Los pedidos descargados se incorporan como nuevos documentos.
 * **Reparto** - la carga preparada incluye los viajes finalizados del repartidor, los clientes y documentos incluidos
 en los viajes. Los documentos descargados se actualizan al incorporar en el caso de las modificaciones.
 Se genera una liquidación para el viaje.
 * **Autoventa** - la carga preparada incluye todas las rutas de venta donde el usuario esta como responsable.
Los documentos descargados se incorporan como nuevos documentos. Se genera una hoja de carga y una liquidación.

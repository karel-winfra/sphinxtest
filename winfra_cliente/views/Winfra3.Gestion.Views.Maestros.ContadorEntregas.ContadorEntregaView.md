title: Winfra3.Gestion.Views.Maestros.ContadorEntregas.ContadorEntregaView.md
=== Contadores de entregas

Define un contador para acumular la venta realizada al cliente.
Cada contador suma las caja de cargo y de regalo por separado.
Contador permite definir el regalo máximo o en relación con cargo para avisar en la linea de venta y en la ficha de la pda.

Los contadores están definidos por cliente.

== Configuración del contador
 * **Activo** - Indica si el contador esta activo (acumula los cargos y regalos).
 !! La búsqueda por defecto solo muestra los contadores activos. Utiliza parámetro **b:** para ver todos los contadores

 * **Desde** - activo desde la fecha
 * **Hasta** - activo hasta la fecha (inclusivo). Las ventas fuera de las fechas no acumulan en el contador
 * **Artículo formato** - se acumulan las ventas del artículo formato indicado
 * **Artículo consumo** - se acumulan las ventas de todos los artículos formato relacionados con el artículo consumo.
 !! La cantidad acumulada del artículo consumo es la cantidad de entrega multiplicada por la equivalencia de artículo formato vendido. Hay que indicar el cargo y regalo teniendo en cuenta la equivalencia.
 * **Artículo agrupación - se acumulan las ventas de artículos de formato incluidos en la agrupación
 * **Cargo** - Indica el cargo mínimo para aplicar el regalo. Si el cargo es **0** la cantidad de regalo es disponible solo una vez.
Si el cargo es mayor que **0**, la cantidad de regalo es disponible cada vez que se acumula la venta igual a cargo.
 * **Regalo** - Indica la cantidad para regalar.
 * **Campaña** - Indica una campaña de tipo **Promoción** o **Regalo**. Solo se acumulan los regalos si son de la campaña indicada.
La campaña es opcional.
 * **Descripción** - nombre del contador que aparece en el aviso. La descripción es opcional.
 * **Cargo acumulado** - la cantidad total de cargo incluida en el contador
 * **Regalo acumulado** - la cantidad total de regalo incluida en el contador

== Aviso en la linea de venta

En caso de cargo igual a **0** el aviso indica la cantidad de regalo que queda por entregar.
 ! regalo disponible = regalo - regalo acumulado

En caso de cargo mayor que **0** el aviso indica la cantidad de cargo para el siguiente regalo y la cantidad de regalo ya disponible.
 ! regalo aplicable = redondear_abajo(cargo acumulado / cargo) * regalo
 ! regalo disponible = regalo aplicable - regalo acumulado

== Contador aplicable

Winfra selecciona el contador filtrando el cliente y la fecha de documento. Solo selecciona los contadores activos.

A continuación busca por artículo formato, por artículo consumo y por la agrupación en este orden.

Si dos contadores tienen el mismo artículo seleccionamos la fecha desde posterior.

title: Winfra3.Gestion.Views.Maestros.Fabricantes.FabricanteDetailsView.md
=== Fabricante

== Campos que inciden en el cálculo del precio medio ponderado

 * **Días para cálculo PMP** indica el número de días atrás que utilizaremos para obtener las compras
 con las que calcular el precio medio (si existe un inventario con precio en el intervalo utilizamos la fecha
 del inventario como fecha desde). Si se deja a cero obtendremos el precio de la última compra del artículo.

    * Ejemplo:

        Días = 60 => obtendremos las compras del artículo 60 días atrás para obtener la media (si hoy fuera 20 de Enero de 2019 obtenemos las compras desde 60 días atrás -22 de Noviembre de 2018-). Si hubiera un inventario valorado en medio utilizamos su fecha (Fecha inventario = 31 de Diciembre de 2018; obtenemos las compras desde esta fecha).

 * **Límite días para cálculo PMP**. Este campo opera siempre que el campo Días se haya dejado a cero. En este caso obtenemos la última compra y el campo establece hasta cuantos días atrás es válida la fecha de esa última compra.

    * Ejemplo:

        Límite = 60 => si hoy fuera 20 de Enero de 2019 y la última compra es posterior al 22 de Noviembre de 2018 utilizamos el precio de esa compra. Por contra si la última compra fuera anterior la descartamos y buscamos el precio de la condición de compra.

 * **Forzar cálculo PMP sobre condición de compra** indica que si valoramos a coste condición o a coste inventario utilizaremos el precio neto de la última condición de compra del artículo aunque esté caducada.

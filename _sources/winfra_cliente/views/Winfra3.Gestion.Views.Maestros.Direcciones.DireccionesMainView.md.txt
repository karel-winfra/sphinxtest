title: Winfra3.Gestion.Views.Maestros.Direcciones.DireccionesMainView.md
=== Gestión de las direcciones

Pantalla de utilidades que permite búsqueda, localización y actualización de las direcciones.

== Operaciones

 * **Geolocalizar** utiliza los servicios de Google Maps para validar las direcciones seleccionadas
y buscar sus coordenadas geográficas.
 * **Actualizar** la dirección. Una vez la dirección ha sido geolocalizada la operacion actualiza la calle,
numero y código postal tal como lo ha localizado Google Maps.

== Datos de las direcciones

 * **Enlace** muestra de quien es la dirección. Las primeras letras indican el tipo: P - proveedor, A - acreedor,
PV - punto de venta, IF - identificación fiscal
 * **Coordenadas** indican las coordenadas geográficas: Latitud y longitud. El vínculo abre Google Maps en el navegador.
 * **Dirección localizada** es la descripción de la dirección tal como se ha podido encontrar en el mapa.
Al **actualizar** la dirección estos datos se van a copiar a los campos Vía, Numero y Código postal.
 * **Tipo dirección localizada** indica el tipo de dirección que se ha podido localizar. Si la dirección es correcta
el tipo de dirección es **street_address**. Si solo se encuentra el pueblo la dirección es **locality** etc.
Puede filtrar y ordenar los tipos de localización. La lista de tipos esta a continuación.

== Tipos de localización y componentes de las direcciones

Esto es la lista de tipos desde la documentación de Google Maps.

El geocodificador admite y devuelve los siguientes tipos en las matrices de tipo de dirección y tipo de componente de dirección:

 * **street_address** indica una dirección exacta.
 * **route** indica la denominación de una carretera (como "US 101").
 * **intersection** indica una intersección principal, generalmente de dos calles importantes.
 * **political** indica una entidad política. Generalmente, este tipo indica un polígono de alguna administración pública.
 * **country** indica la entidad política nacional, y es generalmente el tipo de orden más alto que devuelve el geocodificador.
 * **administrative_area_level_1** indica una entidad civil de primer orden por debajo del nivel de país. En Estados Unidos, estos niveles administrativos son los estados. No todos los países poseen estos niveles administrativos. En la mayoría de los casos, los nombres cortos de administrative_area_level_1 coincidirán considerablemente con las subdivisiones de ISO 3166-2 y otras listas conocidas; sin embargo, no podemos garantizarlo debido a que nuestros resultados de geocodificación están basados en diferentes señales y datos de ubicación.
 * **administrative_area_level_2** indica una entidad civil de segundo orden por debajo del nivel de país. En Estados Unidos, estos niveles administrativos son los condados. No todos los países poseen estos niveles administrativos.
 * **administrative_area_level_3** indica una entidad civil de tercer orden por debajo del nivel de país. Este tipo indica una división civil inferior. No todos los países poseen estos niveles administrativos.
 * **administrative_area_level_4** indica una entidad civil de cuarto orden por debajo del nivel de país. Este tipo indica una división civil inferior. No todos los países poseen estos niveles administrativos.
 * **administrative_area_level_5** indica una entidad civil de quinto orden por debajo del nivel de país. Este tipo indica una división civil inferior. No todos los países poseen estos niveles administrativos.
 * **colloquial_area** indica un nombre alternativo de uso frecuente para la entidad.
 * **locality** indica una entidad política constituida de una ciudad o un pueblo.
 * **ward** indica un tipo específico de localidad japonesa para facilitar la distinción entre los múltiples componentes de localidad en una dirección japonesa.
 * **sublocality** indica una entidad civil de primer orden por debajo de una localidad. Algunas ubicaciones pueden recibir uno de los tipos adicionales: sublocality_level_1 a sublocality_level_5. Cada nivel de sublocalidad es una entidad civil. Los números más altos indican un área geográfica más pequeña.
 * **neighborhood** indica un barrio determinado.
 * **premise** indica una ubicación determinada, generalmente un edificio o un conjunto de edificios con un nombre en común.
 * **subpremise** indica una entidad de primer orden por debajo de una ubicación determinada; generalmente un edificio en particular en un conjunto de edificios con un nombre en común.
 * **postal_code** indica un código postal tal como se usa para identificar una dirección de correo postal dentro del país.
 * **natural_feature** indica una atracción natural destacada.
 * **airport** indica un aeropuerto.
 * **park** indica un parque determinado.
 * **point_of_interest** indica un punto de interés determinado. Generalmente, estos "PI" son entidades locales destacadas que no pueden incluirse fácilmente en otra categoría, como el edificio "Empire State" o la "Estatua de la libertad".

Una lista vacía de tipos indica que no hay tipos conocidos para el componente de dirección específico, por ejemplo, Lieu-dit en Francia.

Además de lo dicho antes, los componentes de dirección pueden incluir los siguientes tipos.

 ! Nota: Esta lista no está completa y está sujeta a cambio.

 * **floor** indica el piso en la dirección de un edificio.
 * **establishment** generalmente indica un lugar que aún ha sido categorizado.
 * **point_of_interest** indica un punto de interés determinado.
 * **parking** indica un área de estacionamiento o una estructura de estacionamiento.
 * **post_box** indica una casilla de correo específica.
 * **postal_town** indica un conjunto de áreas geográficas, como locality y sublocality, utilizadas para las direcciones postales en algunos países.
 * **room** indica una sala en la dirección de un edificio.
 * **street_number** indica el número exacto de una calle.
 * **bus_station**, **train_station** y **transit_station** indican la ubicación de una parada de autobús, tren o transporte público respectivamente.

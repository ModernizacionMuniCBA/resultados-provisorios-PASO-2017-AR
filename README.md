# Resultados provisorios PASO 2017 Argentina

En línea con nuestra política de contribuir con datos reutilizables para el ecosistema (analistas, periodistas, investigadores, etc) local de datos dejamos aquí herramientas para simplificar el uso de este recurso.

## Base de datos original

El Ministerio del Interior deja disponibles los resultados del escrutinio provisorio en su sitio: http://resultados.gob.ar/inicio.htm.  

Allí esta disponible una aplicación de consulta local de resultados en la opción _ Aplicación de consulta de resultados por mesa, Elecciones Argentinas del 13 de agosto de 2017_. Esta aplicación (que incluye la base de datos puede descargarse desde [aquí](http://resultados.gob.ar/cdmesas/App_Consulta_Mesas-Argentina.zip)).  

La base de datos esta en formato _Microsoft Access_. Como no es una herramienta de uso común describimos aquí el proceso y dejamos disponible en nuestro portal de datos una versión simplificada de los datos para Ciudad de Córdoba.  

## Proceso de extración de datos

El entorno usado es sobre el sistema Operativo Ubuntu.

## Pasar a CSV las tablas

Tener en cuenta que la lista de _Ámbitos_ (secciones electorales o departalentos) y las listas participantes est án disponibles en tablas separadas: [Ámbitos](csv/NomAmbitos.csv)] - [Listas](csv/NomPartidos.csv)

En primer lugar podemos extraer las tablas desde Access a CSV con la herrmaienta _mdbtools_

```
apt-get install mdbtools
```

Luego extraemos de la mase de datos todos las tablas a CSV

```
mkdir csv

for i in $( mdb-tables PR_ARGENTINA2017.mdb )
do 
    echo "EXPORTING $i ... " 
    mdb-export PR_ARGENTINA2017.mdb $i > csv/$i.csv
done
```

Tomar los resultados generales y extraer los de la **Provincia de Córdoba**.  

```
head -1 csv/MesasSublemaDNacionales.csv > datos/MesasSublemasCordobaProvincia.csv
cat csv/MesasSublemaDNacionales.csv | grep "\"04\"\,\"0" >> datos/MesasSublemasCordobaProvincia.csv
```

[Ver datos de la Provicia de Córdoba](datos/MesasSublemasCordobaProvincia.csv)

Tomar los resultados generales y extraer los de la **Ciudad de Córdoba**.  

```
head -1 csv/MesasSublemaDNacionales.csv > datos/MesasSublemasCordobaCiudad.csv
cat csv/MesasSublemaDNacionales.csv | grep "\"04\"\,\"001" >> datos/MesasSublemasCordobaCiudad.csv
```

[Ver datos de la Ciudad de Córdoba](datos/MesasSublemasCordobaCiudad.csv)

Luego del ordanamiento de los datos estos quedaron disponibles en nuestro portal de Gobierno Abierto: [VER EN EL PORTAL](https://gobiernoabierto.cordoba.gob.ar/data/datos-abiertos/categoria/sociedad/elecciones-a-diputados-nacionales-en-cordoba/223).  


### Análisis por Circuitos electorales

Los circuitos electorales en general son ciudades de la Provincia de Córdoba.
El análisis de los circuitos sigue [aquí](por-circuitos.md)

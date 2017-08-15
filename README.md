# Resultados provisorios PASO 2017 Argentina

En línea con nuestra política de contribuir con datos reutilizables para el ecosistema (analistas, periodistas, investigadores, etc) local de datos dejamos aquí herramientas para simplificar el uso de este recurso.

## Base de datos original

El Ministerio del Interior deja disponibles los resultados del escrutinio provisorio en su sitio: http://resultados.gob.ar/inicio.htm.  

Allí esta disponible una aplicación de consulta local de resultados en la opción _ Aplicación de consulta de resultados por mesa, Elecciones Argentinas del 13 de agosto de 2017_. Esta aplicación (que incluye la base de datos puede descargarse desde [aquí](http://resultados.gob.ar/cdmesas/App_Consulta_Mesas-Argentina.zip)).  

La base de datos esta en formato _Microsoft Access_. Como no es una herramienta de uso común describimos aquí el proceso y dejamos disponible en nuestro portal de datos una versión simplificada de los datos para Ciudad de Córdoba.  

## Proceso de extración de datos

El entorno usado es sobre el sistema Operativo Ubuntu.

## Pasar a CSV las tablas

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


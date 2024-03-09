# My Habi's Ssr Dev test 🤖🏠

<hr>

## Introducción

Este repositorio tiene como objetivo entregar los resultados de las pruebas 
de desarrollo requeridas para continuar en el proceso de selección para el
cargo de Ssr backend developer en Habi. En su contenido, se encontrarán las
soluciones de ambos ejercicios planteados en el documento de prueba y 
organzados de la forma más orgánica posible para asemejar el posible 
repositorio de un proyecto real y común.

## Tecnologías y recursos

Para el desarrollo del ejercicio 1, para el desarrollo de microservicios se
utilizarán las siguientes tecnologías:

* *Python v3.9.6:* Se escogió esta versión de Python para garantizar estabilidad
y mantenimiento a mediano/largo plazo para este desarrollo. Por el lado de Python,
este lenguaje es mandatorio para el desarrollo de esta prueba.

* *MySQL Server:* Engine de base de datos, mandatorio también para el desarrollo de
esta prueba.

* *mysq-connector-python v8.3.0:* Para el uso correcto de MySQL Server debemos usar
el conector nativo de MySQL para usar con Python.

* *dotenv.load_dotenv*: Este recurso built-in se utilizará para manejar las variables
de entorno del proyecto.

* *http.server:* Usaremos el módulo server de la librería built-in http para realizar
la configuración de un servidor que pueda recibir peticiones GET y POST para el
desarrollo de este ejercicio.

* *socket-server:* Usaremos este recurso para inicializar la ejecución de microservios
en este proyecto.

* *json:* Esta librería de Python la usaremos para manejar el request body a recibir
que contendrá (o no, si no se desea usar) los valores a filtrar en la base de datos.

## Dudas o stoppers encontrados y resueltos durante el desarrollo

Durante el desarrollo de este ejercicio se presentaron algunas dudas y circunstancias
que fueron resueltas durante el mismo lapso de desarrollo de la prueba, las situaciones
presentadas y sus respectivas soluciones fueron las siguientes:

* ¿Como realizar pruebas unitarias para una implementación bajo http.server?
  * **Respuesta:** Dado que llevaba buen tiempo sin hacer una implementación de APIs sin 
  soporte de frameworks (debido a que me he especializado en usar Django o FastAPI) 
  me encontré en la situación de no saber si priorizar pruebas mockeando server para
  dicho acometido o si aislar el componente lógico del método para realizar las pruebas
  unitarias. Entonces, se decide implementar un servidor de pruebas por medio de threading 
  para poder realizar las pruebas de forma aislada a una ejecución normal del servidor.
  Además, se hacen 3 casos de prueba sencillos acorde al ejercicio realizado, todo con 
  pytest y a nivel de testear el endpoint bajo un servidor fixture.
  
* ¿Talvez hacer mas sencillo el uso de variables de entorno?
  * **Respuesta:** Al trabajar con data sensible como una base de datos lo ideal siempre
  será ocultar esta información sensible e implementarla por medio de variables de entorno,
  pero para facilitar la labor de tener que guardarlas en un sistema por medio de la 
  terminal (cosa que dependiendo del usuario puede ser complicado) he decidido implementar
  la librería "dotenv" de python para simplemente almacenar dichas variables en un
  archivo .env que quedará en la raíz del proyecto y donde de forma sencilla cualquier
  usuario colocará las variables de entorno requeridas para la conexión a base de datos
  que requiere este proyecto.

* ¿Como garantizar la funcionalidad de filtros dinámicos en una consulta SQL sin ORM y 
cuidando la integridad de los tipos de datos de dichos filtros?
  * **Respuesta:** Plantié en app/habi_properties_query/utils/queries.py un método con el
  cual el request body que el usuario enviará, será convertido en una secuencia de strings
  concatenados (siempre y cuando se hayan indicado esos campos o se les haya dado valor) 
  y que cumplan las condiciones necesarias para ser insertadas como una clausula WHERE
  en la consulta a realizar. Además, la data, tipo de dato y nombres de campos se 
  colocaron a modo de placeholders para darle más seguridad a la consulta y sobretodo
  cuidar los tipos de datos e información a mandar a la consulta.

* ¿La consulta deseada como se hizo?
  * **Respuesta:** Duré varios minutos planteando como hacer esta query para que no solo
  diera el resultado esperado sino que también fuera lo más optimo posible. Teniendo en 
  cuenta que tenía que partir desde una tabla y hacer JOIN con las otras dos para poder
  filtrar como se deseaba, decidí hacer una consulta adicional para acotar la información
  de los estados más recientes por tabla y esa subconsulta la agregué como un JOIN adicional
  para reducir de una vez y antes de llegar a la clausula WERE todos los estados de propieddes
  que fueran los más recientes por cada propiedad. Esto se hace generando la consulta y agrupando
  los id_propiedad por el máximo valor existente de fecha de actualización de la tabla de 
  historial de estados. Comparando con otras dos versiones más de esta consulta, la implementada
  fue por segundos más eficiente.

* Había data inconsistente en la tabla de propiedades ¿Como se descartó?
  * **Respuesta:** Siguiendo las pautas del modelo de negocio de Habi, propiedades con información
  nula o vacía de precios de venta es redundante porque para Habi no hay interés en mostrar
  inmuebles con "precio en cero" por descarte no traerían beneficio sino inclusive inconvenientes
  con los clientes. Por ende, se agregó internamente un filtro permanente para garantizar que siempre
  venga información con precios reales, que es lo que le importa tanto a Habi como al cliente.

## Instrucciones de uso e instalación

Por favor seguir las indicaciones de uso de este servicio para garantizar su correcto funcionamiento:

1. Posicionate en la carpeta donde deseas clonar el repositorio.
2. Clona el repositorio: https://github.com/el-richi-97/MyHabiTest.git
3. Accede al interior de la carpeta que obtienes al clonar el repositorio, para esto puedes
usar el comando: `cd <nombre_carpeta>`
4. Necesitas crear un entorno virtual. Con virtualenv puedes hacerlo así: `python -m venv mi-entorno`
5. Luego de creado el entorno virtual puedes entrar así: `source mi-entorno/bin/activate`
6. En bien el entorno virtual esté creado, es requerido instalar requerimientos, se hace con 
el comando: `pip install -r requirements.txt`
7. Es necesario instanciar las variables de entorno, se puede hacer creando un archivo llamado 
".env" en la raíz del proyecto y registrar la siguiente información:

```
# DDBB env variables
HABI_SRC_HOST=3.138.156.32
HABI_SRC_PORT=3309
HABI_SRC_USER=pruebas
HABI_SRC_PSSW=VGbt3Day5R
HABI_SRC_DDBB=habi_db

# Service env variables
SERVICE_HOST=localhost
SERVICE_PORT=8000
```

8. Teniendo todo listo, la ejecución del proyecto se podrá hacer simplemente con el comando
`python main.py`
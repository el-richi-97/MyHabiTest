# My Habi Ssr Dev test 🤖🏠

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

# Gestor de Notas
Este proyecto tiene como objetivo realizar la administración de notas mediante una interfaz creada en django

## Requerimientos
- Python 
- Django

## Proceso para la realización del proyecto
1. Creación del proyecto 
- django-admin startproject project_notes

2. Creación de modelos
En el archivo de models.py se agregaran todos los modelos requeridos es importante contemplar el tipo de dato que se requiere 

3. Migración de modelos
Es importante recordar realizar la migración del modela ya que nuestros métodos dependerán de ellos y si no se encuentran en la db no reconocerá las propiedades

4. Preparar templates
Para mantener un orden es recomendable mantener una carpeta por modelo si es posible, en este caso se creo un carpeta en templates para un mejor orden.
Tambien se crean los html necesarios con un html simple para pruebas durante la creacion de los views

5. Crear views 
Es importante identificar los modelos requeridos y empezar a realizar los redireccionamiento correspondientes o renders


6. Construir la maqueta en que se visualizaran los datos

7. Implementar los casos de uso con los metodos de la vista para confirmar el funcionamiento
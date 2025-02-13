**Espero que esto sea legible**
1. Generació d'imatges

No puedo subir el modelo en sí porque pesa demasiado, aquí la idea sería partir de generador.py y adaptar el código de manera que se pueda ejecutar constantemente en el clúster HPC. Cada vez que se genera una imagen, esta debería poder verse en el display de la exposición.

3. Cercador

El script en cercador_missatges.py tiene que estar en ejecución para que la aplicación de Anvil (subo el código en otro archivo de Python) pueda utilizarse, también hay que cambiar los directorios de las carpetas, archivos, etc. Cada vez que se hace una búsqueda, la app de Anvil activa la función para realizar la búsqueda y para ejecutar el modelo de generación de texto, y la página se actualiza cuando todo se ha completado.
La idea sería tener una GUI que realice las dos funciones de manera paralela y localmente. Para la búsqueda con la API, mostrar los títulos y los links de los 10 primeros resultados y optimizar el código para evitar el error por resultados insuficientes. Los links también se guardan en una carpeta como archivos de texto para abrirse como ventanas de Chrome en otro display. Quizás se podría hacer que el texto buscado se guarde en un archivo .txt y que cada vez que este cambie se ejecute otro script con la función del modelo de generación de texto.

5. Bot IRC

El código de esta parte me lo facilitó Alan Tapscott, tal y como está configurado se conecta con un servidor de IRC y envía el contenido del
archivo privateSentenceList.txt como un mensaje cada vez que la función del generador de texto lo actualiza.

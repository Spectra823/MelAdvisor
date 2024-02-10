# MelAdvisor
MelAdvisor es una app creada por Carla Marcos Vázquez, estudiante de segundo de Bachillerato (en el año de creación de la aplicación) del Bachillerato de Excelencia de la Vaguada de la Palma, Salamanca.

Esta aplicación tiene como objetivo la clasificación de imágenes de lesiones cutáneas en dos grupos: nevus (benignos), y melanomas (malignos). En el futuro es posible que se añadan nuevas categorías y se haga un completo rework de al red neuronal utilizada (creada también por Carla para su uso exclusivo en este proyecto).

La aplicación estará disponible como APK en este Github hasta que me sea viable el cumplir con las condiciones de la Google Store. La llegada a dispositivos Apple está planeada para el futuro lejano, pero es posible que no se llegue a dar.

## Cómo funciona
MelAvisor utilizes a Convolutional Neural Network (CNN) to classify pigmented lesions in two classes (for now): nevus (benign) and melanoma (malignant). A CNN is a Deep Learning algorithm used in conjuction with a multilayer perceptron. It specializes in image recognition and classification. The algorith asigns weights to the different parts bits of the image, and then compares them to the learnt ones, being able to determine what kind of image model (images used in training) resembles more closely the one given, and then classifies it into that group.

En el futuro añadiré nuevas funciones y mejoras cuyo uso iré explicando de forma más detallada en este apartado. 
Aun así, ante cualquier duda, no duden en escribirme o dejarme un comentario, y trataré de responderles como mejor pueda.

## Guía de descarga e instalación de la APK en dispositivos Android
De momento la App sigue en fases de desarrollo tempranas, por lo que no voy a subir todavía una APK para descargar. Cuando considere que está en un estado lo suficientemente estable y avanzado para su uso general, subiré un archivo y explicaré en este apartado
descargar e instalar MelAdvisor.

## Uso
MelAdvisor ha sido ideada como una forma sencilla y rápida de checkear tus lunares ante cualquier posible incertidumbre sobre la naturaleza de estas lesiones. La deteción precoz de melanomas es crucial, ya que aumenta en gran medida las posibilidades de sorbevivir a este cancer.

La facilidad de uso de esta aplicación permite a cualquier persona, sin importar su grado de conocimiento sobre estos temas, saber con un alto porcentaje de fiabilidad ante qué tipo de lesión se encuentran.

Lo que esta app no es, y jamás será, es un sustituto para la opinión cualificada de un especialista. Si tienen serias dudas sobre una lesión, por favor contacten a un dermatólogo lo anets posible.

En serio. No arriesguen su salud porque era más sencillo tomar una foto con MelAdvisor que ir al médico a certificar de qué tipo de lesión se trata.

## Desarrollo futuro (Hoja de ruta)
### Cambios muy probables:
+Añadir base de datos local: Esto permitirá al usuario mantener un seguimiento de sus lunares, tomando múltiples fotografías de la misma lesión que se ordenarán en una línea del tiempo para mayor claridad. Se creará un archivo para cada lunar, con sus imágenes y datos relacionados. Para añadir nuevas imágenes al archivo, se deberá estipular a qué lunar pertenecen al tomarlas (pondré un botón de + o algo parecido para ahcer este proceso sencillo). Toda esta información será después representada en un apartado a aprte con un listado mostrando todos los lunares, en que se podrá filtrar por fecha, tamaño...

De esta forma, los usuarios pueden mantener un seguimiento sencillo del crecimiento y los cambios de sus lunares.

También espero poder lograr que toda esta información pueda ser exportada y enviada en un PDF, en caso de que necesiten enviársela a su médico.

Trataré de realizar todo esto en torno a una base local por tres motivos principales:

1.-Privacidad. No quiero que MelAdvisor monitoree a sus usuarios, mucho menos en algo tan sensible como es su salud. Por supuesto, en pos de mejorar el algoritmo, incluiré una opción para enviarnos fotografías con diagnóstico, para poder utilizarlas en una nueva versión de la red y mejorar el rendimiento y la fiabilidad de la aplicación. Pero esto SIEMPRE será opcional.

2.-Uso offline. Al tener toda la información almacenada en su propio dispositivo, no necesitarán de conexión alguna para acceder a ella. Quiero hacer que MelAdvisor funcione totalmente offline si es posible (excepto la función que eprmite buscar el resultado en Google por si quieren más informaciión, pero eso es algo menor). De esta manera, más gente tendrá acceso a la app sin necesidad de preocuparse por la calidad de su Internet.

3.-Costes. No cuento con los recursos necesarios para poder mantener un servidor funcionando 24/7. Sé que existen servicios que te alquilan un servidor por algo más de 2 euros al mes, pero como ya he dicho, la privacidad es una de mis principales preocuapciones, y dejar los datos de mis usuarios en manos de terceros va contra mis principios y los de MelAdvisor.

Por supuesto, esto también tiene aspectos negativos:

1.-Los datos ocuparán espacio en su dispositivo, y podría llegar a ocupar bastante si toma muchas fotos a gran calidad etc...

2.-Para que funcione, es necesario que MelAdvisor acceda al almacenamiento interno del dispositivo. Lo sé, es algo incómodo para los amantes de la privacidad como yo, pero es la mejor solución que se me ocurre para implementar estas nuevas funcionalidades, que considero cruciales. Si alguno de ustedes tuviese alguna mejor alternativa en mente, no duden en comentármela. Si les consuela, puedo asegurarles que no tengo ningún tipo de interés monetario al crear esta aplicación. Es tan solo un proyecto escolar al que he toamdo cariño y que deseo continuar en mi tiempo libre.

Además, si en cualquier momento desean eliminar sus datos, simplemente deben entrar en el almacenamiento de su dispositivo y borrar los archivos. Añadiré además botones para hacer el proceso más simple desde la propia app.

+Añadir una "Wiki": Crearé una barra inferior en que podrán acceder a algunas nuevas funcionalidades, la primera de als cuales será la Wiki. En ella, explicaré de forma breve y sencilla qué son als lesiones pigmentadas, que tipos existen y cuales puede reconocer MelAdvisor, daré consejos sobre cómo enfrentar cada tipo de lesión... Además, en cada nueva actualización después de esta crearé un pequeño apartado en la Wiki explicando las novedades y cambios, para manetenerles siempre informados.

### Lo intentaré, pero no puedo asegurar su realización:
+Análisis en directo: Que la apps sea capaz de analizar y clasificar lesiones en video, en directo. Será capaz de clasificar múltiples lesiones a la vez y que a su vez se podrá crear un nuevo archivo apra cada lesión (o añadir las nuevas imagenes a un archivo ya existente) con tan solo clickear sobre dicha pigmentación.

Resultará algo complejo de realizar, pero confío en que, con el suficiente tiempo y conocimientos, pueda realizarlo.

### Casi imposible:
+Lanzar la app para iOS: Tristemente, no poseo un Mac y, sinceramente, no creo que sea sensato comprar uno solo para programar esta aplicación en iOS. Trataría de pedir prestado su dispositivo a algunos familiares pero no creo que fuese capaz de mantener la aplicación en el estado en que me gustaría (ya que no puedo pedirles prestado su dispositivo cada vez que me surja una nueva idea o encuentre un pequeño arreglo para algo). Por lo que, demomento, MelAdvisor será exclusiva para Androird (lo siento, queridos usuarios de Apple).

Aunque, quizás haya una forma de instalar APKs en un iPhone. Trataré de investigar esto e idear otra forma de haceros llegar la app.

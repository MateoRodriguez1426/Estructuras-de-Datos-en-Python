"""
 
-Estructuras de datos
 Las estructuras de datos son un conjunto de metodos o formas que estan presente en todos los lenguajes de programacion y sirven para
 organizar, almacenar y administrar datos de una determinada forma
 
 
-Colecciones
 Asi mismo las colecciones de datos son la manera especifica que tiene cada lenguaje de programacion para organizar los datos y administrarlos
 generalmente dividiendose dependidiendo de su funcionalidad
 
-Listas
 Es uno de los cuatro tipos de colecciones que hay en python, se inicializan mediante  los corchetes = []
 A continuacion se mostraran algunos metodos y funciones que sirven para manejar y administrarlos:
"""
 
listaEjemplo = ['Hola', 'Mundo', 'aqui', 'estamos', 'programando', 'en', 'Python']
print(listaEjemplo)
print(type(listaEjemplo))
 
listaEjemplo2 = ['Hola', 'Mundo', 'aqui', 'estamos', 'programando', 'en', 'Python']
print(listaEjemplo2)
#.append: Este metodo sirve para agregar elementos a la lista, de manera general  se agrega  al final de la lista
#Ejemplo:
 
listaEjemplo.append('2022')
print(listaEjemplo)
 
#.extend: Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.
#Ejemplo:
listaEjemplo.extend('Colombia')
print(listaEjemplo)
 
#.insert: Inserta un item en una posicion previamente indicada.
#El primer argumento es el índice del ítem delante del cual se insertará,
# or lo tanto a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a a.append(x).
#Ejemplo:
listaEjemplo.insert(8,'Bogota')
print(listaEjemplo )
 
#.remove: Elimina el primer item de la lista cuyo valor sea igual al que se establece
#en caso de no haber un elemento relacionado lanzara ValueError
# #Ejemplo:
listaEjemplo.remove('Hola')
print(listaEjemplo)
 
"""
listaEjemplo.remove('z')
print(listaEjemplo)
"""
#.pop: Elimina el item que se haya especificado basado en el indice
# Si no  existe un indice eliminara y retornara el ultimo elemento de la lista
# #Ejemplo:
listaEjemplo.pop(2)
print(listaEjemplo)
 
 
#.clear: Elimina todos los elementos de la lista dejando una lista vacia
# Ejemplo:
listaEjemplo2.clear()
print(listaEjemplo2, "\n")
 
#.index: Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x.
# Lanza una excepción ValueError si no existe tal elemento.  
# Ejemplo:
print(listaEjemplo.index('C'))
 
 
#.count: Devuelve el numero de veces que se repite
# un determinado elemento en la lista  
# Ejemplo:
print(listaEjemplo.count('C'))
 
#.sort: Este metodo nos permite ordenar los elementos de la lista in situ
# Ejemplo:
listaEjemplo.sort()
print(listaEjemplo)
 
#.reverse: Este metodo invierete totdos los elementos de la lista
# Ejemplo:
listaEjemplo.reverse()
print(listaEjemplo)
 
#.copy: Retorna una copia exacta de la lista
listaEjemplo.copy()
print(listaEjemplo)
 
"""
-Usando Listas como Pilas
 A continuacion se enseña una combinacion de metodos (append, pop) que ejecutados de forma
 secuencial construyen una pila donde el ultimo elemento añadido es el primer elemento retirado
 («último en entrar, primero en salir»).  
"""
 
listaEjemplo3 = [26, 33, 42, 50, 73, 21, 65, 81, 97, 48, 54]
listaEjemplo3.append(34)
listaEjemplo3.append(76)
print(listaEjemplo3)
listaEjemplo3.pop(12)
listaEjemplo3.pop(11)
listaEjemplo3.pop(10)
 
print(listaEjemplo3)
 
 
"""
-Usando listas como colas
 Asi mismo tambien se pude usar una lista como una cola, donde el primer elemento añadido es el primer elemento retirado
 («primero en entrar, primero en salir»); aunque para lograr este cometido es necesario utilizar la libreria collections.deque
 el cual fue diseñado para añadir y quitar de ambas puntas de forma rapida.
"""
from collections import deque
listaEjemplo4 = deque(['a', 'b', 'c', 'd', 'e'])
listaEjemplo4.append('f')          
listaEjemplo4.append('g')          
listaEjemplo4.popleft()
print(listaEjemplo4)
 
 
 
"""
-Comprension de Listas = Creacion de listas
 La comprension de listas son una manera eficiente y concisa de crear listas.
 Generalmente se usa para crear nuevas listas donde sus elementos son el resultado de operaciones
 dentro de uan secuencia o iteracion,
 Ejemplo:
"""
#En este ejemplo se desarrollara una lista que se sustenta en suma de dos
 
listaEjemplo5 = []
for i in range (10):
    listaEjemplo5.append(i+2)
 
print(listaEjemplo5)
#Otra forma de escribirlo de manera mas legible puede ser
listaEmergencia = [x+2 for x in range(10)]
 
"""
El siguiente ejemplo muestra el uso de una lista vacia y que mediante el uso de for anidados y otras dos listas
se pueden realizar una serie de combinaciones
 
"""
listaEmergencia2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            listaEmergencia2.append((x, y))
 
print(listaEmergencia2)
 
"""
-Listas por comprension anidad
 La primera lista contiene dentro de si otras listas generando una matriz
 ejemplo:

"""
matriz = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
print(matriz)
#La siguiente comprensión de lista transpondrá las filas y columnas:

[[row[i] for row in matriz] for i in range(4)]
print(matriz)

#Asi mismo el metodo zip() nos puede facilitar este procedimientos de transponderacion, de la siguiente manera
list(zip(*matriz))

"""
-La instruccion del
Al igual que el metodo pop() este metodo sirve para quitar un item de una lista dependiendo del indice del valor 
que se haya especificado, aunque se difernecia del metodo pop()
principalmente por la sintaxis y por que el metodo pop retorna un valor
Ejemplo:

"""
listaEjemplo6 = [23,52,65,33,85,9,10,43,54]
del listaEjemplo6[6]
print(listaEjemplo6)
del listaEjemplo6[3:7]
print(listaEjemplo6)
del listaEjemplo6[0:]
print (listaEjemplo6)


"""
Ademas tiene la funcionalidad de eliminar toda una lista con la instruccion
del listaEjemplo6
"""

"""
-Las Tuplas y secuencias 
Las tuplas son uno de los cuatro tipos de datos de python junto con listas, diccionarios y conjuntos,
así mismo su función consiste en el almacenamiento de varios artículos en una sola variable.
Entre las características principales de las tuplas, se encuentran:
ORDENAMIENTO 
INDEXADA
INVARIABLE
PERMITE DUPLICADOS
Así mismo cabe resaltar que las tuplas admiten guardar todos los tipos de variables que hay en python, enteros, strings y booleanos 
y su sintaxis principal es mediante la declaracion de variables y los elementos se ecriben entre parentesis ()
Ejemplos:
"""
tuple = ('Vimos', 'que', 'las', 'listas', 'y', 'cadenas', 'tienen', 'propiedades', 'en', 'común')
print(tuple[4])
print(type(tuple))
print(tuple)

#Tambien se puden hacer tuplas anidadas
tuple2 = tuple, (3,4,6,8,1,2)
print(tuple2)

#Asimismo se recuerde que las tuplas son inmutables
#tuple2[6] = ('Hola')


#Pero las tuplas pueden tener dentro de si elementos mutables

tuple3 = ([3,2,6,7,2],['Hola', 'Mundo', 'como', 'estan'])

"""
Una caracteristica especial de las tuplas es que aquellas tuplas que tengan de 0 a 1 elementos,
presentaran algunos cambios y caracteristicas diferentes en su sintaxis

"""
tuplavacia = () #para crear una tupla vacia se declara la variable y luego se colocan los parentesis vacios
print (len(tuplavacia)) # Asi mediante el metodo len se comprueba que la tupla esta vacia

tupla1item = ('1ITEM',) #para crear una tupla con un solo item se debe poner la sintaxis basica y el item deseado, agregandole una coma al final del item

"""
-Conjuntos
Los conjuntos son otro tipo de dato en python, se caracterizan por ser:
Desordenadas
Inmutables
No indexada
No permite elementos duplicados
Importante recordar que al igual que los otros tipos de datos en python (listas, tuplas y diccionarios) aceptan todo tipo de variables, desde enteros, flotantes, string, boolean.

Así mismo la sintaxis está formada por corchetes, de la siguiente manera:


conjunto = {"apple", "banana", "cherry"}

Generalmento se usan oara la verificacion de pertinencia y eliminacion de entradas duplicadas,
ademas soportan operaciones matematicas como la union, interseccion, diferencia y diferencia simetrica.

el nombre clave en python de los conjunto es mediante la palabra reservada set() aunque su sintaxis base es set = {}
"""
conjunto = {'los', 'f22', 'raptor', 'son', 'los', 'cazas', 'de', 'quinta', 'generacion', 'mas', 'avanzados', 'del', 'planeta'}
print(conjunto)
print(type(conjunto))

#Tambien se puden crear condiciones que retornan True o False con las tuplas como en el siguiente ejemplo
'f22' in conjunto
'aviones' in conjunto

#A continuacion se demostraran las operaciones que se puden hacer con los conjuntos
a = set('colombiaesunpaislaico')
b = set('colombiaesunadenocracia')
print(a)
print(a-b) #Muestra las letras que estan en a pero no en b
print (a|b) #Muestra las letras en a o en b o en ambas
print(a&b) #Muestra las letras de ambos conjuntos
print(a^b) #Muestra las letras en a o en b pero no en ambos

a = {x for x in 'colombiaesunpaislaico' if x not in 'abc'}


"""
-Diccionarios
Los diccionarios son un tipo de colección que almacena grupos de datos divididos en palabra clave y valor, 
están ordenados, permiten la manipulación de datos y no permite datos duplicados, también manejan todo tipo de datos, 
enteros, caracteres y booleanos.
*Cabe destacar que cuando un dato esta repetido se sobrescribirá uno de los dos. 
Ejemplo:
Diccionario = {"Hola" : "Mundo", "Python" : "Lenguaje", "Año" : "1984", "Creador" : "Guido van Rossum", "Python" : "Programacion de datos"}  

# En este caso solo imprimirá alguno de las dos variables “Python”

**A partir de la versión 3.7 de python los diccionarios están ordenados, desde las versiones anteriores de 3.6 están desordenadas** 
Su sintaxis está definida por corchete y el conjunto de palabra clave y valor se dividen mediante dos puntos:


En Caso de querer tener un diccionario vacio solo se colocara unas llaves vacias dict = {}
Ejecutando list(d) en un diccionario retornará una lista con todas las claves usadas en el diccionario, 
en el orden de inserción (si deseas que esté ordenada simplemente usa sorted(d) en su lugar). 
Para comprobar si una clave está en el diccionario usa la palabra clave in.

"""
#A continuacion se mostraran unos ejemplos basicos de la estructura y sintaxis que tiene python, 
#entre ellas destacan el metodo del y la capacidad de cambiar un diccionario a lista, tyomando solo las claves 
Diccionario = {"Hola" : "Mundo", "Python" : "Lenguaje", "Año" : 1984, "Creador" : "Guido van Rossum", "Python" : "Programacion de datos"}
print(Diccionario)
print(type(Diccionario))

Diccionario ['Paradigma'] = 'Orientado a objetos'
print(Diccionario)

print(Diccionario['Creador'])

del Diccionario['Hola']
Diccionario['Paradigma2'] = 'Multiparadigma'

Diccionario_a_lista = list(Diccionario)
print(Diccionario_a_lista)

#Exite la palabra reseervada en python Dict que se refire a los diccionarios,
#y trae consigo una serie de funciones y tareas, como por ejemplo cambio o definir 
# una sere de listas, tuplas o cadenas 
Diccionario2 = dict([('Nombres', 'Maicol Pedro'), ('Apellidos', 'Zamora Zambrano'), ('Años', 23)])
print(Diccionario2)

# Compresion/Creacion de Diccionarios con cadenas simples
x = 0

print({x: x**2 for x in (2, 4, 6)})

"""
-Tecnicas o Formas de Iteracionpara los diccionarios
Una resultado de las iteraciones es la obtencion de la clave y valor utilizando el metodo items

"""
#Diccionario = {"Hola" : "Mundo", "Python" : "Lenguaje", "Año" : 1984, "Creador" : "Guido van Rossum", "Python" : "Programacion de datos"}
for i, j in Diccionario.items():
    print(i, j)

#Tambien se puede obtener el indice de pocision junto a su valor correspondiente usando la funcion enumerate()
for i, j in enumerate([1,2,3,4,5,6,7]):
    print(i,j)


#Cuando se desea iterar dos o mas secuencias al mismo tiempo los valores se puden emparejar con la funcion zip()

nombre1 = ['Ingenieria', 'Diseño', 'Ciencias']
nombre2 = ['de Sistemas', 'Grafico', 'Politicas']
for i, j in zip(nombre1,nombre2):
    print('Yo estudio {0} {1}.' .format(i,j)) 

#Si se desea iterar una secuencia en orden inverso, se especifica primero la secuencia al derecho y luego se llama a la funcion reversed()
for i in reversed(range(0,20,5)):
    print (i)



#Para iterar en una secuencia oredenada se utiliza función sorted() la cual retorna una nueva lista ordenada dejando a la original intacta.
futbol = ['mundial', 'qatar', 'championss', 2022, 'premier league']
for i in sorted(futbol):
    print(i)


#El uso de set() en una secuencia elimina los elementos duplicados. El uso de sorted() en combinación con set() sobre una secuencia es una forma 
#idiomática de recorrer elementos únicos de la secuencia en orden ordenado.
futbol = ['mundial', 'qatar', 'championss', 2022, 'premier league']
for i in sorted(set(futbol)):
    print(i)

#Para modificar una lista mientras se esta iterando, aunque se recomienda utilizar una nueva lista
import math
futbol2 = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtrar_informacion = []
for v in futbol2:
    if not math.isnan(v):
        filtrar_informacion.append(v)

print(filtrar_informacion)



"""
-Acerca de Condiciones 
Las condiciones como while o if generalmente utilizan 
cualquier tipo de operador no solamente comparaciones.
Uno de ello son los operadores de comparacion in y not in
que determinan si un valor esta o no esta dentro del contenedor.
Tambien existen los operadores is y is not que compara si dos objetos son realmente
el mismo objeto, tambien cabe destacar que todos los operadores de comparacion tienen
la misma prioridad, pero es menor que la de los operadores numericos



"""
"""
postman
api rest
"""
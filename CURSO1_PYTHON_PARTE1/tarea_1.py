"""
Alumna: Alicia Carballido García
Tarea: Curso de Fundamento de Python Parte 1
Fecha de realización: 27 de marzo de 2022

INSTRUCCIONES:
1. Crear una cadena de tipo parrafo con un poema
2. Crear una cadena de tipo parrafo con un haiku, usar caracteres especiales y el caracter de scape para darle formato 
3. Crear una cadena de tipo parrafo con un poema y mediante slicing imprimir el primer verso
4. Crear una cadena de tipo parrafo con un poema y mediante slicing e indices negativos imprimir el último verso
5. Pedir una palabra
6. Pedir una oración
7. Pedir varias oraciones y crear un parrafo
8. Pedir una oración y determinar la cantidad de caracteres (contando espacios) que tiene
9. Pedir una oración y determinar si la letra x se encuentra en la oración
10. Crear una oración e imprimirla asegurando que no existen espacios al inicio y al final de la oración, imprimirla en mayúsculas y en minúsculas
11. Pedir una oración y cambiar todos los espacios por guiones bajos
12. Pedir una oración y cambiar los primeros 3 espacios por puntos
13. Pedir los datos de 3 alumnos (nombre, apellido, edad y carrera) e imprimirlos de forma que se pueda ver una tabla

"""
#1. Crear una cadena de tipo parrafo con un poema
cadena_poema = """ 
		'Amor eterno' de Gustavo Adolfo Bécquer

		Podrá nublarse el sol eternamente;
		Podrá secarse en un instante el mar;
		Podrá romperse el eje de la tierra
		Como un débil cristal.
		¡todo sucederá! Podrá la muerte
		Cubrirme con su fúnebre crespón;
		Pero jamás en mí podrá apagarse
		La llama de tu amor.
"""
print(cadena_poema)
#2. Crear una cadena de tipo parrafo con un haiku, usar caracteres especiales y el caracter de scape para darle formato 
cadena_haiku = "\t\'Noche sin luna.\n\tLa tempestad estruja\n\tlos viejos cedros.\'\n\n\tMatsuo Basho"
print(cadena_haiku)

#3. Crear una cadena de tipo parrafo con un poema y mediante slicing imprimir el primer verso
print("Primer verso:", cadena_poema[47:83])

#4 Crear una cadena de tipo parrafo con un poema y mediante slicing e indices negativos imprimir el último verso
print("Último verso:",cadena_poema[-21:-1])

#5. Pedir una palabra
palabra = input("Dame una palabra:")

#6. Pedir una oración
oracion = input("Dame una oración:")

#7. Pedir varias oraciones y crear un parrafo
cantidad_oraciones = int(input("¿Cuántas oraciones quieres unir en el párrafo?"))
parrafo = ""
for oracion in range(cantidad_oraciones):
	parrafo += "\n" + input("Dame la oración:")
print("El párrafo completo es:", parrafo)

#8. Pedir una oración y determinar la cantidad de caracteres (contando espacios) que tiene

oracion = input("Dame una oración:")
contador = 0
for i in range(len(oracion)):
	if oracion[i] == " ":
		contador+=1
print("La cantidad de espacios es:", contador)

#9. Pedir una oración y determinar si la letra x se encuentra en la oración
oracion = input("Dame una oración:")
letra_a_buscar = input("¿Qué letra quieres encontrar en la oración?:")
if letra_a_buscar in oracion: 
	print(f'La letra {letra_a_buscar} se encuentra en la oración. ')
else: 
	print(f'La letra {letra_a_buscar} no se encuentra en la oración. ')


#10. Crear una oración e imprimirla asegurando que no existen espacios al inicio y al final de la oración, imprimirla en mayúsculas y en minúsculas

oracion = input("Dame una oracion:")
if oracion[0] == " " and oracion[0] == " ":
	print("Oracion en mayúsculas: ", oracion.upper())
	print("Oración en minúsculas: ", oracion.lower())
else: 
	print("La oración no tiene espacios al inicio y al final.")


#11. Pedir una oración y cambiar todos los espacios por guiones bajos
oracion = input("Dame una oración: ")
nueva_oracion = list(oracion)
for i in range(len(nueva_oracion)):
	if nueva_oracion[i] == " ":
		nueva_oracion[i] = "_"
print("".join(nueva_oracion))

#12. Pedir una oración y cambiar los primeros 3 espacios por puntos
oracion = input("Dame una oración: ")
nueva_oracion = list(oracion)
for i in range(3):
	nueva_oracion[i] = "."
print("".join(nueva_oracion))

#13. Pedir los datos de 3 alumnos (nombre, apellido, edad y carrera) e imprimirlos de forma que se pueda ver una tabla
tabla = ""
for i in range(3):
	nombre = input("Dame tu nombre:")
	apellido = input("Dame tu apellido:")
	edad = input("Dame tu edad:")
	carrera = input("Dame tu carrera")
	tabla += "|Nombre:" + nombre + "\n|Apellido:" + apellido + "\n|Edad:" + edad + "\n|Carrera:" + carrera+ "\n********************\n"
print(tabla)
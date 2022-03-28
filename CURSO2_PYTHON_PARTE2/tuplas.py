'''
#1. Generar una tupla que contenga las 5 vocales del abecedario
vocales = ('a','e','i','o','u')
#2. Generar una tupla que contenga las demás letras (consonantes del abecedario)
consonantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
#3. Generar una tupla que contenga las dos tuplas anteriores
tupla_union = vocales + consonantes
print("Ejercicio 3:",tupla_union)

#4. Generar una tupla que contenga las dos tuplas anteriores pero transformadas en lista (la tupla tendrá como items dos listas, la de vocales y la de consonantes)

conversion = (list(vocales), list(consonantes))
print(conversion)

#5. Desempaquetar esta última tupla y mediante el desempaquetado, sumar los iterables para después generar una lista con todas las letras del abecedario, ordenarla y transformarla en tupla
desempaquetado = conversion[0][:] + conversion[1][:]
tupla_desempaquetada = sorted(desempaquetado)
tupla_desempaquetada2 = tuple(tupla_desempaquetada)
print("Ejercicio 5:", tupla_desempaquetada2)

#6. Comparar la tupla generada en el ejercicio 6 (no era la 5?) con la generada en el ejercicio 3, ¿Qué resulta?
if tupla_desempaquetada2 == tupla_union:
	print("Iguales.")
else: 
	print("Diferentes.")
#El orden es diferente, por lo que no son iguales a pesar de tener los mismos elementos. 
'''
'''7. Dada la tupla:
  ([1,"b",4,-99,10+1j,"b","c",True,"z","hola",1,-999,-5,1-1j,False],[],[],[])
  7.1 Manejar las listas de la tupla de tal manera que en la primera aparezcan puros números, en la segunda puras cadenas, en la tercera números complejos y en la última los booleanos.
  7.2 Tratar de ordenar las listas y generar una tupla con la concatenación de cada una de las listas de la tupla.'''

tupla = ([1,"b",4,-99,10+1j,"b","c",True,"z","hola",1,-999,-5,1-1j,False],[],[],[])
nueva_lista = [[],[],[],[]]

for i in tupla[0]:
	#Números
	if isinstance(i, int) or isinstance(i, float):
		nueva_lista[0].append(i)
	if isinstance(i, str):
		nueva_lista[1].append(i)
	if isinstance(i, complex):
		nueva_lista[2].append(i)
	if isinstance(i, bool):
		nueva_lista[3].append(i)

print(nueva_lista)
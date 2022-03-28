#1. Realizar un programa que lea una palabra y determine si es un palindromo
palabra = input("Dime una palabra que sea palíndromo:")
palabra_limpia = palabra.replace(" ", "")
print(palabra_limpia)
if palabra_limpia[::-1] == palabra_limpia:
	print("Es un palíndromo.")
else: 
	print("No es un palíndromo.")

#2. Un anagrama es una palabra que tiene las mismas letras que otra pero en otro orden, por ejemplo: quieren y enrique, riesgo y sergio, poder y pedro. Realizar un programa que determine si dos palabras son anagramas. Deberemos mantener todas las letras en minusculas para poder compararlas y tener cuidado con los acentos
palabra1 = input("Dime la palabra 1.")
palabra2 = input("Dime la palabra 2.")

palabra1 = list(palabra1)
palabra1_ordenada = sorted(palabra1)

palabra2 = list(palabra2)
palabra2_ordenada = sorted(palabra2)

if(set(palabra1) == set(palabra2)):
    print("Es un anagrama.")
else:
    print("No es un anagrama.")
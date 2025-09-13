#1) Imprimir en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


#2) Pedir al usuario un número entero y determine la cantidad de dígitos que contiene.
import math
num = int(input('Ingrese un número: '))
cantidad = 0

while num>0:
    digito = math.trunc(num/10)
    num = digito
    cantidad += 1

print(f"Cantidad de dígitos: {cantidad}")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input('Ingrese el primer número: ')) 
num2 = int(input('Ingrese el segundo número: ')) 
suma = 0


if num1>num2:
    num1, num2 = num2, num1

for i in range((num1+1), num2):
    suma +=i
    

print(f"Suma de todos los números entre {num1} y {num2}: {suma}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print('Ingrese los números a continuación: ')
suma = 0
num = 1

while True:
    num = int(input('- '))
    if num == 0:
        break
    
    suma += num

print(f"Suma total: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

num_aleatorio = random.randint(0, 9)
intentos = 0

print('¡Juguemos a las adivinanzas!')
print('Ingrese un número entre 0 y 9: ')
while True:
    num_usuario = int(input('- '))

    intentos +=1 
    if num_usuario == num_aleatorio:
        print(f'¡Adivinaste! El número era {num_aleatorio}')
        print(f'Número de intentos: {intentos}')
        break
        


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input('Ingrese un número: '))
suma=0

for i in range(0, num+1):
    suma+=i

print(f"Suma de números entre 0 y {num}: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.

print("Ingrese los números a continuación: ")
pares, impares, positivos, negativos = 0, 0, 0, 0

for i in range(0, 100):
    num = int(input('- '))

    if num%2==0:
        pares += 1
    else:
        impares += 1
    
    if num>0:
        positivos += 1
    else:
        negativos += 1

print(f"""
    Cantidad de pares: {pares}
    Cantidad de impares: {impares}
    Cantidad de positivos: {positivos}
    Cantidad de negativos: {negativos}""")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores.

from statistics import mean

print('Ingrese los números a continuación: ')
lista = []

for i in range(0, 100):
    num = int(input(f'{i+1}. '))
    lista.append(num)

media = mean(lista)

print(f'Media: {media}')


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
import math

num = int(input('Ingrese un número: '))
aux = 0
numero_invertido = 0
digito = 0

while num>0:
    digito = num%10
    numero_invertido = numero_invertido * 10 + digito
    num = math.trunc(num/10)

print(f'Número invertido: {numero_invertido}')
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:54:47 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

n = input('Ingrese un valor para n (botellas en el mercado): ')
n = int(n)

x = input('Ingrese un valor para x (botellas usadas): ')
x = int(x)

total = 0

while (n >= x):
    # Obtenemos el resto de la division usando el operador mod
    resto = n % x

    # Dividimos el valor de 'n' con 'x' obteniendo un valor entero
    n = n // x

    # Incrementamos la iteración
    total = total + n
    n = n + resto

# El proceso está completo y entregamos al usuario la cantidad de botellas producidas
print(f'Se logran producir {total} botellas')

# Reto #4: PRIMO, FIBONACCI Y PAR
# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo,
#  * fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def fibonacci_list(num):
    fibonacci_list = []
    for i in range(100):
        if i == 0 or i == 1:
            fibonacci_list.append(i)
        else:
            fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
        
    return fibonacci_list

def tipo_numero(num):
    if num % 2 == 0:
        par = "y es par"
    else:
        par = "y es impar"
    if num in fibonacci_list(num):
        fibonacci = "fibonacci"
    else:
        fibonacci = "no es fibonacci"
    div = 0
    for i in range(1,num + 1):
        if num % i == 0:
            div += 1
    
    if div == 2:
        primo = "es primo,"
    else:
        primo = "no es primo,"
    
    return primo, fibonacci, par

numero = int(input("Teclee un número:" ))
primo, fibonacci, par = tipo_numero(numero)

print(numero, primo, fibonacci, par)

import math
from colorama import Fore, Back, Style, init
init(convert=True)



cateto1_input_variables = ["cateto1", "c1", "cateto 1",
 "primer cateto", "cateto uno", "1", "a"]
cateto2_input_variables = ["cateto2", "c2", "cateto 2",
 "segundo cateto", "cateto dos", "2", "b"]
hipotenusa_input_variables = ["hipotenusa", "3", "h", "c"]

print(Fore.GREEN + "Bienvenido a la calculadora del Teorema de Pitágoras!")

while True:

        print(Fore.WHITE) 
        print("Por favor escoja el dato a buscar")
        print("Opciones: Cateto 1, Cateto 2 o Hipotenusa")
        incognita = input("Incógnita: ").lower()
        
        if incognita in cateto1_input_variables: 
            while True:
                try:
                    print(Fore.WHITE)
                    cateto2 = float(input("Ingrese el valor del cateto conocido: "))
                    if cateto2 <= 0:
                        print(Fore.RED + "Por favor ingresar un valor mayor a 0")
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Por favor ingresar un valor numérico")
                    continue
            
            while True:   
                try:
                    print(Fore.WHITE)
                    hipotenusa = float(input("Ingrese el valor de la hipotenusa: "))
                    if hipotenusa <= 0:
                        print(Fore.RED + "Por favor ingresar un valor mayor a 0")
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Por favor ingresar un valor numérico")
                    continue
            try:
                cateto1= math.sqrt(hipotenusa ** 2 - cateto2 ** 2)
                print(Fore.YELLOW + Style.BRIGHT)
                print("El valor del cateto es igual a" , cateto1)
                break
            except:
                print(Fore.RED)
                print("Error matemático: el valor de la hipotenusa debe ser mayor al valor de los catetos.")
                continue

        elif incognita in cateto2_input_variables:
            while True:
                try:
                    print(Fore.WHITE)
                    cateto1 = float(input("Ingrese el valor del cateto conocido: "))
                    if cateto1 <= 0:
                        print(Fore.RED + "Por favor ingresar un valor mayor a 0")
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Por favor ingresar un valor numérico")
                    continue
            
            while True:   
                try:
                    print(Fore.WHITE)
                    hipotenusa = float(input("Ingrese el valor de la hipotenusa: "))
                    if hipotenusa <= 0:
                        print(Fore.RED + "Por favor ingresar un valor mayor a 0")
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Por favor ingresar un valor numérico")
                    continue
            try:
                cateto2= math.sqrt(hipotenusa ** 2 - cateto1 ** 2)
                print(Fore.YELLOW + Style.BRIGHT)
                print("El valor del cateto es igual a" , cateto2)
                break
            except:
                print(Fore.RED)
                print("Error matemático: el valor de la hipotenusa debe ser mayor al valor de los catetos.")
                continue
        
        elif incognita in hipotenusa_input_variables:
            while True:
                try:
                    print(Fore.WHITE)
                    cateto1 = float(input("Ingrese el valor del primer cateto: "))
                    if cateto1 <= 0:
                        print(Fore.RED + "Por favor ingresar un valor mayor a 0")
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Por favor ingresar un valor numérico")
                    continue
            
            while True:   
                try:
                    print(Fore.WHITE)
                    cateto2 = float(input("Ingrese el valor del segundo cateto: "))
                    if cateto2 <= 0:
                        print(Fore.RED + "Por favor ingresar un valor mayor a 0")
                        continue
                    else:
                        break
                except:
                    print(Fore.RED + "Por favor ingresar un valor numérico")
                    continue

            hipotenusa= math.sqrt(cateto1 ** 2 + cateto2 ** 2)
            print(Fore.YELLOW + Style.BRIGHT)
            print("El valor de la hipotenusa es igual a" , hipotenusa)
            break
        
        else:
            print(Fore.RED + "Denominación no válida")
            continue


   






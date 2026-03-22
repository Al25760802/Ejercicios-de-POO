###
## Excepciones basicas

# Parte 1: try / except simple
print("=" *50)
print("parte 1: Division con manejo de errores")
print("=" *50)

try:
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    total = a / b
    print(f"El resultado de la division es: {total}")

except ValueError:
    print("Error: debes ingresar un numero entero, no una letra")

except ZeroDivisionError:
    print("error: No se puede dividir entre cero")
    
else:
  print(f"El resultado de {a} / {b} es: {total}")

finally:
  print("¡Gracias por usar el programa de división!")    
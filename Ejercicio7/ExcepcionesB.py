###
# Excepciones basicas / Capturar 

#Parte 2:
print("=" *50)
print("parte 1: Division con manejo de errores")
print("=" *50)

# Creamos una lista de colores.
colores = ["rojo", "verde", "azul", "amarillo"]
print(f"Lista de colores: {colores} (indices 0,1,2,3)")

try:
    indice =( input("que color quieres accerder? (0-3):"))
    print(f"El color seleccionado es: {colores[indice]}")
    
except ValueError as e:
    print (f"Valuerror: {E}")
    
except IndexError as e:
    print(f"IndexError: {e}")
    print(f"Solo puedes usar los nuemros del 0 al 3 para acceder a los colores")
    
finally:
    print("-- Fin del programa")
    
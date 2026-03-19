19 de Marzo 2026

# Declaración

# frase = "Anita lava la tina"
nombre = "Carlos"


# Concatenación
print("Hola, " + nombre)          # con +
# print("Hola,", nombre)            # con coma
# print(f"Hola, {nombre}!")         # f-string ✅ recomendado
# print("Hola, {}!".format(nombre)) # .format()

# Longitud y acceso por índice
# print(len(frase))    # 18
# print(frase[0])      # 'A'  (primer carácter)
# print(frase[-1])     # 'a'  (último carácter)
# print(frase[0:5])    # 'Anita' (slicing)

# Métodos útiles
# frase.upper()        # ANITA LAVA LA TINA
# frase.lower()        # anita lava la tina
# frase.replace("Anita","Bob")    # Bob lava la tina
# frase.split(" ")     # ['Anita', 'lava', 'la', 'tina']
# "  hola  ".strip()   # 'hola'  (sin espacios)
# frase.startswith("A")  # True
# "Python" in frase      # False
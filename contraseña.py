import secrets
import string

# Diccionario con tipos de caracteres
diccionario = {
    'letras': string.ascii_letters,  # Letras mayúsculas y minúsculas
    'numeros': string.digits,        # Dígitos numéricos
    'caracteres': string.punctuation # Caracteres especiales
}

def generar_pass(caracteres_disponibles, longitud=12):
   
    if not caracteres_disponibles:
        print("Debes seleccionar al menos una opción (números, letras o caracteres especiales).")
        return None
    
    # Asegurar que `caracteres_disponibles` es una lista de listas (por tipo)
    if isinstance(caracteres_disponibles, str):
        caracteres_disponibles = [caracteres_disponibles]

    # al menos un caracter de cada tipo seleccionado
    caracteres_iniciales = [secrets.choice(caracter) for caracter in caracteres_disponibles]
    
    # Rellena el resto con caracteres aleatorios 
    resto_caracteres = ''.join(caracteres_disponibles)  # Combina todos los tipos 
    if longitud > len(caracteres_iniciales):
        caracteres_iniciales += [secrets.choice(resto_caracteres) for _ in range(longitud - len(caracteres_iniciales))]
    
    # Mezclar los caracteres para que no haya un orden predecible
    secrets.SystemRandom().shuffle(caracteres_iniciales)
    
    return ''.join(caracteres_iniciales)


while True:
    print("👉------------------------WELCOME------------------------👈")
    print()
    print("                Generador de Contraseñas V0.1")
    print()
    print("•»--------------------------(•o•)------------------------«•")
    print("\n")
    print("Seleccione una de las siguientes opciones:")
    print("»    1. Generar contraseña solo de Letras.")
    print("»    2. Generar contraseña solo de Números.")
    print("»    3. Generar contraseña con Letras y Números.")
    print("»    4. Generar contraseña con Letras, Números y Caracteres.")
    print("»    0. Salir.")


    try:
        opcion = int(input("►    Escriba la opción seleccionada: "))
    except ValueError:
        print("❌ Por favor, ingrese un número valido.")
        continue

    if opcion == 0:
        print("👋 ¡Gracias por usar el generador de contraseñas!")
        break
    elif opcion == 1:
        caracteres_disponibles = diccionario['letras']
    elif opcion == 2:
        caracteres_disponibles = diccionario['numeros']
    elif opcion == 3:
        caracteres_disponibles = diccionario['letras'] + diccionario['numeros']
    elif opcion == 4:
        caracteres_disponibles = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
    else:
        print("❌ Opción no válida. Intente nuevamente.")
        continue

    longitud = int(input("🔢 Ingrese la longitud deseada de la contraseña (mínimo 4): "))
    if longitud < 4:
        print("❌ La longitud mínima es de 4 caracteres.")
        continue

    contraseña = generar_pass(caracteres_disponibles, longitud)
    if contraseña:
        print("\n")
        print("========================================")
        print(f"🔑 Contraseña generada=> {contraseña}  ")
        print("========================================")
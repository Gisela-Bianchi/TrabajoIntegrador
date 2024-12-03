import random
import pickle
import os
#donde se guardan los tickets
archivo_tickets = "tickets.pkl"
#se cargan los tickets al iniciar el programa
if os.path.isfile(archivo_tickets):
    with open(archivo_tickets, "rb") as f:
        tickets = pickle.load(f)
else:
 tickets = []
while True:
    print("\n")
    print("Hola bienvenido al sistema de Tickets\n")
    print("==============================")
    print("1. Generar un Nuevo Ticket   |")
    print("2. Leer un Ticket            |")
    print("0. Salir                     |")
    print("==============================")
    opcion = int(input("Por favor, selecciona una opcion: "))

    if opcion == 1:  # Alta ticket
        seguir = "s"
        while seguir == "s":
            nombre = input("Ingrese su Nombre: ")
            sector = input("Ingrese su Sector: ")
            asunto = input("Ingrese Asunto: ")
            problema = input("Ingrese un Mensaje: ")
            numero = random.randint(1000, 9999)

            ticket = [nombre, sector, asunto, problema, numero]
            tickets.append(ticket)



            print("======================================")
            print("Se genero el siguiente Ticket")
            print("======================================")
            print("Su nombre:", ticket[0], "    NºTicket:", ticket[4])
            print("Sector:", ticket[1])
            print("Asunto:", ticket[2])
            print("Mensaje:", ticket[3])
            print("        Recordar su numero de Ticket")

            seguir = input("¿Desea generar un nuevo Ticket? (s/n): ").lower()
            while seguir not in ("s", "n"):
                print("Por favor, ingresa una letra correcta (s o n).")
                seguir = input("¿Quieres registrar un nuevo ticket? (s/n): ").lower()

    elif opcion == 2:  # Ver ticket
        if not tickets:
            print("\nNo hay tickets disponibles.\n")
        else:
            while True:
                try:
                    numero_ticket = int(input("Ingrese el numero del Ticket que desea leer: "))
                    encontrado = False
                    for ticket in tickets:
                        if ticket[4] == numero_ticket:
                            print("\n======================================")
                            print("Ticket encontrado:")
                            print("======================================")
                            print("Nombre:", ticket[0])
                            print("Sector:", ticket[1])
                            print("Asunto:", ticket[2])
                            print("Mensaje:", ticket[3])
                            print("NºTicket:", ticket[4])
                            print("======================================\n")
                            encontrado = True
                            break
                    if not encontrado:
                        print("\nNo se encontro un ticket con ese numero. Intente nuevamente.\n")

                    seguir = input("¿Desea leer otro Ticket? (s/n): ").lower()
                    while seguir not in ("s", "n"):
                        print("Por favor, ingresa una letra correcta (s o n).")
                        seguir = input("¿Desea leer otro Ticket? (s/n): ").lower()

                    if seguir == "n":
                        break
                except ValueError:
                    print("Por favor, ingrese un numero valido.\n")
    elif opcion == 0:  # Salir
        print("Guardando tickets...")
        with open(archivo_tickets, "wb") as f:
            pickle.dump(tickets, f)
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida")

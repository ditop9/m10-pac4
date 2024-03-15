import sys

from aplication import aplicacio


# Mostra les opcions del menú principal
def mostrar_menu_principal():
    print("\nMENÚ PRINCIPAL")
    print("============================")
    print("Tria una opció i prem Intro")
    print("============================")
    print("1. Afegir client")
    print("2. Eliminar client")
    print("3. Consultar client")
    print("4. Modificar un camp d'un client")
    print("0. Sortir\n")
    print("Opció:")


# Mètode per executar les funcions que proporciona el menú principal del programa
def escollir_opcio_menu_principal(option, llibreta):
    # Generar nou client al sistema
    if option == 1:
        llibreta.generar_client()
    # Eliminar un client existent pel seu ID
    elif option == 2:
        id_client = int(input("INTRODUEIX L'ID DEL CLIENT QUE VOLS ELIMINAR"))
        llibreta.eliminar_client(id_client)
    # Opció que executa el menú de consulta de clients
    elif option == 3:
        option_menu_consulta = -1
        # Es repeteix l'execució del menú mentre que la opció escollida sigui diferent a '0'
        while option_menu_consulta != 0:
            mostrar_menu_consulta()
            try:
                option_menu_consulta = int(input())
                escollir_opcio_menu_consulta(option_menu_consulta, llibreta)
            except ValueError:
                print("ERROR: No és una opció vàlida")
    # Opció que executa el menú de modificació d'atributs dels clients existents
    elif option == 4:
        # Cerca el client que es vol modificar pel seu ID
        id_client = int(input("INTRODUEIX L'ID DEL CLIENT QUE VOLS CERCAR\n"))
        client = llibreta.cercar_per_id(id_client)
        # En cas que es trobi un client executa el menú de consulta
        if client is not None:
            mostrar_menu_modificar()
            try:
                option_menu_modificar = int(input())
                escollir_opcio_menu_modificar(option_menu_modificar, client, llibreta)
            except ValueError:
                print("ERROR: No és una opció vàlida")
    # Tanca el programa
    elif option == 0:
        print("El programa es tanca...")
        sys.exit(0)
    else:
        print("ERROR: No és una opció vàlida")


# Mostra les opcions del menú de consulta de clients
def mostrar_menu_consulta():
    print("\nMENÚ CONSULTA")
    print("============================")
    print("Tria una opció i prem Intro")
    print("============================")
    print("1. Cercar client per Identificador")
    print("2. Cercar client per Nom")
    print("3. Cercar client per cognom")
    print("4. Llistar tots els clients")
    print("0. Enrere\n")
    print("Opció:")


# Mètode per executar les funcions que proporciona el menú de consulta de clients
def escollir_opcio_menu_consulta(option, llibreta):
    # Cerca de client per ID
    if option == 1:
        id_client = int(input("INTRODUEIX L'ID DEL CLIENT QUE VOLS CERCAR\n"))
        print(llibreta.cercar_per_id(id_client))
    # Cerca de client per nom. Retorna una llista amb tots el clients trobats amb aquest nom
    elif option == 2:
        nom_client = input("INTRODUEIX EL NOM DEL CLIENT QUE VOLS CERCAR\n")
        llista_clients_trobats = llibreta.cercar_per_nom(nom_client)
        if llista_clients_trobats:
            for client in llista_clients_trobats:
                print(client)
        else:
            print("ERROR: No s'han trobat clients amb aquest nom")
    # Cerca de client per cognom. Retorna una llista amb tots el clients trobats amb aquest cognom
    elif option == 3:
        cognom_client = input("INTRODUEIX EL COGNOM DEL CLIENT QUE VOLS CERCAR\n")
        llista_clients_trobats = llibreta.cercar_per_cognom(cognom_client)
        if llista_clients_trobats:
            for client in llista_clients_trobats:
                print(client)
        else:
            print("ERROR: No s'han trobat clients amb aquest cognom")
    # Mostra tots el clients disponibles
    elif option == 4:
        print(llibreta.get_llista_clients())
    # Torna al menú principal
    elif option == 0:
        print("Tornant al menú principal...")
        aplicacio.run(llibreta)
    else:
        print("ERROR: No és una opció vàlida")


# Mostra les opcions del menú de modificació de clients
def mostrar_menu_modificar():
    print("\nMENÚ MODIFICACIÓ")
    print("============================")
    print("Tria una opció i prem Intro")
    print("============================")
    print("1.  Modificar nom")
    print("2.  Modificar cognom")
    print("3.  Modificar telèfon")
    print("4.  Modificar correu electrònic")
    print("5.  Modificar adreça")
    print("6.  Modificar codi postal")
    print("7.  Modificar ciutat")
    print("8.  Modificar província")
    print("9. Modificar país")
    print("0. Enrere\n")
    print("Opció:")


# Mètode per executar les funcions que proporciona el menú de modificació d'atributs de clients
def escollir_opcio_menu_modificar(option, client, llibreta):
    # Modificar el nom
    if option == 1:
        client.nom = input("Introdueix el nou nom\n")
    # Modificar el cognom
    elif option == 2:
        client.cognom = input("Introdueix el nou cognom\n")
    # Modificar el telèfon
    elif option == 3:
        try:
            client.telefon = int(input("Introdueix el nou telèfon\n"))
        except ValueError:
            print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")
    # Modificar el correu electrònic
    elif option == 4:
        client.correu = input("Introdueix el nou correu electrònic\n")
    # Modificar la direcció
    elif option == 5:
        client.adress = input("Introdueix la nova direcció\n")
    # Modificar el codi postal
    elif option == 6:
        try:
            client.codi_postal = int(input("Introdueix el nou codi postal\n"))
        except ValueError:
            print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")
    # Modificar la ciutat
    elif option == 7:
        client.ciutat = input("Introdueix la nova ciutat\n")
    # Modificar la província
    elif option == 8:
        client.provincia = input("Introdueix la nova província\n")
    # Modificar el país
    elif option == 9:
        client.pais = input("Introdueix el nou pais\n")
    # Tornar al menú principal
    elif option == 0:
        print("Tornant al menú")
        aplicacio.run(llibreta)
    else:
        print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")

import sys

import menu
from llibreta import Llibreta


def escollir_opcio_menu_principal(option, llibreta):
    if option == 1:
        id_client = int(input("INTRODUEIX L'ID DEL CLIENT QUE VOLS CERCAR"))
        print(llibreta.cercar_per_id(id_client))
    if option == 2:
        nom_client = input("INTRODUEIX EL NOM DEL CLIENT QUE VOLS CERCAR")
        print(llibreta.cercar_per_nom(nom_client))
    if option == 3:
        cognom_client = input("INTRODUEIX EL COGNOM DEL CLIENT QUE VOLS CERCAR")
        print(llibreta.cercar_per_cognom(cognom_client))
    if option == 4:
        print(llibreta.get_llista_clients())
    elif option == 6:
        print("TORNANT AL MENÚ PRINCIPAL...")
    else:
        print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")


def escollir_opcio(option, llibreta):
    if option == 1:
        print("DADES DEL CLIENT")
        nom = input("INTRODUEIX EL NOM")
        cognom = input("INTRODUEIX EL COGNOM")
        telefon = input("INTRODUEIX EL TELEFON")
        correu = input("INTRODUEIX EL CORREU ELECTRÒNIC")
        adress = input("INTRODUEIX L'ADREÇA")
        codi_postal = input("INTRODUEIX EL CODI POSTAL")
        ciutat = input("INTRODUEIX LA CIUTAT")
        provincia = input("INTRODUEIX LA PROVÍNCIA")
        pais = input("INTRODUEIX EL PAÍS")
        llibreta.afegir_client(nom, cognom, telefon, correu, adress, codi_postal, ciutat, provincia, pais)
    elif option == 2:
        id_client = int(input("INTRODUEIX L'ID DEL CLIENT QUE VOLS ELIMINAR"))
        llibreta.eliminar_client(id_client)
    elif option == 3:
        option_menu_consulta = 0
        while option_menu_consulta != 6:
            menu.mostrar_menu_consulta()
            try:
                option_menu_consulta = int(input())
                escollir_opcio_menu_principal(option_menu_consulta, llibreta)
            except ValueError:
                print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")
    elif option == 4:
        pass
    elif option == 5:
        print("EL PROGRAMA ES TANCA...")
        sys.exit(0)
    else:
        print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")


class Aplicacio:
    if __name__ == "__main__":
        llibreta_clients = Llibreta

        while True:
            menu.mostrar_menu_principal()
            try:
                escollir_opcio(int(input()), llibreta_clients)
            except ValueError:
                print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")

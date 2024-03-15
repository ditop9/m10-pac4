import menu
from llibreta import Llibreta


# Execució del programa. Genera una llibreta de clients i mostra el menú principal
def run(llibreta_clients):
    while True:
        menu.mostrar_menu_principal()
        try:
            menu.escollir_opcio_menu_principal(int(input()), llibreta_clients)
        except ValueError:
            print("ERROR: NO ÉS UNA OPCIÓ VÀLIDA")


class Aplicacio:
    if __name__ == "__main__":
        llibreta_clients = Llibreta()
        run(llibreta_clients)

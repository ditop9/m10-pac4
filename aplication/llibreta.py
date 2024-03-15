from aplication import aplicacio
from client import Client

"""Classe que serveix com llista de clients disponibles.
Conté les funcions necessàries per la introduccio de nous clients,
i la cerca per diferents paràmetres.
"""


class Llibreta:
    def __init__(self):
        self.llista_clients = []  # Llista que emmagatzema els clients que hi ha al sistema

    # Imprimeix per consola els clients que hi ha al creats al sistema
    def get_llista_clients(self):
        for client in self.llista_clients:
            print(client)

    # Mètode per obtenir l'identificador necessari per generar nous clients
    def id_client_comptador(self):
        # Si la llista està buida es proporciona l'id '1'
        if not self.llista_clients:
            return 1
        # Per la resta es proporciona l'identificador de l'ultim usuari a la llista + 1
        else:
            client = self.llista_clients[-1]
            return client.identificador + 1

    # Mètode per generar un nou client. Es demana que l'usuari proporcioni els atributs.
    def generar_client(self):
        print("DADES DEL CLIENT")
        nom = input("Introdueix el nom\n")
        cognom = input("Introdueix el cognom\n")
        telefon = 0
        try:
            telefon = int(input("Introdueix el telèfon\n"))
        except ValueError:
            print("ERROR: NO ÉS UN CARÀCER VÀLID\nTornant al menú...")
            aplicacio.run(self)
        correu = input("Introdueix el correu electrònic\n")
        adress = input("Introdueix l'adreça\n")
        codi_postal = 0
        try:
            codi_postal = int(input("Introdueix el codi postal\n"))
        except ValueError:
            print("ERROR: NO ÉS UN CARÀCER VÀLID\nTornant al menú...")
            aplicacio.run(self)
        ciutat = input("Introdueix la ciutat\n")
        provincia = input("Introdueix la província\n")
        pais = input("Introdueix el país\n")
        self.afegir_client(nom.capitalize(), cognom.capitalize(), telefon, correu, adress, codi_postal,
                           ciutat, provincia, pais)

    # Mètode que crea un nou client a partir dels valors rebuts per paràmetres i l'afegeix a la llista
    def afegir_client(self, nom, cognom, telefon, correu, adress, codi_postal, ciutat, provincia, pais):
        # Genera un nou identificador únic
        identificador = self.id_client_comptador()
        client = Client(identificador, nom, cognom, telefon, correu, adress,
                        codi_postal, ciutat, provincia, pais)
        self.llista_clients.append(client)

    # Elimina un client existent rebent per paràmetre el seu identificador
    def eliminar_client(self, id_client):
        trobat = False
        # Búsqueda del client a la llista
        for client in self.llista_clients:
            # Si l'identificador del client és igual a l'id proporcionat per paràmetre s'elimina el client de la llista
            if client.identificador == id_client:
                self.llista_clients.remove(client)
                print("CLIENT ELIMINAT")
                trobat = True
        if not trobat:
            print("NO S'HA TROBAT EL CLIENT")

    # Búsqueda d'un client pel seu identificador proporcionat per paràmetre. Retorna el client si el troba
    def cercar_per_id(self, id_client):
        for client in self.llista_clients:
            if client.identificador == id_client:
                return client
        print("NO S'HA TROBAT EL CLIENT")
        return None

    # Búsqueda d'un client pel seu nom proporcionat per paràmetre. Es retorna una llista amb tots els
    # clients trobats amb aquest nom
    def cercar_per_nom(self, nom_client):
        clients_trobats = []
        trobat = False
        for client in self.llista_clients:
            # Si el nom del client és igual al proporcionat per paràmetre, s'afegeix el client a la llista
            if client.nom.lower() == nom_client.lower():
                clients_trobats.append(client)
                trobat = True
        if not trobat:
            return None
        else:
            return clients_trobats

    # Búsqueda d'un client pel seu cognom proporcionat per paràmetre. Es retorna una llista amb tots els
    # clients trobats amb aquest cognom
    def cercar_per_cognom(self, cognom_client):
        clients_trobats = []
        trobat = False
        for client in self.llista_clients:
            # Si el cognom del client és igual al proporcionat per paràmetre, s'afegeix el client a la llista
            if client.cognom.lower() == cognom_client.lower():
                clients_trobats.append(client)
                trobat = True
        if not trobat:
            return None
        else:
            return clients_trobats

from client import Client


class Llibreta:
    llista_clients = []

    def get_llista_clients(self):
        for client in self.llista_clients:
            print(client)

    def id_client_comptador(self):
        if not self.llista_clients:
            return 1
        return len(self.llista_clients) + 1

    def afegir_client(self, nom, cognom, telefon, correu, adress, codi_postal, ciutat, provincia, pais):
        identificador = self.id_client_comptador()
        client = Client(identificador, nom, cognom, telefon, correu, adress,
                        codi_postal, ciutat, provincia, pais)
        self.llista_clients.append(client)

    def eliminar_client(self, id_client):
        trobat = False
        for client in self.llista_clients:
            if client.identificador == id_client:
                self.llista_clients.remove(client)
                print("CLIENT ELIMINAT")
                trobat = True
        if not trobat:
            print("NO S'HA TROBAT EL CLIENT")

    def cercar_per_id(self, id_client):
        for client in self.llista_clients:
            if client.identificador == id_client:
                return client
        print("NO S'HA TROBAT EL CLIENT")
        return None

    def cercar_per_nom(self, nom_client):
        clients_trobats = []
        trobat = False
        for client in self.llista_clients:
            if client.nom == nom_client:
                clients_trobats.append(client)
                trobat = True
        if not trobat:
            return None
        else:
            return clients_trobats

    def cercar_per_cognom(self, cognom_client):
        clients_trobats = []
        trobat = False
        for client in self.llista_clients:
            if client.cognom == cognom_client:
                clients_trobats.append(client)
                trobat = True
        if not trobat:
            return None
        else:
            return clients_trobats

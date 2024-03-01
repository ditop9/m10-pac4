class Client:
    def __init__(self, identificador, nom, cognom, telefon, correu, adress, codi_postal, ciutat, provincia, pais):
        self.identificador = identificador
        self.nom = nom
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adress = adress
        self.codi_postal = codi_postal
        self.ciutat = ciutat
        self.provincia = provincia
        self.pais = pais

    def __str__(self):
        print(f"Nom i cognoms: {self.nom}" f"{self.cognom}")
        print(f"Identificador: {self.identificador}")
        print(f"Telèfon: {self.telefon}")
        print(f"Correu electrǹic: {self.correu}")
        print(f"Adreça: {self.adress}")
        print(f"Ciutat: {self.ciutat}" f"{self.codi_postal}")
        print(f"Província: {self.provincia}")
        print(f"País: {self.pais}")

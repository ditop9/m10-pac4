"""Classe per la creació de nous clients"""


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
        return (f"Nom i cognoms: {self.nom} {self.cognom}\n"
                f"Identificador: {self.identificador}\n"
                f"Telèfon: {self.telefon}\n"
                f"Correu electrònic: {self.correu}\n"
                f"Adreça: {self.adress}\n"
                f"Ciutat: {self.ciutat} {self.codi_postal}\n"
                f"Província: {self.provincia}\n"
                f"País: {self.pais}\n")

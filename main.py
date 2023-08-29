# Programme pour chercher des expressions à partir de mots-clés
from session import creer_session
from tkinter import *

session = creer_session()  # Créer une session


def afficher_expressions(mots):
    "Afficher les résultats de recherche pour le/les mots entré(s)"
    resultats = []  # Liste des résultats de recherche
    # Rechercher tous les éléments de type h3
    h3_elements = session.html.xpath("//h3")
    for h3 in h3_elements:  # Pour chaque élément h3
        for mot in mots:  # Pour chaque mot entré par l'utilisateur
            if mot in h3.text:  # Si le mot est contenu dans le texte de l'élément h3
                print(h3.text)
                # Ajouter le texte de l'élément h3 aux résultats de recherche
                resultats.append(h3.text)

    return resultats


class Application(Tk):
    "Application"

    def __init__(self):
        super().__init__()
        self.title("Chercheur d'expressions")  # Nommer la fenêtre
        # Créer un label pour indiquer à l'utilisateur ce qu'il doit taper
        self.label_recherche = Label(
            self, text="Tapez une lettre/un mot en Français:")
        self.label_recherche.pack()
        self.barre_recherche = Entry(self)  # Créer une barre de recherche
        self.barre_recherche.pack()
        self.bouton_recherche = Button(
            self, text="Rechercher des expressions", command=self.rechercher_expressions)
        self.bouton_recherche.pack()
        # Liste graphique pour représenter les résultats de recherche
        self.liste_resultats = Listbox(self)
        self.liste_resultats.pack(fill="both", expand=True)

        historique = self.obtenir_historique()
        print(historique)

    def rechercher_expressions(self):
        "Rechercher des expressions en fonction des mots/lettres tapé(e)s par l'utilisateur"
        self.liste_resultats.delete(0, "end")
        # Transformer en liste le contenu de la barre de recherche
        mots_tapes = list(self.barre_recherche.get())
        resultats = afficher_expressions(
            mots_tapes)  # Rechercher des résultats
        if resultats == []:  # S'il n'y a aucun résultat pour la recherche
            self.liste_resultats.insert(
                END, "Il n'y a aucun résultat pour votre recherche")

        else:  # S'il y a des résultats
            for expression in resultats:  # Pour chaque expression dans les résultats
                # Insérer l'expression dans la liste des résultats
                self.liste_resultats.insert(END, expression)

        self.sauvergarder_historique()  # Sauvergarder la recherche dans l'historique

    def sauvergarder_historique(self):
        "Sauvegarder les recherches dans un historique"
        # Indiquer un fichier de sauvegarde pour l'historique
        fichier_sauvegarde = "history.txt"
        recherche = self.barre_recherche.get()  # Recherche de l'utilisateur
        # Obtenir tous les résulats de recherche
        resultats_recherche = self.liste_resultats.get(
            first=0, last=self.liste_resultats.size())
        with open(fichier_sauvegarde, "w") as f:  # Ouvrir le fichier "history.txt", en écriture
            f.write(recherche)  # Ecrire la recherche de l'utilisateur
            # Ecrire les résultats de recherche
            f.write(str(resultats_recherche))
            f.close()  # Fermer le fichier quand le processus d'écriture est terminé

    def obtenir_historique(self):
        "Obtenir l'historique enregistré"
        fichier_historique = "history.txt"  # Indiquer le fichier où chercher l'historique
        recherche_resultats = {}
        with open(fichier_historique, "r") as f:
            for recherche, resultat in f.read():  # Pour les recherches et leurs résultats trouvés
                recherche_resultats[recherche] = resultat

        return recherche_resultats


app = Application()
app.mainloop()

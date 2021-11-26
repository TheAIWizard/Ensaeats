from PyInquirer import prompt
from PyInquirer.separator import Separator
from client.view.abstract_view import AbstractView
from client.view.welcom_view import WelcomeView

import requests

class AuthentificationView(AbstractView):
    
    def display_info(self):
        pass
     
    def make_choice(self):
             
        question = [{
            'type': 'list',
            'name': 'Menu',
            'message': "Avez vous deja un compte \n",
            'choices': ['Oui', Separator(), 'Non']
        }]
        reponse = prompt(question)
        if reponse['Menu']=='Oui':
            self.identifiant = input("Entrez votre identifiant client:   ")
            self.mot_de_passe = input("Entrez votre mot de passe:   ")
            #sans erreur d'authentification, on passe à la view suivante
            try:
                parametres = {"identifiant_client" : self.identifiant , "mot_de_passe_client" : self.mot_de_passe}
                self.client=requests.get('http://localhost:8000/clients/',params=parametres).json()
                #self.client=ClientService.authenticate_and_get_client(identifiant=self.identifiant, password=self.mot_de_passe)
                AbstractView.session.client = self.client
                AbstractView.session.identifiant = self.identifiant
                AbstractView.session.mot_de_passe = self.mot_de_passe
                return WelcomeView()
            except Exception:
                return AuthentificationView()
        else:
            self.nom= input("Nom: ")
            self.prenom= input("Prénom: ")
            self.adresse= input("Adresse: ")
            self.telephone= input("Numéro de téléphone: ")
            self.identifiant= input("Créez votre identifiant client: ")
            self.mot_de_passe= input("Créez votre mot de passe client: ")
            
            self.client_json={
                "id_client": 0,
                "nom": self.nom,
                "prenom": self.prenom,
                "adresse": self.adresse,
                "identifiant": self.identifiant,
                "mot_de_passe": self.mot_de_passe,
                "telephone": self.telephone}
            try:
                self.client=requests.post('http://localhost:5000/clients/',json=self.client_json).json()

                AbstractView.session.client = self.client
                AbstractView.session.nom = self.nom
                AbstractView.session.prenom = self.prenom
                AbstractView.session.adresse = self.adresse
                AbstractView.session.identifiant = self.identifiant
                AbstractView.session.mot_de_passe = self.mot_de_passe
                AbstractView.session.telephone = self.telephone
                return WelcomeView()
            except Exception:
                return AuthentificationView()
      
            
            
        
        
        
from PyInquirer import prompt
from PyInquirer.separator import Separator
from api.metier.adresse import Adresse
from client.view.abstract_view import AbstractView
from client.view.welcom_view import WelcomeView
from client.service.client_service import ClientService
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
            
            try :
                self.client = ClientService.getClient(self.identifiant, self.mot_de_passe)
                AbstractView.session.client = self.client
                AbstractView.session.identifiant = self.identifiant
                AbstractView.session.mot_de_passe = self.mot_de_passe
                return WelcomeView()
            #s'il y a une erreur au niveau de la requête, on retourne la page d'authentification
            except:
                from client.view.authentification_view import AuthentificationView
                return AuthentificationView()
            
                
        else:
            ## Creation d'un nouveau client
            self.nom = input("Nom: ")
            self.prenom = input("Prénom: ")
            self.adresse = input("Adresse: ")
            self.telephone = input("Numéro de téléphone: ")
            self.identifiant = input("Créez votre identifiant client: ")
            self.mot_de_passe = input("Créez votre mot de passe client: ")
            
            self.client_json={
                "id_client": 0,
                "nom": self.nom,
                "prenom": self.prenom,
                "adresse": self.adresse,
                "identifiant": self.identifiant,
                "mot_de_passe": self.mot_de_passe,
                "telephone": self.telephone}
            try:
                self.client=requests.post('http://localhost:8000/clients/',json=self.client_json).json()

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
      
            
            
        
        
        
from PyInquirer import prompt
from pydantic.main import ModelMetaclass
from PyInquirer.separator import Separator
from client.view.abstract_view import AbstractView
from client.view.welcom_view import WelcomeView
from client.service.client_service import ClientService
from client.business.client import Client
from client.exception.client_not_authenticated_exception import ClientNotAuthenticated

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
                self.client=ClientService.authenticate_and_get_client(identifiant=self.identifiant, password=self.mot_de_passe)
                AbstractView.session.client = self.client
                AbstractView.session.id_client = self.client.id_client
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
            self.create_identifiant= input("Créez votre identifiant client: ")
            self.create_mot_de_passe= input("Créez votre mot de passe client: ")
            
            self.nouveau_client=Client(id_client = 1, nom=self.nom, prenom=self.prenom, adresse=self.adresse, 
            identifiant=self.create_identifiant, mot_de_passe=self.create_mot_de_passe, telephone=self.telephone)
            try:
                self.nouveau_client=ClientService.createClient(self.nouveau_client)

                AbstractView.session.nouveau_client = self.nouveau_client
                AbstractView.session.id_client = self.nouveau_client.id_client
                AbstractView.session.nom = self.nom
                AbstractView.session.prenom = self.prenom
                AbstractView.session.adresse = self.adresse
                AbstractView.session.create_identifiant = self.create_identifiant
                AbstractView.session.create_mot_de_passe = self.create_mot_de_passe
                AbstractView.session.create_telephone = self.telephone
                return WelcomeView()
            except Exception:
                return AuthentificationView()
      
            
            
        
        
        
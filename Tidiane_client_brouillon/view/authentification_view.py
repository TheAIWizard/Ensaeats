from PyInquirer import prompt
from pydantic.main import ModelMetaclass

from Tidiane_client_brouillon.view.abstract_view import AbstractView
from Tidiane_client_brouillon.view.welcom_view import WelcomeView
from client.service.client_service import ClientService
from client.business.client import Client
from client.exception.client_not_authenticated_exception import ClientNotAuthenticated

class AuthentificationView(AbstractView):
    
    def display_info(self):
        pass
     
    def make_choice(self):
        #si on ne mets pas cette ligne inutile avant, ça ne fonctionne pas
        #sinon problème d'accès aux paramètres de .env pour db_connection
        self.debug=ClientService.consulter_menu("LTy9AUgMnLn8YS21KfFZ8g")
        self.sign_in= input("Avez-vous déjà un compte ? (oui|non): ")
        if self.sign_in=='oui':
            self.identifiant = input("Entrez votre identifiant client: ")
            self.mot_de_passe = input("Entrez votre mot de passe:")
            #sans erreur d'authentification, on passe à la view suivante
            try:
                self.client=ClientService.authenticate_and_get_client(identifiant=self.identifiant, password=self.mot_de_passe)
                AbstractView.session.client = self.client
                
                AbstractView.session.identifiant = self.identifiant
                AbstractView.session.mot_de_passe = self.mot_de_passe
                return WelcomeView()
            except Exception:
                return AuthentificationView()
        elif self.sign_in=='non':
            self.nom= input("Nom: ")
            self.prenom= input("Prénom: ")
            self.adresse= input("Adresse: ")
            self.telephone= input("Numéro de téléphone: ")
            self.create_identifiant= input("Créez votre identifiant client: ")
            self.create_mot_de_passe= input("Créez votre mot de passe client: ")
            
            self.nouveau_client=Client(nom=self.nom, prenom=self.prenom, adresse=self.adresse, 
            identifiant=self.create_identifiant, mot_de_passe=self.create_mot_de_passe, telephone=self.telephone)
            try:
                self.nouveau_client=ClientService.createClient(self.nouveau_client)

                AbstractView.session.nouveau_client = self.nouveau_client

                AbstractView.session.nom = self.nom
                AbstractView.session.prenom = self.prenom
                AbstractView.session.adresse = self.adresse
                AbstractView.session.create_identifiant = self.create_identifiant
                AbstractView.session.create_mot_de_passe = self.create_mot_de_passe
                AbstractView.session.create_telephone = self.telephone
                return WelcomeView()
            except Exception:
                return AuthentificationView()
        else:
            self.erreur_sign_in = print("Argument invalide: tapez oui ou non")
            AbstractView.session.erreur_sign_in = self.sign_in
            
            
        
        
        
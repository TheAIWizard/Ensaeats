from PyInquirer import prompt
from pydantic.main import ModelMetaclass

from Tidiane_client_brouillon.view.abstract_view import AbstractView
from Tidiane_client_brouillon.view.welcom_view import WelcomeView
from client.service.client_service import ClientService
from client.exception.client_not_authenticated_exception import ClientNotAuthenticated

class AuthentificationView(AbstractView):
    
    def display_info(self):
        pass
     
    def make_choice(self):
        self.identifiant = input("Entrez votre identifiant client: ")
        self.mot_de_passe = input("Entrez votre mot de passe:")
        self.client = ClientService.getClient(self.identifiant)
        try:
            self.client=ClientService.authenticate_and_get_client(identifiant=self.identifiant, password=self.mot_de_passe)
        except Exception:
            AbstractView.session.client = self.client
        
        return WelcomeView()
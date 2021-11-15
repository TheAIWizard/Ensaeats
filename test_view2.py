from Tidiane_client_brouillon.view.authentification_view import AuthentificationView
from Tidiane_client_brouillon.view.welcom_view import WelcomeView

# C'est le script qui va être le point d'entrée de notre application.

if __name__ == '__main__':
    # on démarre sur l'écran accueil
    current_vue = WelcomeView()

    # tant qu'on a un écran à afficher, on continue
    while current_vue:
        # on affiche une bordure pour séparer les vue
        with open('Tidiane_client_brouillon/view/assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
        # les infos à afficher
        current_vue.display_info()
        # le choix que doit saisir l'utilisateur
        current_vue = current_vue.make_choice()



    
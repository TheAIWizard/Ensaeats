from client.view.authentification_view import AuthentificationView

# C'est le script qui va être le point d'entrée de notre application.

if __name__ == '__main__':
    # on démarre sur l'écran accueil
    current_vue = AuthentificationView()

    # tant qu'on a un écran à afficher, on continue
    while current_vue:
        # on affiche une bordure pour séparer les vue
        with open('client/view/assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read()) 
        # les infos à afficher
        current_vue.display_info()

        # le choix que doit saisir l'utilisateur
        current_vue = current_vue.make_choice()

    
    
    


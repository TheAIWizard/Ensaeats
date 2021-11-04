from PyInquirer import Separator, prompt

from view.abstract_vue import AbstractView




class StartView(AbstractView):

    def __init__(self):
        self.questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Bonjour',
                'choices': [
                    'Next'

                ]
            }
        ]

    def display_info(self):
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['choix'] == 'Next':
            from view.welcome_view import WelcomeView
            return WelcomeView()

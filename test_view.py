from PyInquirer import prompt, Separator
questions = [
            {
                'type': 'list',
                'name': 'Menu',
                'message': 'Choisir un option',
                'choices': ['Consulter Menus',
                Separator(),
                'Consulter les avis',
                Separator(),
                'Accueil']
            }
        ]

reponse = prompt(questions)

print(reponse['Menu'])
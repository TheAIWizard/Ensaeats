from API.metier.article import Article
import hashlib
import random

class Menu(): 
    def __init__(self, nom : str, prix : int, article1 : Article, article2 : Article, article3 : Article): 
        self.nom = nom
        self.prix = prix 
        self.article1 = article1
        self.article2 = article2
        self.article3 = article3
        self.id_menu = 1 
        # appel à add_menu -> recupere l'id 
    
    def recup_menu(self): 
        ''' grâce aux id article on peut récupérer les compositions et type d'articles '''
        menu = {"article1" : self.article1.article_desc(),"article2" : self.article2.article_desc(), "article3": self.article3.articledesc()}

    def id_menu_hash(self,digit=10):
        """ DEFINITION DE id_menu"""
        #les id_menu sont haché sous 10 digits
        """ afin d'éviter de réfléchir ou de structurer l'architecture de notre programme sur l'auto-incrémentation des tables,
            nous allons définir id_menu en hachant la concatenation du nom et du prix le composant sous forme de 10 digits.
            L'algorithme de hachage sha512 implémenté en langage Python retourne la même sortie pour une entrée donnée en limitant les collisions.
            L'intérêt : définir de manière unique id_menu de chaque menu sans auto-incrémentation
            Bien que pratique, l'auto-incrémentation peut créer des problèmes de rang. Or, nous serons amenés à
            ajouter, supprimer ou modifier de nombreuses lignes de table."""
        caractere_a_hacher=self.nom+str(self.prix)
        #pour limiter le cas où des menus provenant de restaurants différents ayant un nom et prix identiques, aient le même id_menu
        #on mélange la concaténation du nom et du prix avant hashage.
        caractere_a_hacher_melange = ''.join(random.shuffle(list(caractere_a_hacher)))

        #mise à jour de id_menu
        self.id_menu=int(hashlib.sha512(caractere_a_hacher_melange.encode("utf-8")).hexdigest(), 16) % (10 ** digit)
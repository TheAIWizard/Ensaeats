import requests
from bs4 import BeautifulSoup
import json
import hashlib
from os.path import exists

""" ETAPE 1: SCRAPER LE SITE OFFICIEL SUR LA PAGE YELP ASSOCIE AU SITE DU RESTAURANT """

page=requests.get('https://www.yelp.com/biz/la-fontaine-aux-perles-rennes')

#conversion de la page en objet BeautifulSoup
#html_page = urlopen(page)
soup = BeautifulSoup(page.text, "html.parser")
see_better= soup.prettify()

#après inspecter élément sur le lien du site du restaurant, on a toujours le lien dans la div <a> avec class="css-ac8spe" sur YELP
#on peut donc remonter au lien de redirection vers le site internet officiel du restaurant en recupérant tous les liens contenant 'http' de cette division
recup_lien=[link.get('href') for link in soup.findAll('a',{'class':"css-ac8spe"}) if 'http' in link.get('href')]

#si la liste est vide, on peut pas récupérer de lien (non répertorié sur YELP)
lien_existe=(recup_lien!=[])

#pour accéder au site on rajoute 'https://www.yelp.com'
lien='https://www.yelp.com'+recup_lien[0] if lien_existe else None

""" ETAPE 2: RECUPERER LE SITE OFICIEL SUR LA PAGE DE REDIRECTION"""


#accedons à la page de redirection vers la page officielle du restaurant
page_officiel_redirect=requests.get(lien)
#conversion en objet Beautifulsoup pour scraping
soup_redirect = BeautifulSoup(page_officiel_redirect.text, "html.parser")
#la page de redirection ne contient que des <string>, retrouvons le lien de la page officielle
script_page_officiel=[(script.string) for script in soup_redirect.findAll('script') if 'http' in script.string][0] #ne contient qu'un élément
#si la page se finit par .com on extrait de 'http' à 'm'(de 'com') sinon on extrait jusqu'au 'r' de 'fr
lien_page_officiel=script_page_officiel[script_page_officiel.find('http'):script_page_officiel.find('m')]+'m' if 'com' in script_page_officiel else script_page_officiel[script_page_officiel.find('http'):script_page_officiel.find('r')]+'r'

""" ETAPE 3: SCRAPER LE LIEN DE LA PAGE DE LA CARTE OU DES MENUS SUR LE SITE OFFICIEL DU RESTAURANT"""


page_officiel=requests.get(lien_page_officiel)
#conversion en objet Beautifulsoup pour scraping
soup_officiel = BeautifulSoup(page_officiel.text, "html.parser")
#recuperons tous les liens pouvant amener à un menu ou une carte
recup_lien_menu=[link.get('href') for link in soup_officiel.findAll('a') if ('menu' in link.get('href')) or ('carte' in link.get('href'))]
#prenons le premier résultat qui nous ai donné
lien_page_menu=recup_lien_menu[0]

""" accédons à la page du menu """
page_menu=requests.get(lien_page_menu)
#conversion en objet Beautifulsoup pour scraping
soup_menu = BeautifulSoup(page_menu.text, "html.parser")
#récupérons les sections de page liés aux menus
extract_page_menu=soup_menu.findAll('div',{'class',"small-12 medium-12 large-12 cell"})

''' Menu : (id_menu (NUMERIC), nom (CHAR), prix (NUMERIC) '''
#liste des menus
liste_menu=[menu.string[menu.string.find('M'):].rstrip() for menu in list(soup_menu.findAll('h2')) ] #.rstrip() enève les \n à la fin
#pour l'id des menus, hachons leur intitulé en 6 digits
id_menu=[int(hashlib.sha512(str_menu.encode("utf-8")).hexdigest(), 16) % (10 ** 6)  for str_menu in liste_menu]
# récupérons le prix de chaque menu : on converti les str en numeric en enlevant '€'
prix_menu=[int(prix.string.strip().split()[0]) for prix in soup_menu.findAll('div',{'class':'price-menu'})]

''' Article: (id_article(NUMERIC), nom (CHAR) , type_article (CHAR), composition (char) '''
#liste des articles
liste_plat=[plat.string for plat in list(soup_menu.findAll('strong'))][:-1]
#pour l'id des plats, hachons leur intitulé en 7 digits
id_plat=[int(hashlib.sha512(str_menu.encode("utf-8")).hexdigest(), 16) % (10 ** 7)  for str_menu in liste_plat]
type_article,composition=[],[]

''' Gestion du type d'article : entrée, plat, dessert par rapport aux balise des images'''
#compliqué on considéré que ce sont tous des plats. Sinon il faudra faire du cas par cas, par rapport à l'emplacement des images sur le site ...
#une autre manière serait de créer un dictionnaire sur le nom des articles pour en déduire son type-article

''' Menu_Article : id_menu id_article'''
#itérons sur chaque bloc de page correspondant à des menus et préparons les tuples pour les tables SQL
table_menu_article=[]
i=0
for div in list(extract_page_menu) :
    # à chaque menu, on a la composition (dans <em>) de chaque plat (dans <strong>) dans l'ordre de la liste composition
    composition_div=[composition.string for composition in div.find_all('em')] 
    #concaténons à la liste de composition des plats
    composition+=composition_div
    if div.find_all('strong') != []:
        # les articles pour un menu donné
        plats=[plat.string for plat in div.find_all('strong')]
        # pour chaque menu, on recupère le tuple (id_menu, id_article) : id_menu, hachage en 6 digits et id_article, hachage en 7 digits
        table_menu_article_div=[(id_menu[i],int(hashlib.sha512(article.encode("utf-8")).hexdigest(), 16) % (10 ** 7)) for article in plats]
        #concaténons à la liste des tuples d'id (id_menu,id_article)
        table_menu_article+=table_menu_article_div
        #itérons pour l'id_menu suivant
        i+=1

        
    
#on en déduit les tuples recherché pour la construction des tables: table_menu, table_article, table_menu_article
table_menu=list(zip(id_menu,liste_menu,prix_menu))
table_article=list(zip(id_plat,liste_plat,['plat' for i in range(len(id_plat))],composition))
print(table_menu_article)

#print(soup_menu.findAll('div',{'class',"small-12 medium-12 large-12 cell"}))

""" ETAPE 4: STOCKER LES RESULTATS DANS DES FICHIERS TXT"""
#récupération des résultats dans un fichier .txt

#tuples pour la table menu
#si le fichier n'existe pas déjà
if not(exists('brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_menu.txt')):
    menu = open("brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_menu.txt", "w",encoding="utf-8") 
    for element in table_menu:
        menu.write(str(element) + ",\n")
    menu.close()
else:
    #sinon on rajoute du contenu au fichier déjà existant
    with open('brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_menu.txt', 'a+') as f:
        for element in table_menu:
            f.write(str(element) + ",\n")
            f.close()

#tuples pour la table article
#si le fichier n'existe pas déjà
if not(exists('brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_article.txt')):
    article = open("brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_article.txt", "w",encoding="utf-8") 
    for element in table_article:
        article.write(str(element) + ",\n")
    article.close()
else:
    #sinon on rajoute du contenu au fichier déjà existant
    with open('brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_article.txt', 'a+') as f:
        for element in table_article:
            f.write(str(element) + ",\n")
            f.close()

#tuples pour la table menu
#si le fichier n'existe pas déjà
if not(exists('brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_menu_article.txt')):
    menu_article = open("brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_menu_article.txt", "w",encoding="utf-8") 
    for element in table_menu_article:
        menu_article.write(str(element) + ",\n")
    menu_article.close()
else:
    #sinon on rajoute du contenu au fichier déjà existant
    with open('brouillon/scraping_db_building/donnees_scrappees_txt/scrap_table_menu_article.txt', 'a+') as f:
        for element in table_menu_article:
            f.write(str(element) + ",\n")
            f.close()

""" ETAPE 5: REITERER TOUTES CES ETAPES AVEC LES AUTRES URL DONNEES PAE LE PROGRAMME recup_partie_url_restau ..."""

#Récupérons tout d'abord les restaurants de YELP ayant des liens de redirection vers le site officiel sur YELP

#Affichons le nom des restaurants à scrapper

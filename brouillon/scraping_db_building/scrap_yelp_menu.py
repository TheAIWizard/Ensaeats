import requests
from bs4 import BeautifulSoup
import json

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
#liste des articles
liste_plat=[plat.string for plat in list(soup_menu.findAll('strong'))][:-1]
#liste des menus
liste_menu=[menu.string[menu.string.find('M'):].rstrip() for menu in list(soup_menu.findAll('h2')) ][:-1] #.rstrip() enève les \n
#listons les infos d'un menu dans un dictionnaire : { 'menu': [str] , 'prix': [int], 'article': [list]}
menu_1=dict()
#récupérons les sections de page liés aux menus
extract_page_menu=soup_menu.findAll('div',{'class',"small-12 medium-12 large-12 cell"})
#itérons sur chaque bloc de page correspondant à des menus
for row in list(soup_menu.findAll('div',{'class',"small-12 medium-12 large-12 cell"})) :
    cells = row.find_all(['h2', 'div class="price-menu"','strong'])
    for cell in cells:
        print(cell.name, cell.attrs)




  

""" ANNEXE
#ce qui a donné l'idée
links = []
for link in soup.findAll('a'):
    if link.get('href') is not None:
        # on ne retient que les liens contenant le mot-clé "http"
        if 'http' in link.get('href'):
            links.append(link.get('href')) 
            print(link.get('href')) """


""" 
#autre manière de faire ...
regex_pattern_to_find_all_links = r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
urls = re.findall(regex_pattern_to_find_all_links, str(soup))
print(urls) """
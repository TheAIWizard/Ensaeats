import requests
from bs4 import BeautifulSoup

""" ETAPE 1: SCRAPER LE SITE OFFICIEL SUR LA PAGE YELP ASSOCIE AU SITE DU RESTAURANT """

page=requests.get('https://www.yelp.com/biz/le-pagnol-bruz-2')

#conversion de la page en objet BeautifulSoup
#html_page = urlopen(page)
soup = BeautifulSoup(page.text, "html.parser")
see_better= soup.prettify()

#après inspecter élément sur le lien du site du restaurant, on a toujours le lien dans la div <a> avec class="css-ac8spe" sur YELP
#on peut donc remonter au site internet officiel du restaurant en recupérant tous les liens contenant 'http' de cette division
recup_lien=[link.get('href') for link in soup.findAll('a',{'class':"css-ac8spe"}) if 'http' in link.get('href')]

#si la liste est vide, on peut pas récupérer de lien (non répertorié sur YELP)
lien_existe=(recup_lien!=[])

#pour accéder au site on rajoute 'https://www.yelp.com'
lien='https://www.yelp.com'+recup_lien[0] if lien_existe else None

""" ETAPE 2: SCRAPER LES MENU SUR LE SITE OFFICIEL DU RESTAURANT"""
print(lien)









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
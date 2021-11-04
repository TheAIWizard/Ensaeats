import requests
import pandas as pd
import hashlib
params = {'term': 'restaurant','location': 'Bruz', 'latitude': 48.05089, 'longitude': -1.74192, 'limit':50, 'sort_by': 'rating', 'radius': 20000}
r=requests.get('https://api.yelp.com/v3/businesses/search',headers={'Authorization': 'Bearer fn70eRh36s5xOBDKdreUKbTNiwwzcMCgh3ydHo8UwT5dSFe_lqle6YLhKN1Xh29LqCf9AmLCmpjksKRa0fWvoWg4RuFS5GhyEvFqMWPMKqILPpx2NHaONy5GOjl4YXYx'},params=params)
json=r.json()
df=pd.DataFrame(json['businesses'])
extract_restaurant=df[['id','name']]

''' au choix soit on choisit id_restaurant à la main : celui du premier c'est 1 etc... ou soit on prend la version hachée des business_id de YELP
plutôt que créer des id_restaurant(NUMERIC) à la main, nous allons hacher les business_id de YELP existant en 8 digits
n'importe quelle fonction de hachage fonctionnelle conviendra, ce n'est pas une donnée sensible
garder la même fonction de hachage nous permettra de convertir aisément les id de type str en digit.'''

#ajout colonne id haché: l'algo de hachage sha512 ressort le même hachage pour la même entrée sur Python
df['id_hash']=df['id'].apply(lambda x: int(hashlib.sha512(x.encode("utf-8")).hexdigest(), 16) % (10 ** 8) )
table_restaurant=df[['id','name']]


result_restaurant=list(table_restaurant.to_records(index=False))

#récupération des résultats dans un fichier .txt
file = open("brouillon/scraping_db_building/donnees_scrappees_txt/tuple_id_nom_restaurant.txt", "w",encoding="utf-8") 
for element in result_restaurant:
    file.write(str(element) + ",\n")
file.write(";")
file.close()

print(df)
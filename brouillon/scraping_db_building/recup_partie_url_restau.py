import requests
import pandas as pd
params = {'term': 'restaurants','location': 'Bruz', 'latitude': 48.05089, 'longitude': -1.74192, 'limit':50, 'sort_by': 'rating', 'radius': 20000}
r=requests.get('https://api.yelp.com/v3/businesses/search',headers={'Authorization': 'Bearer fn70eRh36s5xOBDKdreUKbTNiwwzcMCgh3ydHo8UwT5dSFe_lqle6YLhKN1Xh29LqCf9AmLCmpjksKRa0fWvoWg4RuFS5GhyEvFqMWPMKqILPpx2NHaONy5GOjl4YXYx'},params=params)
json=r.json()
df=pd.DataFrame(json['businesses'])
df_business_id=df[['url']]
list_business_id=(list(df['url']))

#récupération des résultats dans un fichier .txt
file = open("brouillon/scraping_db_building/donnees_scrappees_txt/yelp_business_url", "w",encoding="utf-8") 
for address in list_business_id:
    #file.write(address.replace('https://www.yelp.com/biz/','') + "\n") #si on souhaite recup que la partie après https:.../

    #extraction du texte avant '?'
    file.write(address[:address.find('?')] + "\n")
file.close()




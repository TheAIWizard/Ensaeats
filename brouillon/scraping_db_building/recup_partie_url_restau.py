import requests
import pandas as pd
params = {'location': 'Bruz,Brittany,France',}
r=requests.get('https://api.yelp.com/v3/businesses/search',headers={'Authorization': 'Bearer fn70eRh36s5xOBDKdreUKbTNiwwzcMCgh3ydHo8UwT5dSFe_lqle6YLhKN1Xh29LqCf9AmLCmpjksKRa0fWvoWg4RuFS5GhyEvFqMWPMKqILPpx2NHaONy5GOjl4YXYx'},params=params)
json=r.json()
df=pd.DataFrame(json['businesses'])
df_business_id=df[['url']]
list_business_id=(list(df['url']))

#récupération des résultats dans un fichier .txt
file = open("yelp_business_id", "w",encoding="utf-8") 
for address in list_business_id:
    file.write(address.replace('https://www.yelp.com/biz/','') + "\n")
file.close()



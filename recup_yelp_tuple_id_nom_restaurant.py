import requests
import pandas as pd
params = {'location': 'Bruz,Brittany,France',}
r=requests.get('https://api.yelp.com/v3/businesses/search',headers={'Authorization': 'Bearer fn70eRh36s5xOBDKdreUKbTNiwwzcMCgh3ydHo8UwT5dSFe_lqle6YLhKN1Xh29LqCf9AmLCmpjksKRa0fWvoWg4RuFS5GhyEvFqMWPMKqILPpx2NHaONy5GOjl4YXYx'},params=params)
json=r.json()
df=pd.DataFrame(json['businesses'])
extract_restaurant=df[['id','name']]
result_restaurant=list(extract_restaurant.to_records(index=False))

#récupération des résultats dans un fichier .txt
file = open("tuple_id_nom_restaurant.txt", "w",encoding="utf-8") 
for element in result_restaurant:
    file.write(str(element) + ",\n")
file.write(";")
file.close()

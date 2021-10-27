import requests
import pandas as pd
params = {'location': 'Bruz,Brittany,France',}
r=requests.get('https://api.yelp.com/v3/businesses/search',headers={'Authorization': 'Bearer fn70eRh36s5xOBDKdreUKbTNiwwzcMCgh3ydHo8UwT5dSFe_lqle6YLhKN1Xh29LqCf9AmLCmpjksKRa0fWvoWg4RuFS5GhyEvFqMWPMKqILPpx2NHaONy5GOjl4YXYx'},params=params)
json=r.json()
df=pd.DataFrame(json['businesses'])
df_business_id=df[['id']]
list_business_id=(list(df['id']))

list_requests=[]
for address in list_business_id:
    list_requests.append(requests.get("https://api.yelp.com/v3/businesses/"+address+"/reviews", headers={'Authorization': 'Bearer fn70eRh36s5xOBDKdreUKbTNiwwzcMCgh3ydHo8UwT5dSFe_lqle6YLhKN1Xh29LqCf9AmLCmpjksKRa0fWvoWg4RuFS5GhyEvFqMWPMKqILPpx2NHaONy5GOjl4YXYx'}))   
r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20=list_requests
pd.set_option("display.max_rows", None, "display.max_columns", None)

#création des tuples (id_avis,avis,id_restaurant)
aux=[]
id_restau,id_avis=0,200
for restau in list_requests:
    if restau.json()['reviews'] != []:
        for review in list(pd.DataFrame(r1.json()['reviews'])['text']):
            aux.append( (id_avis,review,list_business_id[id_restau]))
            id_avis+=1
    id_restau+=1
        
#récupération des résultats dans un fichier .txt
file = open("db_tuple_avis.txt", "w",encoding="utf-8") 
for element in aux:
    file.write(str(element) + ",\n")
file.write(";")
file.close()

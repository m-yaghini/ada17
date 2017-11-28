import requests,json,csv
import pandas as pd
from json_data_getter import get_all_json

namekey = 'LppAgNaKWacNPwVjmB'
namesurl = "https://gender-api.com/get?key=" + namekey

def getnameGender2(firstname):
    params = dict(key= namekey,name=firstname)
    resp  = requests.get(url=namesurl, params=params)
    namedata = json.loads(resp.text)
    return namedata["gender"]


_, _, documents = get_all_json()
df = pd.DataFrame.from_dict(documents)


gender_dict= dict()
gender_dict[' Pierandré']='male' #genderapi doesn't recognise and it comes a lot. So to avoid useless json queries


list_names = [[v[0]['name'] for v in contributors.values()] for contributors in df.contributors.values]
for idx,names in enumerate(list_names): # a lancer
    if(idx %100 == 0):
        print(idx,end=';')
    for name in names:
        if ',' in name: # only valid names contain comma ( lastname, firstname)
            firstname = name.split(',')[1]
            if firstname not in gender_dict and len(firstname.split())<2:
                print(firstname)
                gender=  getnameGender2(firstname)
                if gender != 'unknown':
                    gender_dict[firstname]=gender


with open('genderMain.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(gender_dict.items())
import requests
from pathlib import Path
import pandas as pd

path = r'./PdfsMontserrat/'
df = pd.read_csv('links3.csv')

for _,row in df.iterrows():

    url = row['link']
    file = url.split('/')[-1]

    if(file != ''):
        filename = Path(path + file)


        response = requests.get(url)

        filename.write_bytes(response.content)

        print (url)
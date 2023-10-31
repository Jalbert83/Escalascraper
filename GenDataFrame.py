import pandas as pd

# importing required modules
import PyPDF2
import re
import warnings
warnings.filterwarnings("ignore")

path = r'./PdfsMontserrat/'
df = pd.read_csv('links3.csv')
url = df.loc[0,'link']
filename = url.split('/')[-1]


fields = ['Via', 'Zona', 'Dificultat', 'Dificultat obligada', 'Llargària', 'Grau d’exposició', 'Grau de compromís', 'Equipament', 'Material', 'Orientació', 'Valoració']
dfInfo = pd.DataFrame(columns = fields)


for j, (_, row) in enumerate(df.iterrows()):
    url = row['link']
    dfInfo.loc[j, 'link'] = url
    filename = url.split('/')[-1]
    pdfFileObj = open(path + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for f in fields:
        dfInfo.loc[j, f] = ""
    for page in [pdfReader.getPage(i) for i in range(pdfReader.numPages)]:
        text = page.extractText()

        for f in fields:
            reg = f+r':.*$'
            res = re.search(reg, text, re.MULTILINE)
            if(res != None and res.group(0) != ''):
                if ((j == 140) and (f=='Valoració')):
                    a = 0
                val = res.group(0).split(':')[-1].strip()
                dfInfo.loc[j, f] = val
    print(j)

dfInfo.to_csv('MontserratTapiaInfo.csv')
dfInfo.to_excel('MontserratTapiaexcel.xlsx', engine='xlsxwriter')


pdfFileObj.close()
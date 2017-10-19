# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:26:00 2017

@author: JanHelge
"""

import matplotlib.pyplot as plt
import os, time, glob
import pandas as pd
import json
import requests
import pygal


def hentSkred(veg, fylke):
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    api = 'https://www.vegvesen.no/nvdb/api/v2/'
    headers =   { 'accept' : 'application/vnd.vegvesen.nvdb-v2+json',
                            'X-Client' : 'testapi.py',
                            'X-Kontaktperson' : 'jan.aalbu@vegvesen.no'}
    objType = 445 #Skred
    url = api + 'vegobjekter/' + str(objType)
    skredListe = [4198, 4199, 5351, 4200, 4201, 4202, 4203] #Lager liste for å itere igjennom til filter for API
    skredType = ['Stein', 'Jord', 'Is/stein', 'Snø', 'Is', 'Flomskred', 'Sørpeskred'] #Litt dårlig løysing for å legge til i Pandas DF, for bruk i graf
    data = []
    sNum = 0
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    for i in skredListe:
        filtre = {'egenskap': '2326=' + str(i), 'fylke': fylke, 'vegreferanse': veg}
        rstat = requests.get(url + '/statistikk', headers=headers, params=filtre)
        skredT = skredType[sNum]
        obj = rstat.json()
        pie_chart.add(skredtype, 
        #print (obj['antall'])
        #data.append((i, skredT, obj['antall']))
        sNum = sNum +  1
    df = pd.DataFrame(data, columns=('Skredkode', 'Skredtype', 'Antall'))
    gruppert = df.groupby(['Skredtype'])['Antall']
    gruppert.sum().plot(kind='bar')
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile
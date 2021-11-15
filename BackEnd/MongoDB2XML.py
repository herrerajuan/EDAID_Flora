# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:17:01 2021

@author: Ismael Navas
"""

import pymongo
from pymongo import MongoClient
import pandas as pd

from xml.etree.ElementTree import Element, SubElement, Comment, tostring


flora = Element('Flora')
comment = Comment('Data generated from MongoDB')
flora.append(comment)

client = pymongo.MongoClient("mongodb+srv://soledad03:coronavirusbdb@cluster0.epzrv.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.Flora
resultado = db.Flora.find()

df =  pd.DataFrame(list(resultado))
for index, row in df.iterrows() :
    fl = SubElement(flora, 'Data')
    #address = SubElement(restaurant, 'address')
    #address.text = row['address']
    num_register = SubElement(fl, 'num_register')
    num_register.text = str(row['num_register'])
    date = SubElement(fl, 'date')
    date.text = str(row['date'])
    author = SubElement(fl, 'author')
    author.text = row['author']
    location = SubElement(fl, 'location')
    location.text = row['location']
    UTM = SubElement(fl, 'UTM')
    UTM.text = row['UTM']
    lithology = SubElement(fl, 'lithology')
    lithology.text = row['lithology']
    coverage = SubElement(fl, 'coverage')
    coverage.text = str(row['coverage'])
    altitude = SubElement(fl, 'altitude')
    altitude.text = str(row['altitude'])
    plot_slope = SubElement(fl, 'plot_slope')
    plot_slope.text = str(row['plot_slope'])
    altitude_veg = SubElement(fl, 'altitude_veg')
    altitude_veg.text = str(row['altitude_veg'])
    plot_area = SubElement(fl, 'plot_area')
    plot_area.text = str(row['plot_area'])
    plot_orientation = SubElement(fl, 'plot_orientation')
    plot_orientation.text = row['plot_orientation']
    community = SubElement(fl, 'community')
    community.text = str(row['community'])
    abies_pinsapo = SubElement(fl, 'abies_pinsapo')
    abies_pinsapo.text = str(row['abies_pinsapo'])
    pinus_halepensis = SubElement(fl, 'pinus_halepensis')
    pinus_halepensis.text = str(row['pinus_halepensis'])
    juniperus_plumosa = SubElement(fl, 'juniperus_plumosa')
    juniperus_plumosa.text = str(row['juniperus_plumosa'])
    juniperus_oxycedrus = SubElement(fl, 'juniperus_oxycedrus')
    juniperus_oxycedrus.text = str(row['juniperus_oxycedrus'])
    ceratonia_siliqua = SubElement(fl, 'ceratonia_siliqua')
    ceratonia_siliqua.text = str(row['ceratonia_siliqua'])
    chaualiop_limitis = SubElement(fl, 'chaualiop_limitis')
    chaualiop_limitis.text = str(row['chaualiop_limitis'])
    ranunculus_aqualitis = SubElement(fl, 'ranunculus_aqualitis')
    ranunculus_aqualitis.text = str(row['ranunculus_aqualitis'])
    acu_frentence = SubElement(fl, 'acu_frentence')
    acu_frentence.text = str(row['acu_frentence'])
    sorbus_aria = SubElement(fl, 'sorbus_aria')
    sorbus_aria.text = str(row['sorbus_aria'])
    digitalis_obscura = SubElement(fl, 'digitalis_obscura')
    digitalis_obscura.text = str(row['digitalis_obscura'])
    athamanta_vayredana = SubElement(fl, 'athamanta_vayredana')
    athamanta_vayredana.text = str(row['athamanta_vayredana'])
    centaurea_clementei = SubElement(fl, 'centaurea_clementei')
    centaurea_clementei.text = str(row['centaurea_clementei'])
    campanula_mollis = SubElement(fl, 'campanula_mollis')
    campanula_mollis.text = str(row['campanula_mollis'])
    silene_andryalifolia = SubElement(fl, 'silene_andryalifolia')
    silene_andryalifolia.text = str(row['silene_andryalifolia'])
    sedum_dasphyllum = SubElement(fl, 'sedum_dasphyllum')
    sedum_dasphyllum.text = str(row['sedum_dasphyllum'])
    chaenorrhinum_villosum = SubElement(fl, 'chaenorrhinum_villosum')
    chaenorrhinum_villosum.text = str(row['chaenorrhinum_villosum'])
    rhamnus_myrtifolius = SubElement(fl, 'rhamnus_myrtifolius')
    rhamnus_myrtifolius.text = str(row['rhamnus_myrtifolius'])
    teucrium_similatum = SubElement(fl, 'teucrium_similatum')
    teucrium_similatum.text = str(row['teucrium_similatum'])
    cephalaria_leucantha = SubElement(fl, 'cephalaria_leucantha')
    cephalaria_leucantha.text = str(row['cephalaria_leucantha'])
    helictotrichon_filifolium_arundanum = SubElement(fl, 'helictotrichon_filifolium_arundanum')
    helictotrichon_filifolium_arundanum.text = str(row['helictotrichon_filifolium_arundanum'])
    thrincia_sp = SubElement(fl, 'thrincia_sp')
    thrincia_sp.text = str(row['thrincia_sp'])
    sanguisorba_minor = SubElement(fl, 'sanguisorba_minor')
    sanguisorba_minor.text = str(row['sanguisorba_minor'])
    scabiosa_turolensis_grosii = SubElement(fl, 'scabiosa_turolensis_grosii')
    scabiosa_turolensis_grosii.text = str(row['scabiosa_turolensis_grosii'])

    

print(tostring(flora))

f = open("floradesdemongodb.xml", "w")

f.write(str(tostring(flora, encoding='unicode')))

f.close()

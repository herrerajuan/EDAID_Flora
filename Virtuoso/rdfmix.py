# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:07:44 2021

@author: Ismael Navas
"""

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD

import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

catalogo = Element('')
with open('EDAID_Flora\\FloraCambiados.json', 'r', encoding='utf-8') as myfile:
    data=myfile.read()

obj = json.loads(data)


g = Graph()
result = g.parse("C:\\Users\\paula\\OneDrive - Universidad de Málaga\\Documentos\\CUARTO\\EDAID\\EDAID_Flora\\Ontologia\\Flora1.owl")
base = 'http://www.semanticweb.org/usuario/ontologies/2021/10/untitled-ontology-7'
#type = g.value(semweb, RDFS.label)


for row in obj:
    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#num_register"),
    Literal(str(row['num_register']), datatype=XSD.string)
    ))
    
    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#date"),
    Literal(str(row['date']), datatype=XSD.string)
    ))
    
    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#author"),
    Literal(str(row['author']), datatype=XSD.string)
    ))
    
    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#location"),
    Literal(str(row['location']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#UTM"),
    Literal(str(row['UTM']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#lithology"),
    Literal(str(row['lithology']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#coverage"),
    Literal(str(row['coverage']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#altitude"),
    Literal(str(row['altitude']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#plot_slope"),
    Literal(str(row['plot_slope']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#altitude_veg"),
    Literal(str(row['altitude_veg']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#plot_area"),
    Literal(str(row['plot_area']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#plot_orientation"),
    Literal(str(row['plot_orientation']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#community"),
    Literal(str(row['community']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#abies_pinsapo"),
    Literal(str(row['abies_pinsapo']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#pinus_halepensis"),
    Literal(str(row['pinus_halepensis']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#juniperus_plumosa"),
    Literal(str(row['juniperus_plumosa']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#juniperus_oxycedrus"),
    Literal(str(row['juniperus_oxycedrus']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#ceratonia_siliqua"),
    Literal(str(row['ceratonia_siliqua']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#chaualiop_limitis"),
    Literal(str(row['chaualiop_limitis']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#ranunculus_aqualitis"),
    Literal(str(row['ranunculus_aqualitis']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#acu_frentence"),
    Literal(str(row['acu_frentence']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#sorbus_aria"),
    Literal(str(row['sorbus_aria']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#digitalis_obscura"),
    Literal(str(row['digitalis_obscura']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#athamanta_vayredana"),
    Literal(str(row['athamanta_vayredana']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#centaurea_clementei"),
    Literal(str(row['centaurea_clementei']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#campanula_mollis"),
    Literal(str(row['campanula_mollis']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#silene_andryalifolia"),
    Literal(str(row['silene_andryalifolia']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#sedum_dasphyllum"),
    Literal(str(row['sedum_dasphyllum']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#chaenorrhinum_villosum"),
    Literal(str(row['chaenorrhinum_villosum']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#rhamnus_myrtifolius"),
    Literal(str(row['rhamnus_myrtifolius']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#teucrium_similatum"),
    Literal(str(row['teucrium_similatum']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#helictotrichon_filifolium_arundanum"),
    Literal(str(row['helictotrichon_filifolium_arundanum']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#thrincia_sp"),
    Literal(str(row['thrincia_sp']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#sanguisorba_minor"),
    Literal(str(row['sanguisorba_minor']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#scabiosa_turolensis_grosii"),
    Literal(str(row['scabiosa_turolensis_grosii']), datatype=XSD.string)
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#esEscrito"),
    URIRef(base + "#" + str(row['author'])),
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    RDF.type,
    URIRef(base + "#Register")
    ))

    result.add((
    URIRef(base + "#" + str(row['author'])),
    RDF.type,
    URIRef(base + "#Author")
    ))

    result.add((
    URIRef(base + "#" + str(row['location'])),
    RDF.type,
    URIRef(base + "#Location")
    ))

    result.add((
    URIRef(base + "#" + str(row['num_register'])),
    URIRef(base + "#localizadoEn"),
    URIRef(base + "#" + str(row['location'])),
))
  
f = open("PyFlora.owl", "w")
f.write(result.serialize(format="xml", encoding="utf-8").decode())
f.close()
#tostring(catalogo, encoding='unicode')

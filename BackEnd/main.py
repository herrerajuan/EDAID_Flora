# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:17:36 2021

@author: USUARIO
"""
from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://soledad03:coronavirusbdb@cluster0.epzrv.mongodb.net/Flora?ssl=true&ssl_cert_reqs=CERT_NONE")
mongo_db = client.get_database("Flora")
mongo_col = pymongo.collection.Collection(mongo_db, "Flora")

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("AplicacionFlora.html")

@app.route('/flora')
def list_flora():
    data = mongo_col.find()
    return render_template("flora.html", users = data, mostrar_enlace = True)

@app.route('/formulario', methods = ['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return render_template("formulario.html")
    elif request.method == 'POST':
        num_register = request.form['num_register']
        date = request.form['date']
        author = request.form['author']
        location = request.form['location']
        UTM = request.form['UTM']
        lithology = request.form['lithology']
        coverage = request.form['coverage']
        altitude = request.form['altitude']
        plot_slope = request.form['plot_slope']
        altitude_veg = request.form['altitude_veg']
        plot_area = request.form['plot_area']
        plot_orientation  = request.form['plot_orientation']
        community = request.form['community']
        abies_pinsapo = request.form['abies_pinsapo']
        pinus_halepensis = request.form['pinus_halepensis']
        juniperus_plumosa = request.form['juniperus_plumosa']
        juniperus_oxycedrus = request.form['juniperus_oxycedrus']
        ceratonia_siliqua = request.form['ceratonia_siliqua']
        chaualiop_limitis = request.form['chaualiop_limitis']
        ranunculus_aqualitis = request.form['ranunculus_aqualitis']
        acu_frentence = request.form['acu_frentence']
        sorbus_aria = request.form['sorbus_aria']
        digitalis_obscura = request.form['digitalis_obscura']
        athamanta_vayredana = request.form['athamanta_vayredana']
        centaurea_clementei = request.form['centaurea_clementei']
        campanula_mollis = request.form['campanula_mollis']
        silene_andryalifolia = request.form['silene_andryalifolia']
        sedum_dasphyllum = request.form['sedum_dasphyllum']
        chaenorrhinum_villosum = request.form['chaenorrhinum_villosum']
        rhamnus_myrtifolius = request.form['rhamnus_myrtifolius']
        teucrium_similatum = request.form['teucrium_similatum']
        cephalaria_leucantha = request.form['cephalaria_leucantha']
        helictotrichon_filifolium_arundanum = request.form['helictotrichon_filifolium_arundanum']
        thrincia_sp = request.form['thrincia_sp']
        sanguisorba_minor = request.form['sanguisorba_minor']
        scabiosa_turolensis_grosii = request.form['scabiosa_turolensis_grosii']
        especie = {"num_register" : num_register, "date": date, 
                "author" : author, "location" : location, "UTM" : UTM, 
                "lithology" : lithology, "coverage" : coverage, 
                "altitude" : altitude, "plot_slope" : plot_slope, 
                "altitude_veg" : altitude_veg, "plot_area" : plot_area, 
                "plot_orientation" : plot_orientation, "community" : community, 
                "abies_pinsapo" : abies_pinsapo, "pinus_halepensis" : pinus_halepensis, 
                "juniperus_plumosa" : juniperus_plumosa, "juniperus_oxycedrus" : juniperus_oxycedrus, 
                "ceratonia_siliqua" : ceratonia_siliqua, "chaualiop_limitis" : chaualiop_limitis,
                "ranunculus_aqualitis" : ranunculus_aqualitis, "acu_frentence" : acu_frentence, 
                "sorbus_aria" : sorbus_aria, "digitalis_obscura" : digitalis_obscura, 
                "athamanta_vayredana" : athamanta_vayredana, "centaurea_clementei" : centaurea_clementei,
                "campanula_mollis" : campanula_mollis, "silene_andryalifolia" : silene_andryalifolia, 
                "sedum_dasphyllum" : sedum_dasphyllum, "chaenorrhinum_villosum" : chaenorrhinum_villosum, 
                "rhamnus_myrtifolius" : rhamnus_myrtifolius, "teucrium_similatum" : teucrium_similatum,
                "cephalaria_leucantha" : cephalaria_leucantha, "helictotrichon_filifolium_arundanum" : helictotrichon_filifolium_arundanum, 
                "thrincia_sp" : thrincia_sp, "sanguisorba_minor" : sanguisorba_minor,
                "scabiosa_turolensis_grosii" : scabiosa_turolensis_grosii}
        mongo_col.insert_one(especie)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:17:36 2021

@author: USUARIO
"""
from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb+srv://soledad03:coronavirusbdb@cluster0.epzrv.mongodb.net/Flora?ssl=true&ssl_cert_reqs=CERT_NONE")
mongo_db = client.get_database('Flora')
mongo_col = pymongo.collection.Collection(mongo_db, 'Flora')

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    print("principal")
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
        print("post")
        OBJECTID = request.form['OBJECTID']
        MapCode = request.form['MapCode']
        MapClass = request.form['MapClass']
        MCVName = request.form['MCVName']
        MCVLevel = request.form['MCVLevel']
        HabAECOM = request.form['HabAECOM']
        HabCode = request.form['HabCode']
        Site = request.form['Site']
        AcresGIS = request.form['AcresGIS']
        Shape_Leng = request.form['Shape_Leng']
        CalVegType = request.form['CalVegType']
        CalVegCode = request.form['CalVegCode']
        SCWHRType = request.form['SCWHRType']
        CWHRCode = request.form['CWHRCode']
        GlobalRank = request.form['GlobalRank']
        StateRank = request.form['StateRank']
        Sensitive = request.form['Sensitive']
        CaCode = request.form['CaCode']
        MCVAlliance = request.form['MCVAlliance']
        MCVGroup = request.form['MCVGroup']
        MCVMacrogroup = request.form['MCVMacrogroup']
        CommunityLink = request.form['CommunityLink']
        Shape__Area = request.form['Shape__Area']
        Shape__Length = request.form['Shape__Length']
        especie = {"OBJECTID" : OBJECTID, "MapCode": MapCode, "MapClass" : 
                   MapClass, "MCVName" : MCVName, "MCVLevel" 
                   : MCVLevel, "HabAECOM" : HabAECOM, "HabCode" : HabCode, 
                   "Site" : Site, "AcresGIS" : AcresGIS, 
                   "Shape_Leng" : Shape_Leng, "CalVegType" : CalVegType, 
                   "CalVegCode" : CalVegCode, "SCWHRType" : SCWHRType, 
                   "CWHRCode" : CWHRCode, "GlobalRank" : GlobalRank, 
                   "StateRank" : StateRank, "Sensitive" : Sensitive, 
                   "CaCode" : CaCode, "MCVAlliance" : MCVAlliance, 
                   "MCVGroup" : MCVGroup, "MCVMacrogroup" : MCVMacrogroup, 
                   "CommunityLink" : CommunityLink, "Shape__Area" : Shape__Area,
                   "Shape__Length" : Shape__Length}
        mongo_col.insert_one(especie)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)